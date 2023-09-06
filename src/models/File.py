import os
import glob
import pathlib
import frontmatter
from random import randint


current_folder = pathlib.Path(__file__).parent.resolve()


class File:
    def __init__(self, assigned_file=None):
        self._file = assigned_file if assigned_file else self._get_file()

    def _get_root_folder(self):
        return pathlib.Path(__file__).parent.parent.parent.resolve()

    def _get_files_list(self):
        md_file_path = os.path.join(current_folder, '..', '..', '01. RawCards', '*.md')
        return glob.glob(md_file_path)

    def _get_file(self):
        files = self._get_files_list()
        file = files[randint(0, len(files) - 1)]
        post = None
        with open(file, 'r') as f:
            post = frontmatter.load(f)
        # TODO: exception handling
        return post

    def _get_metadata(self):
        return self._file.metadata

    def get_tags(self):
        return self._get_metadata().get('tags', [])

    def get_source(self):
        return self._get_metadata().get('source', '')

    def get_content(self):
        return self._file.content
