from ads.utils.files import file2stream
import yaml


class Yaml(object):

    @file2stream
    def parseYamlFile(self, file, path=None):
        content = yaml.load(file, Loader=yaml.SafeLoader)
        return [content, file]
