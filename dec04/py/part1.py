class Board:
    def __init__(self, lines):
        self.data = []
        for i, l in enumerate(lines):
            self.data.append([int(x) for x in l.split()])

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return str(self)

    def uncalled_numbers(self, called):
        nums = []
        for row in self.data:
            nums.extend(row)
        not_called = list(set(nums) - set(called))
        return not_called

    def won(self, called):
        called = set(called)

        # horzontally
        for row in self.data:
            if set(row).issubset(called):
                return True

        # vertically
        for x in range(5):
            s = set()
            for y in range(5):
                s.add(self.data[y][x])
            if s.issubset(called):
                return True
        return False



if __name__ == "__main__":
    lines = open('../input.txt', 'r').readlines()
    called = lines[0]
    boards = []
    accum = []

    for l in lines[1:]:
        if not l.strip() and accum:
            boards.append(Board(accum))
            accum = []
        else:
            accum.append(l.strip())
    called_numbers = []
    won = False
    boards = boards[1:]
    for call in called.split(','):
        if won:
            break
        called_numbers.append(int(call))
        print(f"Called {call}")
        for b in boards:
            if b.won(called_numbers):
                print(b)
                won = True
                print(f'Just called was: {call}')
                uncalled = b.uncalled_numbers(called_numbers)
                print(f"Sum of uncalled {sum(uncalled)}")
                print(f"{sum(uncalled) * int(call)}")
hide = """
    data = "20 87 16 25  9
15 70 19 72 56
71 37 69  2 62
76 97 41  8 92
40 65 86  0 32"
    data = data.split('\n')
    b = Board(data)
    print(b.data)
    print(b.won([15,70,19,72,56]))
    print(b.won([20,15,71,76,40]))
    print(b.won([16,22,7,19,2,69,80,41,82]))
"""