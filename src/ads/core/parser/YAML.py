from ads.utils.filewrapper import file2stream

import yaml, os

class YAML(object):
    def __init__(self, path):
        pass

    @file2stream('path')
    def parseYAMLFile(self, file, path=None):
        content = yaml.load(file, Loader=yaml.SafeLoader)
        return [content, file]

if __name__ == "__main__":
    parser = YAMLParser('.');

    [content, file] = parser.readFile('test.yaml')
    print(content)
