import requests
from swym.adaptor import Adaptor
from adaptorImpl import AdaptorImpl

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

merchant1 = Merchant(0)
merchant1.GetProduct()