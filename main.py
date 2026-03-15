import os

from fastmcp.server import create_proxy

mcp = create_proxy(
    "https://f1-card-game-mcp-server.onrender.com/mcp",
    name="F1 Card Game MCP Proxy",
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8000))
    mcp.run()
