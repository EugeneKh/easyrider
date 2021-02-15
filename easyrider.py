import json
from collections import defaultdict

json_in = json.loads(input())
line_stops = defaultdict(int)
for track in json_in:
    line_stops[track['bus_id']] += 1

for line, stops in line_stops.items():
    print(f"bus_id: {line}, stops: {stops}")
