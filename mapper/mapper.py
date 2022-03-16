# # importing the module
import json
 
# # Opening JSON file
# with open('data.json') as json_file:
#     data = json.load(json_file)

#     # Print the type of data variable
#     print("Type:", type(data))

#     print(data)

# input schema
source = {
  "id": 123,
  "sku": "string",
  "name": "test name",
  "price": 0
}

# target schema
lookup = {
    "recordid" : "id",
    "title"    : "name"
}

print("source:", json.dumps(source, indent=2))
print("lookup:", json.dumps(lookup, indent=2))

result = lookup.copy()
print(result)
result1={}
for k in result:
    # result[k] = source[lookup[k]]
    print(k, result1)
    # setattr(result1, k, 99)

    setattr(result1, k, 99)
print(result)

print(source.__class__)
