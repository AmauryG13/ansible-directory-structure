from ads.core.filesystem.path import Path
import os


class Directory(Path):
    def __init__(self, path=None):
        super().__init__(path)

    def createDirectory(self, dir, path=None):
        cPath = self.getEntirePath(path)
        if isinstance(dir, list):
            for el in dir:
                dirpath = os.path.join(cPath, el)

                status = self._mkdir(dirpath)
        else:
            dirpath = os.path.join(cPath, dir)
            status = self._mkdir(dirpath)

        return status

    def deleteDirectory(self, dir, path=None):
        cPath = self.getEntirePath(path)
        if isinstance(dir, list):
            for el in dir:
                dirpath = os.path.join(cPath, el)
                status = self._rmdir(dirpath)
        else:
            dirpath = os.path.join(cPath, dir)
            status = self._rmdir(dirpath)

        return status

    def _mkdir(self, path):
        if not os.path.exists(path):
            os.mkdir(path)
            return True
        return False

    def _rmdir(self, path, recursive=False):
        content = os.listdir(path)

        if isinstance(content, list) and recursive:
            for el in content:
                dirpath = os.path.join(path, el)
                if os.path.isdir(dirpath):
                    self._rmdir(path, recurvise=True)
        else:
            os.rmdir(path)
            return True

        return False

    def isExistingDir(self, dir, path=None):
        cPath = self.getEntirePath(path)
        dirpath = os.path.join(cPath, dir)

        return os.path.exists(dirpath)
