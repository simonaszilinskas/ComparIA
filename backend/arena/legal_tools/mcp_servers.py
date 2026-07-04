"""
Registry of agentic tools the model can call ("MCP servers" in the product UI).

ponytail: the only starter tool wraps an in-process function (no external
process/network session to manage), so this registry doesn't implement the
full MCP transport protocol (stdio/SSE) yet. The `id`/`openai_schema`/`handler`
shape is deliberately what a real MCP-backed entry would also need to provide,
so wiring in a real remote MCP server later is additive, not a rewrite.
"""

import logging
from dataclasses import dataclass
from typing import Awaitable, Callable

from backend.arena.web_search import search_web

logger = logging.getLogger("languia")


@dataclass(frozen=True)
class ToolDef:
    id: str
    label: str
    description: str
    openai_schema: dict
    handler: Callable[[dict], Awaitable[str]]


async def _web_search_handler(arguments: dict) -> str:
    query = arguments.get("query", "")
    if not query:
        return "Aucune requête fournie."

    results = await search_web(query, use_cache=True)
    if not results:
        return "Aucun résultat trouvé pour cette recherche."

    return "\n\n---\n\n".join(
        f"Source: {r.name} ({r.url})\n{r.content}".strip() for r in results
    )


AVAILABLE_MCP_SERVERS: dict[str, ToolDef] = {
    "web_search": ToolDef(
        id="web_search",
        label="Recherche web",
        description=(
            "Permet au modèle de rechercher des informations récentes sur le web "
            "en cours de réponse, s'il juge que c'est utile."
        ),
        openai_schema={
            "type": "function",
            "function": {
                "name": "web_search",
                "description": (
                    "Recherche des informations récentes sur le web pour répondre "
                    "à une question juridique ou factuelle."
                ),
                "parameters": {
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "La requête de recherche",
                        }
                    },
                    "required": ["query"],
                },
            },
        },
        handler=_web_search_handler,
    ),
}
