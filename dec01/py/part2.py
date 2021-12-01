depths = [int(x.strip()) for x in open('../input.txt', 'r').readlines()]

increases = 0
for i, d in enumerate(depths):
    if i + 4 > len(depths):
        break
    first_window = depths[i:i+3]
    second_window = depths[i+1:i+4]
    if sum(first_window) < sum(second_window):
        increases += 1
print(increases)