# Upstream Source

- Repository: `https://github.com/JackKuo666/Google-Scholar-MCP-Server`
- Imported commit: `738d60a4d69464731e7c5b3a61767c06ff2cec0d`
- Imported on: `2026-03-09`

## Vendored Files

- `scripts/google_scholar_server.py`
- `scripts/google_scholar_web_search.py`
- `scripts/requirements.txt` derived from upstream requirements

## Notes

- Upstream `README.md` describes the project as MIT-licensed, but no standalone license file was present in the imported snapshot.
- This skill packages the MCP server inside the skill directory so the skill remains portable when copied into `.codex/skills`, `.claude/skills`, or similar directories.

## Refresh Workflow

1. Clone or fetch the upstream repository at the desired ref.
2. Replace `scripts/google_scholar_server.py` and `scripts/google_scholar_web_search.py` with the upstream versions.
3. Update `scripts/requirements.txt` if upstream dependencies changed.
4. Update the pinned commit in this file.
5. Validate syntax with:

```bash
python -m py_compile scripts/run_server.py scripts/google_scholar_server.py scripts/google_scholar_web_search.py
```
