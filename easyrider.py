import json
import jsonschema
from schema import schema, fileds
from collections import defaultdict


def json_validate():
    v = jsonschema.Draft7Validator(schema)
    for m in json_in:
        errors = v.iter_errors(m)
        for error in errors:
            filed_id = error.absolute_path[0]
            fileds[filed_id] += 1


def print_errors():
    print(f"Type and required field validation: {sum(fileds.values())} errors")
    for k, v in fileds.items():
        print(f"{k}: {v}")


json_in = json.loads(input())
line_stops = defaultdict(int)
for track in json_in:
    line_stops[track['bus_id']] += 1

for line, stops in line_stops.items():
    print(f"bus_id: {line}, stops: {stops}")

