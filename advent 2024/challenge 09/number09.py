import copy
from collections import Counter


def defragment_part_one(inp):
    i = 0
    while i < len(inp):
        if inp[i] == '.':
            while inp[-1] == '.':
                inp = inp[:-1]
            inp[i] = inp[-1]
            inp = inp[:-1]
        i += 1
        #print(i)

    sum = 0
    for i in range(len(inp)):
        sum += i * inp[i]
    print(sum)


def defragment_part_two(inp):
    reverse = copy.deepcopy(inp)
    reverse.reverse()
    reverse = dict(Counter(x for x in reverse if x != '.'))

    map_of_empties = {}

    i = 0
    while i < len(inp):
        if inp[i] == '.':
            i2 = i
            while inp[i2] == '.':
                i2 += 1
            map_of_empties[i] = i2 - i
            i = i2
        else:
            i += 1

    for k in reverse.keys():
        print(f'Only {k} left!')
        length_needed = reverse[k]

        inp, map_of_empties = find_match(k, map_of_empties, length_needed, inp)

    total = 0
    for x in range(len(inp)):
        total += inp[x] * x if inp[x] != '.' else 0
    print(total)


def find_match(k: int, map_of_empties: dict, length_needed: int, inp: list):
    max_search = inp.index(k)
    for m in map_of_empties.keys():
        if m > max_search:
            return inp, map_of_empties
        if map_of_empties[m] >= length_needed:
            map_of_empties[m + length_needed] = map_of_empties[m] - length_needed
            map_of_empties.pop(m)
            inp = inp[:inp.index(k)] + ['.' for x in range(length_needed)] + inp[inp.index(k) + length_needed:]
            inp = inp[:m] + [k for x in range(length_needed)] + inp[m + length_needed:]

            map_of_empties = dict(sorted(map_of_empties.items()))

            return inp, map_of_empties

    return inp, map_of_empties


def get_input():
    with open('./input.txt', 'r') as input_file:
        l = [int(x) for x in input_file.readline().strip('\n')]

    explicit_blocks = []
    id_counter = 0
    for pos in range(len(l)):
        is_block_size = True if pos % 2 == 0 else False
        for block in range(l[pos]):
            explicit_blocks += [id_counter] if is_block_size else ['.']
        id_counter += 1 if is_block_size else 0

    return explicit_blocks


def solve():
    daily_input = get_input()
    #print(daily_input)
    # defragment_part_one(daily_input)
    defragment_part_two(daily_input)


if __name__ == "__main__":
    solve()
