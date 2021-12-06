# 345793
# 1572643095893


def process_pregnancy(more_fish, day_counter=1, max_days=80):
    fish_giving_birth = more_fish[0]
    for x in range(0,8):
        more_fish[x] = more_fish[x+1] if x != 6 else (more_fish[x+1] + fish_giving_birth)
    more_fish[8] = fish_giving_birth

    if day_counter < max_days:
        day_counter += 1
        return process_pregnancy(more_fish, day_counter, max_days=max_days)
    else:
        return sum(v for v in more_fish.values())


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [int(x) for x in [l.strip('\n').split(',') for l in input_file.readlines()][0]]
        more_fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0}
        for fish in lines:
            more_fish[fish] += 1
    return more_fish


def solve():
    fishes = get_input()
    more_fishes = process_pregnancy(fishes)
    print(more_fishes)
    even_more_fishes = process_pregnancy(fishes, max_days=255)
    print(even_more_fishes)


if __name__ == "__main__":
    solve()
