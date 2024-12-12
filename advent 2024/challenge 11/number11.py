import copy
from datetime import datetime


def process_stones(inp: list, iterations: int):
    blink = 1
    outer_map = {}
    start = datetime.now()

    for x in inp:
        if outer_map.get(x):
            outer_map[x] += 1
        else:
            outer_map[x] = 1

    while blink <= iterations:
        k = list(k for k in outer_map.keys() if outer_map[k] > 0)
        value_map = copy.deepcopy(outer_map)
        for x in value_map.keys():
            value_map[x] = 0
        k.sort()
        for x in k:
            times = outer_map[x]
            #value_map[x] = 0
            if x == 0:
                value_map[1] = times
            elif len(str(x)) % 2 == 0:
                n = str(x)
                new = [int(n[:int(len(n) / 2)]), int(n[int(len(n)/2):])]
                for n in new:
                    if n == 40:
                        pass
                    if value_map.get(n):
                        value_map[n] += times
                    else:
                        value_map[n] = times
            else:
                new = x * 2024
                if value_map.get(new):
                    value_map[new] += times
                else:
                    value_map[new] = times


        outer_map = value_map
        blink += 1

    print(f'Done blinking, it took {datetime.now()-start}')

    return sum(x for x in outer_map.values() if x > 0)


def get_input() -> list:
    with open('./input.txt', 'r') as input_file:
        stones = [int(l) for l in input_file.readline().strip('\n').split()]

    return stones


def solve():
    daily_input = get_input()
    first = process_stones(daily_input, 25)
    second = process_stones(daily_input, 75)
    print(f'First: {first}, second: {second}')


if __name__ == "__main__":
    solve()
