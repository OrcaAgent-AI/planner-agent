"""MCP server configurations."""
from typing import Any, Dict

MCP_SERVERS: Dict[str, Any] = {
    "deepwiki": {
        "url": "https://mcp.deepwiki.com/mcp",
        "transport": "streamable_http",
    },
}