def iterate_day(fish):
    new = fish.count('0')
    fish = fish.translate({56:55, 55:54, 54:53, 53:52, 52:51, 51:50, 50:49, 49:48, 48:54})
    fish = fish + ",8" * new
    return fish


if __name__ == "__main__":
    fish = open("../input.txt", 'r').read().strip()
    for x in range(80):
        fish = iterate_day(fish)
    print(len(fish.split(',')))
