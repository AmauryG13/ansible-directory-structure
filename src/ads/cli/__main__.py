#!/usr/bin/env python3
from ads.cli import Cli
from ads.__main__ import Builder


def getArgs(method, args):
    output = {}
    keys = {
        'init': ['path', 'mode', 'config'],
        'hook': ['name']
    }

    for key in keys[method]:
        if key in args:
            output[key] = args[key]

    return output


cli = Cli()
cli.init()

args = cli.parse()
print(args)

ads = Builder(**getArgs('init', args))

funcName = 'create{}'.format(args['resource'].capitalize())
getattr(ads, funcName)(**getArgs('hook', args))
