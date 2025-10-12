"""MCP Client setup and management for LangGraph ReAct Agent."""

import logging
import json
from typing import Any, Callable, List, cast

from langchain_mcp_adapters.client import (  # type: ignore[import-untyped]
    MultiServerMCPClient,
)

logger = logging.getLogger(__name__)

# Global MCP client and tools cache
_mcp_client: MultiServerMCPClient | None = None
_mcp_tools_cache: List[Callable[..., Any]] = []
_mcp_server_configs: str | None = None


async def get_mcp_client(
    server_configs: str,
) -> MultiServerMCPClient | None:
    """Get or initialize the global MCP client with given server configurations."""
    global _mcp_client
    global _mcp_server_configs

    if _mcp_client is None or _mcp_server_configs != server_configs:
        try:
            config = json.loads(server_configs)
        except Exception as e:
            logger.error("Invalid JSON for server_configs: %s", e)
            return None
        
        try:
            _mcp_client = MultiServerMCPClient(
                config
            )  # pyright: ignore[reportArgumentType]
            _mcp_server_configs = server_configs
        except Exception as e:
            logger.error("Failed to initialize MCP client: %s", e)
            return None
    return _mcp_client


async def get_mcp_tools(
    server_configs: str,
) -> List[Callable[..., Any]]:
    """Get MCP tools for a specific server, initializing client if needed."""
    global _mcp_tools_cache

    # Return cached tools if available
    if _mcp_tools_cache:
        return _mcp_tools_cache

    try:
        client = await get_mcp_client(server_configs)
        if client is None:
            return []

        # Get all tools and filter by server (if tools have server metadata)
        all_tools = await client.get_tools()
        tools = cast(List[Callable[..., Any]], all_tools)

        _mcp_tools_cache = tools
        logger.info(f"Loaded {len(tools)} tools from MCP server.")
        for idx, tool in enumerate(tools):
            logger.info(
                f"Tool {idx+1}: {getattr(tool, 'name', 'Unknown')}, {getattr(tool, 'description', 'No description')}"
            )
        return tools
    except Exception as e:
        logger.warning("Failed to load tools from MCP server: %s", e)
        _mcp_tools_cache = []
        return []


def clear_mcp_cache() -> None:
    """Clear the MCP client and tools cache (useful for testing)."""
    global _mcp_client, _mcp_tools_cache
    _mcp_client = None
    _mcp_tools_cache = []
