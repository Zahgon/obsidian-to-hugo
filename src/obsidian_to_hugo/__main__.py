"""
Obsidian to Hugo CLI
"""

import argparse
import os
from .obsidian_to_hugo import ObsidianToHugo
from obsidian_to_hugo import __version__


parser = argparse.ArgumentParser()

parser.add_argument(
    "--version",
    "-v",
    action="version",
    version=f"obsidian-to-hugo {__version__}",
    help="Show the version and exit.",
)

parser.add_argument(
    "--hugo-content-dir",
    help="Directory of your Hugo content directory, the obsidian notes should be processed into.",
    type=str,
)

parser.add_argument(
    "--obsidian-vault-dir",
    help="Directory of the Obsidian vault, the notes should be processed from.",
    type=str,
)


def main() -> None:
    """
    Main entry point of the CLI.
    """
    pass


if __name__ == "__main__":
    main()
