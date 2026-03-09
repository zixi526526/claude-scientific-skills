#!/usr/bin/env python3
"""Launch the vendored Google Scholar MCP server from this skill."""

from pathlib import Path
import runpy
import sys


def main() -> None:
    scripts_dir = Path(__file__).resolve().parent
    sys.path.insert(0, str(scripts_dir))
    runpy.run_path(str(scripts_dir / "google_scholar_server.py"), run_name="__main__")


if __name__ == "__main__":
    main()
