#!/usr/bin/env python3
"""Create a notebook folder for a new client."""
from pathlib import Path
import shutil
import sys

ROOT = Path(__file__).resolve().parent
TEMPLATE = ROOT / "templates" / "client_template.ipynb"
NOTEBOOK_ROOT = ROOT / "notebooks"


def main():
    if len(sys.argv) != 2:
        print("Usage: init_client.py <client_name>")
        return
    name = sys.argv[1]
    target_dir = NOTEBOOK_ROOT / name
    target_dir.mkdir(parents=True, exist_ok=True)
    shutil.copy(TEMPLATE, target_dir / f"{name}.ipynb")
    print(f"Created notebook {target_dir / f'{name}.ipynb'}")


if __name__ == "__main__":
    main()
