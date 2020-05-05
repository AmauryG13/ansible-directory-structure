from ads.core.filesystem.directory import Directory
from ads.core.filesystem.file import File


class Filesystem(File, Directory):
    def __init__(self, path, *args, **kwargs):
        super().__init__(path, *args, **kwargs)

    def isFile(self, string):
        dotIdx = string.find('.')

        return (False, True)[dotIdx > -1]
