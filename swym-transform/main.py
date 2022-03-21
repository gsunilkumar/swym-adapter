from flask import Flask, json, request
from transformsvc import TransformSvc

transformsvc = TransformSvc()
api = Flask(__name__)
port = 7003


@api.route('/api/swym/transform', methods=['POST'])
def GetTransformedData():
  payload = request.get_json(force=True)
  return transformsvc.Transform(payload)

if __name__ == '__main__':
    api.run(host ='0.0.0.0',port=port)