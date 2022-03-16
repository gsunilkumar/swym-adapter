import requests

class Adaptor(object):
    def __init__(self):
        pass

    def GetMetadata(self):
        pass

    def GetData(self):
        pass

    def Transform(self, source, destination, mapping):
        print("Applying transformations")

class AdaptorImpl(Adaptor):
    def __init__(self):
        self.ProviderId = 0
        self.ProviderUrl = "http://localhost:7001/provider/{}/metadata".format(self.ProviderId)

    def GetMetadata(self):
        print("Adaptor implementation - GetMetadata", self.ProviderUrl)
        r = requests.get(self.ProviderUrl)
        return r.json()

    # pull internal data and transform
    def GetData(self):
        print("Adaptor implementation - GetData")
        # Read from internal/external data providers
        data = {'a':1, 'b': 2}
        self.Transform(data, data, data)
        return data

class Merchant(object):
    def GetProduct(self):
        print("Merchant:", self.Name, "GetProduct")
        pass

    def __init__(self, adaptorImpl):
        self.adaptorImpl = adaptorImpl
        self.Name = "Merchant1"
        pass

adaptor = AdaptorImpl()
adaptor.GetMetadata()
adaptor.GetData()