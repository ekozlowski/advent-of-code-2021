lines = [x.strip() for x in open('../input.txt').readlines()]

low_points = []

for i, line in enumerate(lines):
    for j, c in enumerate(line):
        print(line[j:])
        higher = True
        lower = True
        right = True
        left = True
        # [i,j] are the coords.
        if i == 0:  # no higher
            higher = False
        if i+1 == len(lines): # no lower
            lower = False
        if j == 0:  # none left
            left = False
        if j+1 == len(lines): # none right
            right = False
        points = []
        if higher:
            points.append(lines[i-1][j])
            if left:
                points.append(lines[i-1][j-1])
            if right:
                points.append(lines[i-1][j+1])
        if left:
            points.append(line[j-1])
        if right:
            points.append(line[j+1])
        if lower:
            points.append(lines[i+1][j])
            if left:
                points.append(lines[i+1][j-1])
            if right:
                points.append(lines[i+1][j+1])
        points = list(map(int, points))
        if int(c) < min(points):
            low_points.append(int(c))
            print(f"Low point: {c}")
            print(points)

print(low_points)
risk_points = [x+1 for x in low_points]
print(sum(risk_points))