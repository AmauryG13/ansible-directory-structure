from ads.__meta__ import __package__, __prog__
# from ads.__main__ import Builder
import argparse
import textwrap


def getMainDescription(text):
    return textwrap.dedent("""
--------------------------------------------------------------------------------
----------                 {}                ----------
--------------------------------------------------------------------------------

{}
""".format(__package__, text))


epilog = """
---------- {}
""".format(__package__)


class Cli(object):
    def __init__(self, *args, **kwargs):
        self.parser = argparse.ArgumentParser(
            prog=__prog__,
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description=getMainDescription('Create a set of resource in the directory structure'),
            epilog=epilog
        )

    def init(self):
        self._createSubparsers()

    def parse(self):
        self.args = self.parser.parse_args()
        print(self.args)

        args = self.__normalizeArgs()
        return args

    def _createSubparsers(self):
        self.subparsers = self.parser.add_subparsers(
            metavar='resource',
            dest='resource',
            help="specify the resource to create",
            required=True
        )

        self.subparser = {}

        self._parserRepo()
        self._parserConfig()
        self._parserInventory()
        self._parserPlaybook()
        self._parserRole()

    def _parserRepo(self):
        key = 'repo'

        self.subparser[key] = self.subparsers.add_parser(
            'repo',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='Create a new repository for Ansible',
            epilog=epilog
        )

        self.__setModeArgument(key)

        self.subparser[key].add_argument(
            '--path,-p',
            dest='path',
            metavar='PATH',
            help='specify the relative path from where the command is launched to create the repo',
        )

        self.subparser[key].add_argument(
            '--extra',
            dest='options',
            const='extra',
            help='specify if the repo should be created with its extra dependencies',
            action='append_const'
        )

    def _parserConfig(self):
        key = 'config'

        self.subparser[key] = self.subparsers.add_parser(
            'config',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='Create a new configuration',
            epilog=epilog
        )

        self.__setModeArgument(key)

    def _parserInventory(self):
        key = 'inventory'

        self.subparser[key] = self.subparsers.add_parser(
            'inventory',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='Create a new inventory',
            epilog=epilog
        )

        self.subparser[key].add_argument(
            'name',
            help='specify the name of the inventory'
        )

        self.__setModeArgument(key)

    def _parserPlaybook(self):
        key = 'playbook'
        self.subparser[key] = self.subparsers.add_parser(
            'playbook',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='Create a new playbok',
            epilog=epilog
        )

        self.subparser[key].add_argument(
            'name',
            help='specify the name of the playbook'
        )

        self.__setModeArgument(key)

    def _parserRole(self):
        key = 'role'
        self.subparser[key] = self.subparsers.add_parser(
            'role',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='Create a new role directory',
            epilog=epilog
        )

        self.subparser[key].add_argument(
            'name',
            help='specify the name of the role'
        )

        self.__setModeArgument(key)

        self.subparser[key].add_argument(
            '--files',
            dest='options',
            const='files',
            help='specify if the role should be created with the files directories',
            action='append_const'
        )

        self.subparser[key].add_argument(
            '--variables',
            dest='options',
            const='variables',
            help='specify if the role should be created with the variables directories',
            action='append_const'
        )

        self.subparser[key].add_argument(
            '--extra',
            dest='options',
            const='extra',
            help='specify if the role should be created with its extra dependencies',
            action='append_const'
        )

        self.subparser[key].add_argument(
            '--all',
            dest='options',
            const=['files', 'variables', 'extra'],
            help='specify if the role should be created with all its dependencies',
            action='store_const'
        )

    def __setModeArgument(self, key):
        help = 'specify the mode used to create the {}'.format(key)

        self.subparser[key].add_argument(
            '--mode', '-m',
            dest='mode',
            metavar='MODE',
            nargs=1,
            type=str,
            default='default',
            help=help,
            choices=('default', 'alternative')
        )

    def __normalizeArgs(self):
        keys = ['path', 'mode', 'config', 'name', 'options']
        args = vars(self.args)

        args['mode'] = args['mode'][0]

        for key in keys:
            if key not in args:
                args[key] = None

        return args
