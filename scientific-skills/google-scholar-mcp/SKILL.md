---
name: google-scholar-mcp
description: Run a local Google Scholar MCP server from this skill for MCP-enabled clients such as Claude Desktop, Cursor, and similar tools. Use when the user wants Google Scholar exposed as MCP tools instead of one-off scripts, or when integrating Google Scholar paper search and author lookup into an MCP workflow.
allowed-tools: Read Write Edit Bash
license: Upstream README states MIT
metadata:
    skill-author: Curated integration
---

# Google Scholar MCP

## When to Use This Skill

Use this skill when you need:
- A local MCP server that exposes Google Scholar search to an MCP-capable client
- Keyword search, advanced search, or author lookup through MCP tools
- A reusable Google Scholar server inside this repository's skill layout

Do not use this skill for simple citation cleanup or BibTeX formatting alone. For those tasks, use `citation-management`.

## Bundled Components

- `scripts/google_scholar_server.py`: vendored upstream MCP server
- `scripts/google_scholar_web_search.py`: vendored upstream Google Scholar search helper
- `scripts/run_server.py`: stable launcher for this packaged skill
- `scripts/requirements.txt`: Python dependencies for the vendored server
- `references/upstream.md`: upstream source, pinned commit, and refresh notes

## Setup

Install the dependencies:

```bash
python -m pip install -r scripts/requirements.txt
```

Start the server from the skill directory:

```bash
python scripts/run_server.py
```

If you manage Python environments per client, replace `python` with the exact interpreter path for that environment.

## MCP Client Configuration

Point the client to this skill's launcher script.

Example JSON:

```json
{
  "mcpServers": {
    "google-scholar": {
      "command": "python",
      "args": [
        "/absolute/path/to/google-scholar-mcp/scripts/run_server.py"
      ]
    }
  }
}
```

Windows example:

```json
{
  "mcpServers": {
    "google-scholar": {
      "command": "C:\\Path\\To\\python.exe",
      "args": [
        "C:\\Path\\To\\google-scholar-mcp\\scripts\\run_server.py"
      ]
    }
  }
}
```

## MCP Tools Exposed

- `search_google_scholar_key_words`
- `search_google_scholar_advanced`
- `get_author_info`

## Workflow Guidance

- Use this skill when the user explicitly wants MCP integration or an MCP config snippet.
- Use `citation-management` after search if you need BibTeX generation, metadata cleanup, or citation validation.
- Prefer `pubmed-database` or `research-lookup` as fallback if Google Scholar blocks automated access.
- Respect Google Scholar rate limits and terms of service.
