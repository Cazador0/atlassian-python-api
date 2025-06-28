#!/usr/bin/env python3
"""Generate a markdown file listing Jira and Bitbucket API methods."""

import inspect
from pathlib import Path
from atlassian import Jira, Bitbucket

OUTPUT = Path(__file__).resolve().parent / "api_map.md"


def is_public(name: str) -> bool:
    return not name.startswith("_")


def get_methods(cls):
    return sorted(name for name, member in inspect.getmembers(cls, inspect.isfunction) if is_public(name))


def main():
    jira_methods = get_methods(Jira)
    bitbucket_methods = get_methods(Bitbucket)
    with OUTPUT.open("w") as fh:
        fh.write("# API Feature Map\n\n")
        fh.write("## Jira\n")
        for m in jira_methods:
            fh.write(f"- `{m}`\n")
        fh.write("\n## Bitbucket\n")
        for m in bitbucket_methods:
            fh.write(f"- `{m}`\n")
    print(f"API map written to {OUTPUT}")


if __name__ == "__main__":
    main()
