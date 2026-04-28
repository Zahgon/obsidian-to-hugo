"""
Utilities to extract markdown marks from text and turn them into html marks.
"""

from typing import TypedDict, List
import re


Mark = TypedDict("Marks", {"md_mark": str, "text": str})


def get_md_marks(text: str) -> List[Mark]:
    """
    Get all markdown marks from the given text and return a list of them.
    Each list item is a dictionary with the following keys:
    - mark: the exact match
    - text: the extracted text
    """
    pass


def md_marks_to_html_marks(md_mark: Mark) -> str:
    """
    Convert the markdown mark into an html mark.
    """
    pass


def replace_md_marks(text: str) -> str:
    """
    Replace all markdown marks in the given text with html marks.
    """
    pass
