from flask import Flask, json

product = [{
  'name':'some name',
  'description': 'some description',
  'price':100,
  'quantity':2
}]

api = Flask(__name__)
port = 7002

@api.route('/datafeed/<int:id>/product', methods=['GET'])
def get_companies(id):
  data = {}
  if id < len(product):
    data = product[id]
  return json.dumps(data)

if __name__ == '__main__':
    api.run(port=port) 