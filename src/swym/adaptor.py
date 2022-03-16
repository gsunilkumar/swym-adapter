from mapper import Mapper

class Adaptor(object):
    def __init__(self):
        pass

    def GetMetadata(self):
        pass

    def GetData(self):
        pass

    def Transform(self, source, destination, mapping):
        print("Applying transformations:", mapping)
        Mapper.Transform(source, destination, mapping)

# source = {'name':'some name','b':2}
# target = {'x':1, 'y':2, 'z':4}
# mapping = {'title': 'name'}
# print(target)
# Mapper.Transform(source, target, mapping)
# print(target)