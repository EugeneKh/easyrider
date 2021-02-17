import json
from itertools import combinations


class Lines:
    lines = []

    def __init__(self, line):
        self.line = line
        self.names = set()
        self.starts = 0
        self.stops = 0
        self.start_name = ''
        self.stop_name = ''
        Lines.lines.append(self)

    def add_stop(self, name, stop_type):
        if stop_type == 'S':
            self.starts += 1
            self.start_name = name
        if stop_type == 'F':
            self.stops += 1
            self.stop_name = name
        self.names.add(name)

    def diag(self):
        if self.starts != 1 or self.stops != 1:
            print(f'There is no start or end stop for the line: {self.line}.')
            return False
        return True

    @staticmethod
    def set_data(json_data):
        d = {}
        for track in json_data:
            if track['bus_id'] not in d:
                d[track['bus_id']] = Lines(track['bus_id'])
            d[track['bus_id']].add_stop(track['stop_name'], track['stop_type'])

    @staticmethod
    def get_answer():
        starts, stops = set(), set()
        all_names = []
        for obj in Lines.lines:
            if obj.diag():
                starts.add(obj.start_name)
                stops.add(obj.stop_name)
                all_names.append(obj.names)
            else:
                break
        all_stops = set()
        for a, b in combinations(all_names, 2):
            all_stops |= set.intersection(a, b)
        print(f'Start stops: {len(starts)} {sorted(list(starts))}')
        print(f'Transfer stops: {len(all_stops)} {sorted(list(all_stops))}')
        print(f'Finish stops: {len(stops)} {sorted(list(stops))}')


Lines.set_data(json.loads(input()))
Lines.get_answer()
