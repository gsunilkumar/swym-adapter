from flask import Flask, json
from markupsafe import escape

metadata = [
  {
    "id": 0,
    "sku": "string",
    "name": "string",
    "attribute_set_id": 0,
    "price": 0,
    "status": 0,
    "visibility": 0,
    "type_id": "string",
    "created_at": "string",
    "updated_at": "string",
    "weight": 0
  },
  {
    "recordid": 0,
    "sku": "string",
    "title": "string",
    "prop_id": 0,
    "cost": 0,
    "status": 0,
    "visibility": 0
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
    api.run(port=port) 