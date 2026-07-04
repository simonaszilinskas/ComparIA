"""
Builds the shared tool set for a comparison from its enabled MCP server ids.

Built once per comparison (see `stream_comparison_messages`) and passed
identically to both bot positions, so both LLMs being compared always see the
exact same tools — never gated per-position.

Remote MCP servers are connected to once per comparison (not per-turn or
per-position) and kept open for the lifetime of the streaming response, via
the returned async context manager.
"""

import logging
from contextlib import AsyncExitStack, asynccontextmanager
from dataclasses import dataclass
from typing import Awaitable, Callable

from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

from backend.arena.legal_tools.mcp_servers import (
    AVAILABLE_MCP_SERVERS,
    LocalMCPServer,
    RemoteMCPServer,
)

logger = logging.getLogger("languia")


@dataclass
class ToolSet:
    openai_tools: list[dict]
    handlers: dict[str, Callable[[dict], Awaitable[str]]]
    labels: dict[str, str]


def _make_remote_handler(
    session: ClientSession, tool_name: str
) -> Callable[[dict], Awaitable[str]]:
    async def handler(arguments: dict) -> str:
        result = await session.call_tool(tool_name, arguments)
        parts = [block.text for block in result.content if hasattr(block, "text")]
        return "\n".join(parts) if parts else "Aucun résultat."

    return handler


@asynccontextmanager
async def mcp_tools_for(enabled_mcp_servers: tuple[str, ...] | None):
    """
    Yields a ToolSet (or None if no tools ended up available) for the given
    enabled server ids, keeping any remote MCP sessions open until the
    context exits.
    """
    if not enabled_mcp_servers:
        yield None
        return

    openai_tools: list[dict] = []
    handlers: dict[str, Callable[[dict], Awaitable[str]]] = {}
    labels: dict[str, str] = {}

    async with AsyncExitStack() as stack:
        for server_id in enabled_mcp_servers:
            server = AVAILABLE_MCP_SERVERS.get(server_id)
            if server is None:
                continue

            if isinstance(server, LocalMCPServer):
                for name, (schema, handler) in server.tools.items():
                    openai_tools.append({"type": "function", "function": schema})
                    handlers[name] = handler
                    labels[name] = server.label
                continue

            assert isinstance(server, RemoteMCPServer)
            try:
                read, write, _ = await stack.enter_async_context(
                    streamablehttp_client(server.url)
                )
                session = await stack.enter_async_context(ClientSession(read, write))
                await session.initialize()
                tools = await session.list_tools()
            except Exception:
                # Fail open: an unreachable third-party MCP server shouldn't
                # break the comparison, it's just unavailable for this turn.
                logger.warning(f"mcp_server_unreachable: {server.id}", exc_info=True)
                continue

            for tool in tools.tools:
                openai_tools.append(
                    {
                        "type": "function",
                        "function": {
                            "name": tool.name,
                            "description": tool.description or "",
                            "parameters": tool.inputSchema,
                        },
                    }
                )
                handlers[tool.name] = _make_remote_handler(session, tool.name)
                labels[tool.name] = server.label

        if not openai_tools:
            yield None
            return

        yield ToolSet(openai_tools=openai_tools, handlers=handlers, labels=labels)
