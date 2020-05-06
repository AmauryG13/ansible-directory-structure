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
        args = self.parser.parse_args()
        print(args)

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
        self.subparser['repo'] = self.subparsers.add_parser(
            'repo',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='Create a new repository for Ansible',
            epilog=epilog
        )

        self.subparser['repo'].add_argument(
            '--mode', '-m',
            dest='mode',
            metavar='MODE',
            nargs=1,
            help='specify the mode used to create the resource',
            choices=('default', 'alternative')
        )

        self.subparser['repo'].add_argument(
            '--path,-p',
            dest='path',
            metavar='PATH',
            help='specify the relative path from where the command is launched to create the resource',
        )

        self.subparser['repo'].add_argument(
            '--extra',
            help='specify if the repositoty should be created with its extra dependencies',
            action='store_true'
        )

    def _parserConfig(self):
        self.subparser['config'] = self.subparsers.add_parser(
            'config',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='Create a new configuration',
            epilog=epilog
        )

        self.subparser['config'].add_argument(
            '--mode,-m',
            dest='mode',
            metavar='MODE',
            help='specify the mode used to create the resource',
            choices=('default', 'alternative')
        )

    def _parserInventory(self):
        self.subparser['inventory'] = self.subparsers.add_parser(
            'inventory',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='Create a new inventory',
            epilog=epilog
        )

        self.subparser['inventory'].add_argument(
            'name',
            help='specify the name of the inventory'
        )

        self.subparser['inventory'].add_argument(
            '--mode,-m',
            metavar='MODE',
            help='specify the mode used to create the resource',
            choices=('default', 'alternative')
        )

    def _parserPlaybook(self):
        self.subparser['playbook'] = self.subparsers.add_parser(
            'playbook',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='Create a new playbok',
            epilog=epilog
        )

        self.subparser['playbook'].add_argument(
            'name',
            help='specify the name of the playbook'
        )

        self.subparser['playbook'].add_argument(
            '--mode,-m',
            metavar='MODE',
            help='specify the mode used to create the resource',
            choices=('default', 'alternative')
        )

    def _parserRole(self):
        self.subparser['role'] = self.subparsers.add_parser(
            'role',
            formatter_class=argparse.RawDescriptionHelpFormatter,
            description='Create a new role directory',
            epilog=epilog
        )

        self.subparser['role'].add_argument(
            'name',
            help='specify the name of the role'
        )

        self.subparser['role'].add_argument(
            '--mode,-m',
            metavar='MODE',
            help='specify the mode used to create the resource',
            choices=('default', 'alternative')
        )

        self.subparser['role'].add_argument(
            '--files',
            help='specify if the role should be created with the files directories',
            action='store_true'
        )

        self.subparser['role'].add_argument(
            '--variables',
            help='specify if the role should be created with the variables directories',
            action='store_true'
        )

        self.subparser['role'].add_argument(
            '--extra',
            help='specify if the role should be created with its extra dependencies',
            action='store_true'
        )

        self.subparser['role'].add_argument(
            '--all',
            help='specify if the role should be created with all its dependencies',
            action='store_true'
        )
