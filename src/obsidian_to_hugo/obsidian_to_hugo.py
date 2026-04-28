"""
Utilities to process obsidian notes and convert them to hugo ready content files.
"""

import os
from shutil import rmtree, copytree, ignore_patterns
from .wiki_links_processor import replace_wiki_links
from .md_mark_processor import replace_md_marks


class ObsidianToHugo:
    """
    Process the obsidian vault and convert it to hugo ready content.
    """

    def __init__(
        self,
        obsidian_vault_dir: str,
        hugo_content_dir: str,
        processors: list = None,
        filters: list = None,
    ) -> None:
        self.obsidian_vault_dir = obsidian_vault_dir
        self.hugo_content_dir = hugo_content_dir
        self.processors = [replace_wiki_links, replace_md_marks]
        self.filters = []
        if processors:
            self.processors.extend(processors)
        if filters:
            self.filters.extend(filters)

    def run(self) -> None:
        """
        Delete the hugo content directory and copy the obsidian vault to the
        hugo content directory, then process the content so that the wiki links
        are replaced with the hugo links.
        """
        pass

    def clear_hugo_content_dir(self) -> None:
        """
        Delete the whole content directory.
        NOTE: The folder itself gets deleted and recreated.
        """
        pass

    def copy_obsidian_vault_to_hugo_content_dir(self) -> None:
        """
        Copy all files and directories from the obsidian vault to the hugo content directory.
        """
        pass

    def process_content(self) -> None:
        """
        Looping through all files in the hugo content directory and replace the
        wiki links of each matching file.
        """
        pass
