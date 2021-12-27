
# octogrid is (x,y,) keys that are Octopus objects.
octogrid = {}

# In this way, if an octopus flashes, we can increase adjacent energy levels by looking up (y-1, (x-1, x, x+1)),
#(x-1, x+1), and (y+1, x-1, x, x+1) and increase their energy levels as appropriate.

flashes = 0

class Octopus:
    def __init__(self, energy_level, x, y):
        self.energy_level = energy_level
        self.has_flashed = False
        self.x = x
        self.y = y

    def increase_energy_level(self):
        if self.has_flashed:
            return
        self.energy_level += 1
        if self.energy_level >= 9:
            self.flash()

    def flash(self):
        global flashes
        if self.energy_level <= 9:
            return
        if self.has_flashed:
            return
        flashes += 1
        self.has_flashed = True
        # find all adjacent to me, and increase their energy levels.
        coords = [(self.x-1, self.y+1), (self.x, self.y+1), (self.x+1, self.y+1), (self.x-1, self.y), (self.x+1, self.y), (self.x-1, self.y-1), (self.x, self.y-1), (self.x+1, self.y-1)]
        for c in coords:
            octo = octogrid.get(c)
            if octo is not None:
                octo.increase_energy_level()
        self.energy_level = 0

    def __str__(self):
        return f" {self.energy_level} {self.has_flashed} "

    def __repr__(self):
        return str(self)

grid = """5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526"""

grid = [x.strip() for x in open('../input.txt', 'r').readlines()]

# reversed, b/c the y coord starts at the _bottom_ as 0.  (ex, row 11111 at the bottom is y=0)
for y, line in enumerate(grid):
    for x, c in enumerate(line):
        print(x,y)
        o = Octopus(int(c), x, y)
        octogrid[(x, y)] = o



def render_grid():
    # grid is 5x5
    # at start
    ys = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for y in reversed(ys):
        s = ''
        for x in range(10):
            s += str(octogrid.get((x, y,)))
        print(s)

# steps:

# Increase the energy of _every_ octopus by 1.
# any octopus with energy level > 9 <flashes>
    # increase energy level of all adjacent by 1.
    # if this causes an octo to have > 9, it _also_ flashes.
    # continues as long as new octos keep having their energy level raised beyond 9.
    # octos can only flash once per step
# any octo that flashed has energy level set to 0.

if __name__ == "__main__":
    render_grid()
    last_flashes = flashes
    for x in range(100):
        for o in octogrid.values():
            o.increase_energy_level()
        for o in octogrid.values():
            o.flash()
        for o in octogrid.values():
            if o.has_flashed:
                o.energy_level = 0
        print(f"after step {x + 1}")
        render_grid()
        print(f"Resetting flash.")
        for o in octogrid.values():
            o.has_flashed = False
        last_flashes = flashes
    print(f"{flashes} flashes")