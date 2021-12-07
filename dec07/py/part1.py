input = open('../input.txt', 'r').read()


class Crab:
    def __init__(self, pos):
        self.pos = pos
        self.fuel_spent = 0

    def move(self, pos):
        self.fuel_spent += abs(self.pos - pos)


crabs = [Crab(int(x)) for x in input.strip().split(',')]


for x in range(1000):
    for c in crabs:
        c.move(x)
    print(f"Position {x} Total Fuel: {sum([c.fuel_spent for c in crabs])}")
    for c in crabs:
        c.fuel_spent = 0
