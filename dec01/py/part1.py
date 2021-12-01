depths = [int(x.strip()) for x in open('../input.txt', 'r').readlines()]
prev = None
increases = 0
for d in depths:
    if prev is None:
        prev = d
        continue
    if d > prev:
        increases += 1
    prev = d
print(increases)

