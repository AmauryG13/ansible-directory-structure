import os, argparse

errorString = "argument {} : invalid choice '{}' (choose from '{}')"

class BootCommand(argparse.Action):
    validAction = ['create', 'delete']
    validResource = ['repo', 'inventory', 'roles']

    def __init__(self, option_strings, dest, nargs=1, **kwargs):
        super().__init__(option_strings, dest, nargs, **kwargs)

    def __call__(self, parser, namespace, values, option_string=None):
        value = values[self.nargs-1]
        setattr(namespace, self.dest, value)

        [action, resource] = value.split(':')

        if action not in self.validAction:
            parser.error(errorString.format('action', action, "', '".join(self.validAction)))

        setattr(namespace, "{}_action".format(self.dest), action)
        setattr(namespace, "{}_resource".format(self.dest), resource)
