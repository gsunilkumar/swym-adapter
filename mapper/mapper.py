import json

source = {
  "id": 123,
  "sku": "string",
  "name": "test name",
  "price": 0
}

# target schema
lookup = {
    "recordid" : "id2",
    "title"    : "name"
}

print("source:", json.dumps(source, indent=2))
print("lookup:", json.dumps(lookup, indent=2))

result = lookup.copy()
print("before:\t",result)

sourceKeys = source.keys()
for k in result:
    if lookup[k] in sourceKeys:
        result[k] = source[lookup[k]]
    else:
        result[k] = None
print("after:\t",result)