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
    targetValue = None
    if lookup[k] in sourceKeys:
        targetValue = source[lookup[k]]
    result[k] = targetValue
print("after:\t",result)