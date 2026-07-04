"""
Builds the shared tool set for a comparison from its enabled MCP server ids.

Built once per comparison (see `stream_comparison_messages`) and passed
identically to both bot positions, so both LLMs being compared always see the
exact same tools — never gated per-position.
"""

from dataclasses import dataclass
from typing import Awaitable, Callable

from backend.arena.legal_tools.mcp_servers import AVAILABLE_MCP_SERVERS


@dataclass(frozen=True)
class ToolSet:
    openai_tools: list[dict]
    handlers: dict[str, Callable[[dict], Awaitable[str]]]
    labels: dict[str, str]


def build_tool_set(enabled_mcp_servers: tuple[str, ...] | None) -> ToolSet | None:
    if not enabled_mcp_servers:
        return None

    tools = [
        AVAILABLE_MCP_SERVERS[server_id]
        for server_id in enabled_mcp_servers
        if server_id in AVAILABLE_MCP_SERVERS
    ]
    if not tools:
        return None

    return ToolSet(
        openai_tools=[tool.openai_schema for tool in tools],
        handlers={tool.openai_schema["function"]["name"]: tool.handler for tool in tools},
        labels={tool.openai_schema["function"]["name"]: tool.label for tool in tools},
    )
