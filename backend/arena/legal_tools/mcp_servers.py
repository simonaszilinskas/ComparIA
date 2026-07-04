"""
Registry of agentic tools the model can call ("MCP servers" in the product UI).

Two kinds:
- LocalMCPServer: an in-process function, no external session needed.
- RemoteMCPServer: a genuine third-party MCP server, connected to over
  streamable HTTP at call time (see mcp_client.py).

Only servers listed here can be enabled — this is the allowlist. Never accept
a user-supplied URL/command.
"""

from dataclasses import dataclass
from typing import Awaitable, Callable, Literal

from backend.arena.web_search import search_web


@dataclass(frozen=True)
class LocalMCPServer:
    id: str
    label: str
    description: str
    # tool name -> (OpenAI function schema, handler)
    tools: dict[str, tuple[dict, Callable[[dict], Awaitable[str]]]]
    kind: Literal["local"] = "local"


@dataclass(frozen=True)
class RemoteMCPServer:
    id: str
    label: str
    description: str
    url: str
    kind: Literal["remote"] = "remote"


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


AVAILABLE_MCP_SERVERS: dict[str, LocalMCPServer | RemoteMCPServer] = {
    "web_search": LocalMCPServer(
        id="web_search",
        label="Recherche web",
        description=(
            "Permet au modèle de rechercher des informations récentes sur le web "
            "en cours de réponse, s'il juge que c'est utile."
        ),
        tools={
            "web_search": (
                {
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
                _web_search_handler,
            )
        },
    ),
    "eu_ai_act": RemoteMCPServer(
        id="eu_ai_act",
        label="EU AI Act (Lawve)",
        description=(
            "Outils juridiques déterministes pour le Règlement européen sur "
            "l'IA (2024/1689) : classification des systèmes à haut risque "
            "(Annexe III), échéances de conformité, calcul des amendes (Art. 99), "
            "obligations par rôle (fournisseur/déployeur) et FAQ. Serveur "
            "tiers public, opéré par Lawve AI, sans authentification."
        ),
        url="https://mcp.lexbeam.com/mcp",
    ),
}
