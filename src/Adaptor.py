import requests

class Mapper(object):
    @staticmethod
    def Transform(source, target, lookup):
        sourceKeys = source.keys()
        lookupKeys = lookup.keys()

        for k in mapping:
            targetValue = None
            print(k, lookup)
            if k in lookupKeys and lookup[k] in sourceKeys:
                targetValue = source[lookup[k]]
            target[k] = targetValue

class Adaptor(object):
    def __init__(self):
        pass

    def GetMetadata(self):
        pass

    def GetData(self):
        pass

    def Transform(self, source, destination, mapping):
        print("Applying transformations")
        Mapper.Transform(source, destination, mapping)

class AdaptorImpl(Adaptor):
    def __init__(self):
        self.ProviderId = 0
        self.ProviderUrl = "http://localhost:7001/provider/{}/metadata".format(self.ProviderId)

    def GetMetadata(self):
        print("Adaptor implementation - GetMetadata", self.ProviderUrl)
        r = requests.get(self.ProviderUrl)
        return r.json()

    def GetMappings(self):
        return {'title': 'name'}

    # pull internal data and transform
    def GetData(self):
        print("Adaptor implementation - GetData")
        # Read from internal/external data providers
        data = {'name': "some name", 'b': 2}
        lookup = self.GetMappings()
        target = data.copy()
        self.Transform(data, target, lookup)
        print(target)
        return target

class Merchant(object):
    def GetProduct(self):
        print("Merchant:", self.Name, "GetProduct")
        pass

    def __init__(self, adaptorImpl):
        self.adaptorImpl = adaptorImpl
        self.Name = "Merchant1"
        pass

# adaptor = AdaptorImpl()
# adaptor.GetMetadata()

# source = {'a':12,'b':2}
# target = {'x':1, 'y':2, 'z':4}
# mapping = {'y': 'a'}
# print(target)
# Mapper.Transform(source, target, mapping)
# print(target)

source = {'a':12,'b':2}
target = {'x':1, 'y':2, 'z':4}
mapping = {'title': 'name'}
adaptor = AdaptorImpl()
adaptor.GetData()