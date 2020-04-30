from ads.core.filesystem import Manager
from asa.core.parser import YAML

import os

class AnsibleAssembler(Manager, YAML):
    def __init__(self, path, config):
        super().__init__(path)
        self.config = config

    def createRepo(self, name=None):
        self._createHook()

    def createInventory(self, name):
        key = 'inventories/'
        self._createHook(key, name)

    def createRole(self, name):
        key = 'roles/'
        self._createHook(key, name)

    def _createHook(self, key=None, name=None):
        content = self._getConfigContent(key)
        [directories, files] = self._detectContentNature(content)
        print(directories)
        print(files)

        if name is not None:
            self.createDirectory(name, key)

        idir = (key, "")[key is None] if name is None else os.path.join(key, name)
        self.createDirectory(directories, idir)

        if key is not None:
            for directory in directories:
                ifile = os.path.join(idir, directory)
                self.createFile("main.yaml", ifile)

            for f in files:
                ifile = key if name is None else os.path.join(key, name)
                self.createFile(f, ifile)

    def _getConfigContent(self, key):
        [config, file] = self.parseYAMLFile(self.config)
        tContent = config['toplevel']

        if key is not None:
            content = tContent[key]

            if isinstance(content, dict):
                keys = content.keys()
                return keys

            return content

        return tContent

    def _detectContentNature(self, content):
        directories = list()
        files = list()

        for c in content:
            strc = str(c)
            if strc.endswith("/"):
                directories.append(strc)
            else:
                files.append(strc)

        return [directories, files]
