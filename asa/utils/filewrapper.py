import os

def file2stream(path):
    def decorated(func):
        def convertFilename2Stream(self, *args, **kwargs):
            cPath = getattr(self, path)

            largs = list(args)

            if len(largs) > 2:
                filename = os.path.join(cPath, largs[1], largs[0])
            else:
                filename = os.path.join(cPath, largs[0])

            largs[0] = open(filename, 'r')
            args = tuple(largs)

            [content, file] = func(self, *args, **kwargs)

            file.close()
            return [content, filename]
        return convertFilename2Stream
    return decorated
