"""
Utilities to extract wiki links from text and turn them into hugo links.
"""

from typing import TypedDict, List
import re


WikiLink = TypedDict("WikiLink", {"wiki_link": str, "link": str, "text": str})


def get_wiki_links(text: str) -> List[WikiLink]:
    """
    Get all wiki links from the given text and return a list of them.
    Each list item is a dictionary with the following keys:
    - wiki_link: the exact match
    - link: the extracted link
    - text: the possible extracted text
    """
    pass


def wiki_link_to_hugo_link(wiki_link: WikiLink) -> str:
    """
    Convert the wiki link into a hugo link.
    """
    pass


def replace_wiki_links(text: str) -> str:
    """
    Replace all wiki links in the given text with hugo links.
    """
    pass
