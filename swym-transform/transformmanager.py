import json
import requests
from mapper import Mapper
import os

class TransformManager(object):
	def __init__(self):
	  self.ProviderUrlFormat = "http://{basepath}/provider/{id}/metadata"
	  self.provider_basepath = "localhost:7001"
	  if 'PROVIDER_API' in os.environ:
		  self.provider_basepath = os.environ['PROVIDER_API']

	def GetMetadata(self, provider):
	  providerEndpoint = self.ProviderUrlFormat.format(basepath=self.provider_basepath,id=provider)
	  print("Fetching metadata from: ", providerEndpoint)

	  r = requests.get(providerEndpoint)
	  data = r.json()
	  print("Product Metadata", data)
	  return data

	def GetMappings(self, id): # input: mapping id
	  configSource = "./mapping.json"
	  lookup = {}
	  with open(configSource, 'r') as f:
	      lookup = json.load(f)

	  if id < len(lookup):
	  	return lookup[id]
	  return {}

	def Transform(self, payload):
		mappingId = payload["id"]
		mapping = self.GetMappings(mappingId)
		print(mapping)

		lookup = mapping['lookup'] 
		print("Lookup:",lookup)
		destination = self.GetMetadata(mapping['provider'])
		print(destination)
		data = []

		for item in payload["products"]:
			print("Apply transform: ",item)
			t = Mapper.Transform(item, destination, lookup)
			data.append(t)
		return data

# t=TransformManager()
# data=t.GetMetadata(1)
# print(data)
# print(t.GetMappings(0))

# payload={
# 	"id":0,
# 	"provider":1,
# 	"products":[
# 		{
# 			"a":2,
# 			"price":100,
# 			"name":"some title1"
# 		},
# 		{
# 			"a":2,
# 			"price":200,
# 			"name":"some title2"
# 		}
# 	]
# }
# print(t.Transform(payload))