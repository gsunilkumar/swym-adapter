from flask import Flask, json

metadata = [
  {
    "id": 0,
    "sku": "",
    "name": "",
    "attribute_set_id": 0,
    "price": 0,
    "status": 0,
    "visibility": 0,
    "type_id": "",
    "created_at": "",
    "updated_at": "",
    "weight": 0,
    "provider": "Provider 0"
  },
  {
    "recordid": 0,
    "sku": "",
    "title": "",
    "prop_id": 0,
    "cost": 0,
    "status": 0,
    "visibility": 0,
    "provider": "Provider 1"
  },
  {
    "recordid": 0,
    "sku": "",
    "title": "",
    "prop_id": 0,
    "cost": 0,
    "status": 0,
    "visibility": 0,
    "provider": "Provider 2"
  }
]

api = Flask(__name__)
port = 7001

@api.route('/provider/<int:id>/metadata', methods=['GET'])
def get_companies(id):
  data = {}
  if id < len(metadata):
    data = metadata[id]
  return json.dumps(data)

if __name__ == '__main__':
    api.run(host ='0.0.0.0',port=port) 