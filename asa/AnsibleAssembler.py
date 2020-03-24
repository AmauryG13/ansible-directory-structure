from asa.Core.FileSystem.Manager import Manager
from asa.Core.Parser.YAML import YAML

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

        if name is not None:
            self.createDirectory(name, key)

        idir = self.path if name is None else os.path.join(self.path, key, name)
        self.createDirectory(directories, idir)

    def _getConfigContent(self, key):
        [config, file] = self.parseYAMLFile(self.config)
        tContent = config['toplevel']

        if key is not None:
            content = tContent[key]
            keys = content.keys()
            return keys

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
