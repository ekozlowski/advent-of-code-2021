initial = "3,4,3,1,2"
fish = map(int, initial.split(','))


def iterate_day(old):
    new = {8: old.get(0, 0), 0: old.get(1, 0), 1: old.get(2, 0), 2: old.get(3, 0), 3: old.get(4, 0), 4: old.get(5, 0),
           5: old.get(6, 0), 6: old.get(7, 0), 7: old.get(8, 0)}
    new[6] = new[6] + old.get(0, 0)
    return new


if __name__ == "__main__":
    fish = open("../input.txt", 'r').read().strip()
    fish = map(int, fish.split(','))

    # -- initial setup into age pools
    age_pools = {}
    for f in fish:
        count = age_pools.get(f, 0)
        age_pools[f] = count + 1

    # iterate days
    for x in range(256):
        age_pools = iterate_day(age_pools)
        print(f"Day {x+1}, Sum: {sum([x for x in age_pools.values()])}", age_pools)