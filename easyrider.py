import json
import jsonschema
from schema import schema, fileds

json_in = json.loads(input())
v = jsonschema.Draft7Validator(schema)
for m in json_in:
    errors = v.iter_errors(m)
    for error in errors:
        filed_id = error.absolute_path[0]
        fileds[filed_id] += 1

print(f"Type and required field validation: {sum(fileds.values())} errors")
for k, v in fileds.items():
    print(f"{k}: {v}")
