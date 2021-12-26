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


def get_completion(line):
    buffer = deque()
    for c in line:
        if c in open_char_types:
            buffer.append(c)
        elif c in close_char_types:
            buffer.pop()
    # What I'm left with is the completion string in the buffer.
    s = ""
    while buffer:
        s += close_char_types[open_char_types.index(buffer.pop())]
    return s

def get_completion_score(completion):
    completion_score_lookup = {
        ")": 1,
        "]": 2,
        "}": 3,
        ">": 4
    }
    score = 0
    for c in completion:
        score = score * 5
        score = score + completion_score_lookup.get(c)
    return score

def is_corrupt(line):
    buffer = deque()
    for c in line:
        if c in open_char_types:
            buffer.append(c)
        elif c in close_char_types:
            index = close_char_types.index(c)
            if buffer[-1] != open_char_types[index]:
                return True
            buffer.pop()
    return False

scores = []
for line in [x for x in open('../input.txt', 'r').readlines() if x.strip()]:
    if not is_corrupt(line):
        completion = get_completion(line)
        print(f"Completion: {completion} Completion score: {get_completion_score(completion)}")
        scores.append(get_completion_score(completion))

scores.sort()
print(len(scores))
print(len(scores) // 2)
print(scores[(len(scores) // 2)])