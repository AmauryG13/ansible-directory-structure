from ads.core.filesystem.Directory import Directory
from ads.core.filesystem.File import File

class Manager(File, Directory):
    def __init__(self, path=None):
        super().__init__(path)


if __name__ == "__main__":
    fs = Manager(".")

    print(fs._path)
    print(type(fs.path))

    status = fs.createDirectory("test")
    file = fs.createFile("main.yml", "test")


    #status = fs.deleteDirectory("test")
    #print(status)
