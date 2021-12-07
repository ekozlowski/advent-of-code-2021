input = open('../input.txt', 'r').read()


class Crab:
    def __init__(self, pos):
        self.pos = pos
        self.fuel_spent = 0

    def move(self, pos):
        distance = abs(self.pos - pos)
        self.fuel_spent = (distance * (distance + 1)) // 2


crabs = [Crab(int(x)) for x in input.strip().split(',')]
minimum_pos = min([c.pos for c in crabs])
maximum_pos = max([c.pos for c in crabs])

fuels_spent = []

for x in range(minimum_pos, maximum_pos + 1):
    for c in crabs:
        c.move(x)
    fuels_spent.append(sum([c.fuel_spent for c in crabs]))
    for c in crabs:
        c.fuel_spent = 0

print(min(fuels_spent))