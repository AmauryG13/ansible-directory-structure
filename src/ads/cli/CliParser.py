from ads.AnsibleAssembler import AnsibleAssembler

class CliParser(AnsibleAssembler):
    def __init__(self, path, config, action, resource, **args):
        super().__init__(path, config)
        self.action = action
        self.resource = resource
        self.args = args

    def runCommand(self):
        methodName = ''.join([self.action, self.resource.capitalize()])
        getattr(self, methodName)(name=self.args["name"])
