import os
from ads.core.parser.yaml import Yaml

class Config(Yaml):
    _defaultPath = os.path.join(os.path.dirname(__file__), '../../../../config')
    _configKeys = ['layout', 'inventory', 'playbook', 'role', 'config'];

    def __init__(self, config, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configPath = config

    def readDefaultConfig(self):
        content = self._readConfigFiles(self._configKeys, self._defaultPath)

        self.config = content['layout']['default']
        for inKey in self.config:
            self.config[inKey] = content[inKey]

    def readUsertConfig(self):
        files = self._scanForConfigFile(self.configPath)
        keys = self._getKeysForFiles(files)

        content = self._readConfigFiles(keys, self.configPath)
        return content

    def mergeConfigContent(self, content):
        for userKey in content:
            self.config[userKey] = content[userKey]

    def readConfig(self):
        self.readDefaultConfig()

        if self.configPath is not None:
            userConfig = self.readUsertConfig()
            self.mergeConfigContent(userConfig)

    def _readConfigFiles(self, keys, path):
        content = {}
        for key in keys:
            [content[key], file] = self.parseYamlFile(
                self._getConfigFile(key),
                self._defaultPath)

        return content

    def _scanForConfigFile(self, path=None):
        if path is None:
            path = self.defaultPath

        return os.listdir(path)

    def _getConfigFile(self, filename):
        configFile = filename + '.yaml'
        return configFile

    def _getKeysFromFiles(self, files):
        keys = []
        for file in files:
            keys.append(file[0:file.find('.')])

        return keys

if __name__ == '__main__':
    import pprint

    config = Manager()
    config.readConfig()

    pprint.pprint(config.config)
