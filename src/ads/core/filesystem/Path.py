import os

class Path(object):
    def __init__(self, path=None):
        if path is None:
            self._path = os.getcwd()
        else:
            self._path = path

        self.isAbsolute = os.path.isabs(self._path)
        self.isRelative = (True, False)[self.isAbsolute]

    def getEntirePath(self, path=None):
        if path is not None:
            npath = os.path.join(self._path, path)
            return npath

        return self._path

    @property
    def path(self):
        return self._path

    @path.setter
    def path(self, value):
        self._path = value
