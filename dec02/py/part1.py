lines = open('../input.txt', 'r').readlines()

class Submarine:
    def __init__(self):
        self.depth = 0
        self.horizontal_position = 0

    def forward(self, x):
        self.horizontal_position += x

    def up(self, x):
        self.depth -= x

    def down(self, x):
        self.depth += x

    def move(self, direction, units):
        if direction == "forward":
            self.forward(units)
        elif direction == "down":
            self.down(units)
        elif direction == "up":
            self.up(units)


    def __str__(self):
        return f"<Submarine at depth: {self.depth} forward {self.horizontal_position}>"

if __name__ == "__main__":
    s = Submarine()
    for l in [x.strip() for x in lines]:
        direction, units = l.split()
        units = int(units)
        s.move(direction, units)
    print(s.depth * s.horizontal_position)
    print(s)

