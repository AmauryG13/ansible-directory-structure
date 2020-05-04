from ads.core.filesystem.directory import Directory
from ads.core.filesystem.file import File

class Filesystem(File, Directory):
    def __init__(self, path, *args, **kwargs):
        super().__init__(path, *args, **kwargs)

    def isFile(self, string):
        dotIdx = string.find('.')

        return (False, True)[dotIdx > -1]

if __name__ == "__main__":
    fs = Manager(".")

    print(fs._path)
    print(type(fs.path))

    status = fs.createDirectory("test")
    file = fs.createFile("main.yml", "test")


    #status = fs.deleteDirectory("test")
    #print(status)
