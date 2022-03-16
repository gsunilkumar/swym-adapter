import json
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
        configSource = "./mapping.json"
        mappings = {}
        with open(configSource, 'r') as f:
            mappings = json.load(f)
        return mappings

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