# F1 Card Game — MCP Proxy Server

A lightweight proxy that forwards MCP requests to the hosted [F1 Card Game MCP Server](https://github.com/naman/F1-Card-Game-MCP-Server), so you can play without running the backend locally.

No database, no `.env` secrets, no setup — just add it to your MCP client and start playing.

---

## Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) — install with `pip install uv`

---

## Claude Desktop Setup

**1. Clone this repo**

```bash
git clone https://github.com/naman/F1-Card-Game-Proxy-MCP-Server.git
```

**2. Add to your Claude Desktop config**

Open your config file:

- **macOS**: `~/Library/Application Support/Claude/claude_desktop_config.json`
- **Windows**: `%APPDATA%\Claude\claude_desktop_config.json`

Add the following entry under `mcpServers`:

```json
{
  "mcpServers": {
    "F1 Card Game MCP Proxy": {
      "command": "<path to uv>",
      "args": [
        "run",
        "--with",
        "fastmcp",
        "fastmcp",
        "run",
        "<path to repo>/main.py"
      ]
    }
  }
}
```

> Replace `<path to uv>` with the output of `which uv` (e.g. `/Users/you/.pyenv/shims/uv`) and `<path to repo>` with the absolute path to the cloned repository.

**3. Restart Claude Desktop.** The F1 Card Game tools should now appear.

---

## How It Works

This proxy uses [FastMCP](https://github.com/jlowin/fastmcp)'s `create_proxy` to relay all tool calls, resources, and prompts to the remote server:

```
Claude Desktop ⟷ (stdio) ⟷ Proxy ⟷ (http) ⟷ Hosted MCP Server
```

The proxy doesn't contain any game logic — it simply passes requests through. All game state, driver data, and leaderboard live on the hosted backend.

---

## Available Tools

Once connected, the following 9 MCP tools are available through the proxy:

| Tool | Description |
|------|-------------|
| `welcome` | Register or log in with a name and password |
| `update_password` | Change your account password |
| `logout` | End the current session |
| `ensure_ai_user` | Create the AI opponent if missing |
| `start_game` | Start a new game — deals 5 driver cards and picks 5 tracks |
| `play_card` | Play a driver card for the current round |
| `get_hand` | View your remaining cards |
| `get_game_status` | Check current round, scores, and past results |
| `get_leaderboard` | View top players ranked by total points |

## Available Resources

| URI | Description |
|-----|-------------|
| `f1cardgame://rules` | Complete rules and scoring guide |
| `f1cardgame://skills` | Definitions of the 6 driver skills |
| `f1cardgame://drivers` | Full driver catalog with skills and teams |
| `f1cardgame://tracks` | Full track catalog with circuit types |

---

## Game Overview

Two players (you + AI) each receive 5 random F1 driver cards. Over 5 rounds, tracks are revealed one-by-one, and both players play a card. Each driver's average skill score is multiplied by their track affinity to determine the round winner. After all 5 rounds, the overall winner earns leaderboard points.

**Power formula:**

```
power = average(pace, racecraft, awareness, experience, wet_weather, tire_management) × track_multiplier
```

---

## Links

- [F1 Card Game MCP Proxy Server](https://github.com/naman/F1-Card-Game-Proxy-MCP-Server) — this repo
- [F1 Card Game MCP Server](https://github.com/naman/F1-Card-Game-MCP-Server) — the full backend with game logic, database, and data seeding
