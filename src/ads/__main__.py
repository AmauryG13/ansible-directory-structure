from ads.core.config.manager import Config
from ads.core.filesystem.manager import Filesystem
from ads.core.parser.manager import Parser
import os


class Builder(Config, Filesystem, Parser):
    def __init__(self, mode, path, config):
        super().__init__(path=path, config=config)
        self.mode = mode
        self.actions = []
        self.readConfig()

    def createRepo(self, name=None):
        content = self._getConfigContent(None)

        self._addNewAction('directory', 'roles')
        self._executeActions()

        for key in content[:-1]:
            getattr(self, 'create' + key.capitalize())()

    def createConfig(self):
        key = 'config'
        self._createHook(key, None)

    def createInventory(self, name=None):
        key = 'inventory'

        self._detectPreviousConfig(key)

        if name is not None and self.isFile(name):
            if self.mode == "default":
                self.config[key][self.mode]['path'] = './' + name
                name = None
            elif self.mode == 'alternative':
                name = name[0:name.find('.')]
        else:
            if self.mode == 'alternative':
                self._addNewAction('directory', 'inventories')
                self._executeActions()
                return

        self._createHook(key, name)

    def createPlaybook(self, name=None):
        key = 'playbook'

        self._detectPreviousConfig(key)

        if name is not None and self.isFile(name):
            if self.mode == "default":
                self.config[key][self.mode]['path'] = './' + name
                name = None
            elif self.mode == "alternative":
                name = self.config[key][self.mode]['content'] = [name]
                name = None

        self._createHook(key, name)

    def createRole(self, name):
        key = 'role'
        self._createHook(key, name)

    def _createHook(self, key=None, name=None):
        entry = self.config[key]
        mode = ('default', self.mode)[self.mode in entry]
        entry = entry[mode]

        if entry is None:
            return

        self._createActions(name, entry)
        self._executeActions()

    def _getConfigContent(self, key):
        if key is None:
            return list(self.config.keys())

        return self.config[key]

    def _createActions(self, path, entry):
        actionDriver = entry['driver']
        actionPath = entry['path']

        if path is not None:
            self._addNewAction('directory', actionPath)
            actionPath = self.__pathJoint(actionPath, path)

        self._addNewAction(actionDriver, actionPath)

        if 'content' in entry:
            content = entry['content']
            self._handleContent(actionPath, content)

    def _executeActions(self,):
        print(self.actions)
        for action in self.actions:
            func = 'create' + action['driver'].capitalize()
            getattr(self, func)(action['path'])

        self.actions = []
        print(self.actions)

    def _addNewAction(self, driver, path):
        self.actions.append(
            self._createNewAction(driver, path)
        )

    def _createNewAction(self, driver, path):
        return {'driver': driver, 'path': path}

    def _handleContent(self, path, content):
        if isinstance(content, list):
            for element in content:
                actionDriver = ('directory', 'file')[self.isFile(element)]
                actionPath = self.__pathJoint(path, element)
                self._addNewAction(actionDriver, actionPath)
        elif isinstance(content, dict):
            for key in content:
                actionDriver = ('directory', 'file')[self.isFile(key)]
                actionPath = self.__pathJoint(path, key)
                self._addNewAction(actionDriver, actionPath)

                if isinstance(content[key], list):
                    self._handleContent(actionPath, content[key])

    def __pathJoint(self, p1, p2):
        if self.isFile(p1):
            return p2

        return os.path.join(p1, p2)

    def _detectPreviousConfig(self, key):
        config = self.config[key]
        params = config['alternative']

        status = self.isExistingDir(params['path'])

        if status:
            self.mode = 'alternative'
        else:
            self.mode = 'default'
