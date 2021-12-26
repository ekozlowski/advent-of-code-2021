
caves = {}

class Cave:

    def __init__(self, label):
        self.label = label
        self.connections = []

    def add_connection(self, c):
        if c not in self.connections:
            self.connections.append(c)

    def __repr__(self):
        return f"<Cave {self.label} with connections to {self.connections}>"


class Visitor:

    def __init__(self, start_cave, pred_choices):
        self.pred_choices = pred_choices
        self.start_cave = start_cave
        self.current_cave = start_cave
        self.visited = []
        self.visited.append(self.start_cave.label)

    def move(self, cave_text):
        print(f"Moving to {cave_text}")
        self.current_cave = caves.get(cave_text)
        self.visited.append(cave_text)

    def pick_path(self):
        # If there is a predecessor, try unvisited paths from the predecessor
        if self.pred_choices:
            for c in self.current_cave.connections:
                if c not in self.pred_choices:
                    return c
        # first, try unvisited paths:
        for c in self.current_cave.connections:
            if c not in self.visited:
                print(f"Picked {c}")
                return c
        # if we haven't returned, the only path back is back the way we came.
        for c in self.current_cave.connections:
            print(f"Revisiting {c}")
            return c


    def find_path(self):
        while self.current_cave.label != "end":
            self.move(self.pick_path())


    def visualize(self):
        print('->'.join([seg for seg in self.visited]))

if __name__ == "__main__":
    data = """start-A
start-b
A-c
A-b
b-d
A-end
b-end"""
    #for x in [line.strip() for line in open('../input.txt', 'r').readlines()]:
    for x in [line.strip() for line in data.split('\n')]:
        begin, end = x.split('-')
        b = caves.get(begin, Cave(begin))
        b.add_connection(end)
        e = caves.get(end, Cave(end))
        e.add_connection(begin)
        caves[begin] = b
        caves[end] = e
    print(caves)

    v = Visitor(caves.get('start'), pred_choices=None)
    v.find_path()
    v.visualize()

    for x in range(10):
        pred_choices = v.visited
        print(pred_choices)
        v = Visitor(caves.get('start'), pred_choices=pred_choices)
        v.find_path()
        v.visualize()
