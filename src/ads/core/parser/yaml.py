from ads.utils.files import file2stream

import yaml, os

class Yaml(object):

    @file2stream
    def parseYamlFile(self, file, path=None):
        content = yaml.load(file, Loader=yaml.SafeLoader)
        return [content, file]

if __name__ == "__main__":
    parser = Yaml();

    [content, file] = parser.parseYamlFile('test.yaml')
    print(content)
