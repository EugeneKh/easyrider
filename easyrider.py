import json
from itertools import combinations


class Lines:
    lines = []
    arrival_time = True

    def __init__(self, line):
        self.line = line

        self.names = set()
        self.starts = 0
        self.start_name = ''
        self.stops = 0
        self.stop_name = ''
        self.ondemainds = set()

        self.last_time = 0
        self.time_error_points = []

        Lines.lines.append(self)

    def add_stop(self, name, stop_type, time):
        cur_time = int(time.replace(':', ""))
        if cur_time <= self.last_time:
            self.time_error_points.append(name)
        self.last_time = cur_time

        if stop_type == 'S':
            self.starts += 1
            self.start_name = name
        if stop_type == 'F':
            self.stops += 1
            self.stop_name = name
        if stop_type == 'O':
            self.ondemainds.add(name)
        self.names.add(name)

    @staticmethod
    def set_data(json_data):
        d = {}
        for track in json_data:
            if track['bus_id'] not in d:
                d[track['bus_id']] = Lines(track['bus_id'])
            d[track['bus_id']].add_stop(track['stop_name'],
                                        track['stop_type'],
                                        track['a_time'], )

    def end_points_test(self):  # TODO: Rename
        if self.starts != 1 or self.stops != 1:
            print(f'There is no start or end stop for the line: {self.line}.')
            return False
        return True

    @staticmethod
    def stops_test(n: int):
        starts, stops, ondemainds = set(), set(), set()
        all_names = []
        for obj in Lines.lines:
            if obj.end_points_test():
                starts.add(obj.start_name)
                stops.add(obj.stop_name)
                ondemainds |= obj.ondemainds
                all_names.append(obj.names)
            else:
                break

        transfers = set()
        for a, b in combinations(all_names, 2):
            transfers |= set.intersection(a, b)
        if n == 3:
            print(f'Start stops: {len(starts)} {sorted(list(starts))}')
            print(f'Transfer stops: {len(transfers)} {sorted(list(transfers))}')
            print(f'Finish stops: {len(stops)} {sorted(list(stops))}')
        if n == 6:
            print('On demand stops test:')
            er_s = set()
            er_s |= set.intersection(ondemainds, starts)
            er_s |= set.intersection(ondemainds, transfers)
            er_s |= set.intersection(ondemainds, stops)
            if er_s:
                print(f'Wrong stop type: {sorted(list(er_s))}')
            else:
                print('OK')

    @staticmethod
    def times_test():
        print('Arrival time test:')
        t_error = False
        for obj in Lines.lines:
            if obj.time_error_points:
                print(f'bus_id line {obj.line}: wrong time on station {obj.time_error_points[0]}')
                t_error = True
                continue
        if not t_error:
            print('OK')


Lines.set_data(json.loads(input()))
# Lines.times_test()
Lines.stops_test(6)
