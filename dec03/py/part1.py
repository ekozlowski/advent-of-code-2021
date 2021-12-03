lines = [x.strip() for x in open('../input.txt', 'r').readlines() if x.strip()]

gamma = ""
epsilon = ""

for x in range(len(lines[0])):
    zeros = 0
    ones = 0
    for l in lines:
        if l[x] == "0":
            zeros += 1
        else:
            ones += 1
    if zeros > ones:
        gamma = gamma + "0"
        epsilon = epsilon + "1"
    else:
        gamma = gamma + "1"
        epsilon = epsilon + "0"

print("Gamma is: ", gamma, int(gamma, 2))
print("Epsilon is: ", epsilon, int(epsilon, 2))
print("Gamma times epsilon: ", int(gamma,2) * int(epsilon,2))