from asa.Core.FileSystem.Path import Path
import os

class File(Path):
    def __init__(self, path=None):
        super().__init__(path)

    def createFile(self, filename, path=None):
        cPath = self.getEntirePath(path)
        filepath = os.path.join(cPath, filename)
        file = open(filepath, 'x')
        return file

    def deleteFile(self, filename, path=None):
        cPath = self.getEntirePath(path)
        filepath = os.path.join(cPath, filename)

        if os.path.exists(filepath):
            os.remove(filepath)
            return True

        return False

    def writeFile(self, filename, content, appends=True, path=None):
        Path = self.getEntirePath(path)
        filepath = os.path.join(cPath, filename)

        if appends == True:
            mode = 'a+'
        else:
            mode = 'w+'

        file = open(filepath, mode)
        file.write(content)

        return True

    def readFile(self, filename, path=None):
        Path = self.getEntirePath(path)
        filepath = os.path.join(cPath, filename)
        file = open(filepath, 'r')

        return file.read()

if __name__ == '__main__':
    file = File('.')
    print(dir(file))
    print(file.path)
