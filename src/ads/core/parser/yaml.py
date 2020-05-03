from ads.utils.filewrapper import file2stream

import yaml, os

class Yaml(object):
    def __init__(self):
        pass

    @file2stream
    def parseYamlFile(self, file, path=None):
        content = yaml.load(file, Loader=yaml.SafeLoader)
        return [content, file]

if __name__ == "__main__":
    parser = Yaml();

    [content, file] = parser.parseYamlFile('test.yaml')
    print(content)
