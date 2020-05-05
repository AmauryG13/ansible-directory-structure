from ads.core.filesystem.path import Path
import os


class File(Path):
    def __init__(self, path=None):
        super().__init__(path)

    def createFile(self, filename, path=None):
        cPath = self.getEntirePath(path)
        filepath = os.path.join(cPath, filename)

        if not os.path.exists(filepath):
            file = open(filepath, 'x')
            return file

        return

    def deleteFile(self, filename, path=None):
        cPath = self.getEntirePath(path)
        filepath = os.path.join(cPath, filename)

        if os.path.exists(filepath):
            os.remove(filepath)
            return True

        return False

    def writeFile(self, filename, content, appends=True, path=None):
        cPath = self.getEntirePath(path)
        filepath = os.path.join(cPath, filename)

        if appends:
            mode = 'a+'
        else:
            mode = 'w+'

        file = open(filepath, mode)
        file.write(content)

        return True

    def readFile(self, filename, path=None):
        cPath = self.getEntirePath(path)
        filepath = os.path.join(cPath, filename)
        file = open(filepath, 'r')

        return file.read()
