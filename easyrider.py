import json

# json_in = json.loads(input())


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
        lines = []
        for obj in Lines.lines:
            if obj.diag():
                starts.add(obj.start_name)
                stops.add(obj.stop_name)
                lines.append(obj.names)
            else:
                break
        print(f'Start stops: {len(starts)} {list(starts)}')
        print(f'Transfer stops: {len(lines)} {list(lines)}')
        print(f'Finish stops: {len(stops)} {list(stops)}')


s = """[{"bus_id" : 128, "stop_id" : 1, "stop_name" : "Prospekt Avenue", "next_stop" : 3, "stop_type" : "S", "a_time" : "08:12"}, 
{"bus_id" : 128, "stop_id" : 3, "stop_name" : "Elm Street", "next_stop" : 5, "stop_type" : "", "a_time" : "08:19"}, 
{"bus_id" : 128, "stop_id" : 5, "stop_name" : "Fifth Avenue", "next_stop" : 7, "stop_type" : "O", "a_time" : "08:25"}, 
{"bus_id" : 128, "stop_id" : 7, "stop_name" : "Sesame Street", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:37"}, 
{"bus_id" : 512, "stop_id" : 4, "stop_name" : "Bourbon Street", "next_stop" : 6, "stop_type" : "", "a_time" : "08:13"}, 
{"bus_id" : 512, "stop_id" : 6, "stop_name" : "Sunset Boulevard", "next_stop" : 0, "stop_type" : "F", "a_time" : "08:16"}]"""


Lines.set_data(json.loads(input()))
Lines.get_answer()
