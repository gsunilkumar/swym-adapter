import json
import requests
from transformmanager import TransformManager

class TransformSvc(object):
	def __init__(self):
	  self.manager = TransformManager()

	def Transform(self, payload):
		print("Received request to transform", payload)
		transformedData = self.manager.Transform(payload)
		print("transformedData", transformedData)
		
		return json.dumps(transformedData)