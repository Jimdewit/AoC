import datetime


def process_pregnancy(fishes, more_fish={}, day_counter=1, max_days=80):

    if day_counter == 1:
        more_fish = {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
        for fish in fishes:
            if fish == 0:
                more_fish[8] += 1
                more_fish[6] += 1
            else:
                more_fish[fish-1] += 1
    else:
        fish_giving_birth = more_fish[0]

        more_fish[0] = more_fish[1]
        more_fish[1] = more_fish[2]
        more_fish[2] = more_fish[3]
        more_fish[3] = more_fish[4]
        more_fish[4] = more_fish[5]
        more_fish[5] = more_fish[6]
        more_fish[6] = more_fish[7] + fish_giving_birth
        more_fish[7] = more_fish[8]
        more_fish[8] = fish_giving_birth


    if day_counter < max_days:
        day_counter += 1
        #print('{} - Currently at iteration {}, fish length at {}'.format(datetime.datetime.now(), day_counter, sum(v for v in more_fish.values()) if day_counter > 1 else 1))
        return process_pregnancy(fishes, more_fish, day_counter, max_days=max_days)
    else:
        return sum(v for v in more_fish.values())


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [int(x) for x in [l.strip('\n').split(',') for l in input_file.readlines()][0]]
    return lines


def solve():
    fishes = get_input()
    more_fishes = process_pregnancy(fishes)
    print(more_fishes)
    even_more_fishes = process_pregnancy(fishes, max_days=256)
    print(even_more_fishes)


if __name__ == "__main__":
    solve()