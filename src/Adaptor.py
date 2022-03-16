import requests
from swym.adaptor import Adaptor

class AdaptorImpl(Adaptor):
    def __init__(self, id):
        self.ProviderId = id
        self.ProviderUrl = "http://localhost:7001/provider/{}/metadata".format(self.ProviderId)
        self.ProductUrl = "http://localhost:7002/datafeed/{}/product".format(self.ProviderId)
    def GetMetadata(self):
        print("Adaptor implementation - GetMetadata", self.ProviderUrl)
        r = requests.get(self.ProviderUrl)
        return r.json()

    def GetMappings(self):
        return {'title': 'name'}

    # pull internal data and transform
    def GetData(self):
        print("Adaptor implementation - GetData", self.ProductUrl)

        r = requests.get(self.ProductUrl)
        data = r.json()
        print('Original data: ', data)

        lookup = self.GetMappings()
        target = data.copy()
        self.Transform(data, target, lookup)

        print('Transformed data:',target)
        return target

class Merchant(object):
    def GetProduct(self):
        print("Merchant:", self.Name, "GetProduct")
        data = self.adaptorImpl.GetData()
        return data

    def __init__(self, id):
        self.adaptorImpl = AdaptorImpl(id)
        self.Name = "Merchant1"

# adaptor = AdaptorImpl()
# adaptor.GetMetadata()

# source = {'a':12,'b':2}
# target = {'x':1, 'y':2, 'z':4}
# mapping = {'title': 'name'}
# adaptor = AdaptorImpl()
# adaptor.GetData()

merchant1 = Merchant(1)
merchant1.GetProduct()