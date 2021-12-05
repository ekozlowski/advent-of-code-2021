lines = [x.strip() for x in open('../input.txt', 'r').readlines() if x.strip()]


def get_all_coords_between_points(x1, y1, x2, y2):
    coords = []
    # Handle horizontal lines
    if x1 == x2:
        if y1 < y2:
            for c in range(y1, y2 + 1):
                coords.append((x1, c,))
        elif y1 > y2:
            for c in range(y2, y1 + 1):
                coords.append((x1, c,))
    # Handle vertical lines
    elif y1 == y2:
        if x1 < x2:
            for c in range(x1, x2 + 1):
                coords.append((c, y1,))
        elif x1 > x2:
            for c in range(x2, x1 + 1):
                coords.append((c, y1,))
    return coords


# Grab every coordinate that got "hit" by a line
coord_objs = []
for line in lines:
    first, second = line.split('->')
    x1, y1 = map(int, first.split(','))
    x2, y2 = map(int, second.split(','))
    coord_objs.extend(get_all_coords_between_points(x1, y1, x2, y2))

# Count hits
counter = {}
for c in coord_objs:
    count = counter.get(f"{c[0]},{c[1]}", 0)
    count += 1
    counter[f"{c[0]},{c[1]}"] = count

print(len([c for c in counter if counter.get(c) > 1]))
