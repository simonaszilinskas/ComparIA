"""
Known-good OpenRouter equivalents for models in this instance's pool, used
only when agentic tools are enabled for a conversation.

OpenRouter standardizes tool-calling across providers (OpenAI-compatible
`tools`/`tool_calls`) and tracks per-model tool-call reliability, which is
more consistent than these models' direct endpoints (mostly Scaleway),
whose tool-calling support varies. Routing tool-enabled turns through
OpenRouter is scoped to this mapping only — a model without an entry here
just keeps using its normal endpoint (fail-open, not fail-closed).

Keyed by our internal LLMData id (str(uuid)). Verified against OpenRouter's
public /models catalog to exist and report `tools` in supported_parameters.
"""

OPENROUTER_MODEL_OVERRIDES: dict[str, str] = {
    "2c1d03bb-c089-4e04-ab70-59a029a63eef": "meta-llama/llama-3.3-70b-instruct",  # Llama 3.3 70B
    "8383a2cd-d687-47a4-b916-3535ab71ba2e": "google/gemma-3-27b-it",  # Gemma 3 27B
    "391b8ea0-37cf-4e6e-bc78-3cdd807934cf": "mistralai/mistral-small-3.2-24b-instruct",  # Mistral Small 3.2 24B
    "0875287d-6611-4c4b-92f7-6703e029a341": "google/gemma-4-26b-a4b-it",  # Gemma 4 26B A4B
    "51e17915-a07b-4a81-a121-ff618d5e6c16": "z-ai/glm-5.2",  # GLM 5.2
    "3cea8697-c38b-47e5-93dc-582a19fecf21": "qwen/qwen3-235b-a22b-2507",  # Qwen3 235B A22B Instruct
    "9c066f46-fb23-4b41-b8f2-de0d0b5038d0": "qwen/qwen3.6-35b-a3b",  # Qwen3.6 35B A3B
    "a97ee553-f339-4731-982c-656e4a88a919": "openai/gpt-oss-120b",  # GPT OSS-120B
    "7a65e7f3-0302-4482-9f09-b33c825e2d01": "qwen/qwen3.5-397b-a17b",  # Qwen 3.5 397B
    "b6155e2b-ef01-4c4d-b988-126651809ecd": "mistralai/mistral-medium-3-5",  # Mistral Medium 3.5
}
