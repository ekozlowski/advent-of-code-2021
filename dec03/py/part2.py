lines = [x.strip() for x in open('../input.txt', 'r').readlines() if x.strip()]


def filter(lines, index, filterval, tiebreaker):
    lines = [x for x in lines if x[index] == filterval]
    if len(lines) == 2:
        if lines[0][index] == tiebreaker:
            return [lines[0]]
        else:
            return [lines[1]]
    return lines


def get_most_common(lines, index):
    count_zeros = len([x for x in lines if x[index] == "0"])
    count_ones = len([x for x in lines if x[index] == "1"])
    if count_ones > count_zeros:
        return "1"
    elif count_zeros == count_ones:
        return "1"
    else:
        return "0"


def get_least_common(lines, index):
    count_zeros = len([x for x in lines if x[index] == "0"])
    count_ones = len([x for x in lines if x[index] == "1"])
    if count_ones < count_zeros:
        return "1"
    elif count_zeros == count_ones:
        return "0"
    else:
        return "0"


if __name__ == "__main__":

    # Get Oxygen Rating
    index = 0
    newlines = lines[:]
    while len(newlines) > 1:
        mc = get_most_common(newlines, index)
        newlines = filter(newlines, index, mc, "1")
        index += 1
    print(newlines)
    firstval = newlines[0]

    # Get CO2 Scrubber Rating
    newlines = lines[:]
    print(newlines)
    index = 0
    while len(newlines) > 1:
        lc = get_least_common(newlines, index)
        newlines = filter(newlines, index, lc, "0")
        index += 1
    secondval = newlines[0]
    print(int(firstval, 2))
    print(int(secondval, 2))
    print(int(firstval, 2) * int(secondval, 2))
