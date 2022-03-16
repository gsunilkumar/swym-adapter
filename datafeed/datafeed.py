from flask import Flask, json

product = [{
  'name':'some name',
  'description': 'some description',
  'price':100,
  'quantity':2
  },
  {
    'name':'some product',
    'description': 'some notes',
    'price':200,
    'quantity':7
  }
]

api = Flask(__name__)
port = 7002

@api.route('/datafeed/<int:id>/product', methods=['GET'])
def get_companies(id):
  data = {}
  if id < len(product):
    data = product[id]
    print(data)
  return json.dumps(data)

if __name__ == '__main__':
    api.run(host ='0.0.0.0',port=port)