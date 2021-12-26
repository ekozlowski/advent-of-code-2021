example = """[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]"""

open_char_types = ["(", "[", "{", "<"]
close_char_types = [")", "]", "}", ">"]

from collections import deque


points = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
}


def get_points(line):
    buffer = deque()
    for c in line:
        if c in open_char_types:
            buffer.append(c)
        elif c in close_char_types:
            index = close_char_types.index(c)
            if buffer[-1] != open_char_types[index]:
                return points.get(c)
            buffer.pop()

    return 0

total_points = 0
for line in [x for x in open('../input.txt', 'r').readlines() if x.strip()]:
     total_points += get_points(line)
print(total_points)

