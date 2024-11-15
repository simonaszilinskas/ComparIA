"""
The gradio utilities for chatting with a single model.
"""
import gradio as gr

import random
from languia.api_provider import get_api_provider_stream_iter

import time
from custom_components.customchatbot.backend.gradio_customchatbot.customchatbot import ChatMessage

from languia.utils import (
    ContextTooLongError,
    EmptyResponseError,
)
from languia import config

import logging

logger = logging.getLogger("languia")


def update_last_message(messages, text):
    if len(messages) < 1:
        return [ChatMessage(role="assistant", content=text)]
    # We append a new assistant message if last one was from user
    if messages[-1].role == "user":
        messages.append(gr.ChatMessage(role="assistant", content=text))
    else:
        messages[-1].content = text
    return messages


def bot_response(
    state,
    request: gr.Request,
    temperature=0.7,
    # top_p=1.0,
    max_new_tokens=2048,
    apply_rate_limit=True,
    use_recommended_config=True,
):
    start_tstamp = time.time()
    print("start:"+str(start_tstamp))
    # temperature = float(temperature)
    # top_p = float(top_p)
    # max_new_tokens = int(max_new_tokens)

    # if apply_rate_limit:
    #     ip = get_ip(request)
    #     ret = is_limit_reached(state.model_name, ip)
    #     if ret is not None and ret["is_limit_reached"]:
    #         error_msg = RATE_LIMIT_MSG + "\n\n" + ret["reason"]
    #         logger.warn(f"rate limit reached. error_msg: {ret['reason']}")
    #         # state.conv.update_last_message(error_msg)
    #         # yield (state, state.to_gradio_chatbot()) + (no_change_btn,) * 5
    #         raise RuntimeError(error_msg)

    messages, model_name = state.messages, state.model_name
    model_api_endpoints = [endpoint for endpoint in config.api_endpoint_info if endpoint["model_id"] == model_name]
        
    if model_api_endpoints == []:
        logger.critical("No endpoint for model name: " + str(model_name))
    else:
        if state.endpoint is None:
            state.endpoint = random.choice(model_api_endpoints)
            endpoint_name = state.endpoint["api_base"].split("/")[2]
            logger.info(f"picked_endpoint: {endpoint_name} for {model_name}")
        endpoint = state.endpoint
        endpoint_name = endpoint["api_base"].split("/")[2]
        if use_recommended_config:
            recommended_config = endpoint.get("recommended_config", None)
            if recommended_config is not None:
                temperature = recommended_config.get("temperature", float(temperature))
                # top_p = recommended_config.get("top_p", float(top_p))
                max_new_tokens = recommended_config.get(
                    "max_new_tokens", int(max_new_tokens)
                )
        try:
            stream_iter = get_api_provider_stream_iter(
                messages,
                endpoint,
                temperature,
                max_new_tokens,
                request,
            )
        except Exception as e:
            logger.error(
                f"Error in get_api_provider_stream_iter. error: {e}",
                extra={request: request},
            )

    # html_code = "<br /><br /><em>En attente de la réponse…</em>"

    # update_last_message(messages, html_code)
    # yield (state)

    for i, data in enumerate(stream_iter):
        if "output_tokens" in data:
            logger.debug(f"reported output tokens for api {endpoint['api_id']}:" + str(data["output_tokens"]))
            # Sum of all previous interactions
            # FIXME: some output cumulative completion_tokens count, and some only output this iteration's completion tokens count...
            if not state.output_tokens:
                state.output_tokens = 0

            state.output_tokens += data["output_tokens"]

        output = data.get("text")
        if output:
            output.strip()
            messages = update_last_message(messages, output)
            yield (state)

    output = data.get("text")
    if not output or output == "":
        logger.error(
            f"reponse_vide: {model_name}, data: " + str(data),
            exc_info=True,
            extra={request: request},
        )
        # logger.error(data)
        raise EmptyResponseError(f"No answer from API {endpoint_name} for model {model_name}")

    messages = update_last_message(messages, output)

    yield (state)