from copy import deepcopy


def get_input():
    with open('./test_input.txt', 'r') as file:
        return [int(x[:-1]) for x in file]


def solve(joltages, arrangement_finder=False):
    sorted_joltages = deepcopy(joltages)
    sorted_joltages += [max(sorted_joltages) + 3]
    sorted_joltages += [0]
    sorted_joltages = sorted(sorted_joltages)
    pos = 1
    distri_dict = {1: 0, 2: 0, 3: 0}

    while pos < len(sorted_joltages):
        diff = sorted_joltages[pos] - sorted_joltages[pos-1]
        distri_dict[diff] += 1
        pos += 1
    if not arrangement_finder:
        return distri_dict[1] * distri_dict[3]

    else:
        valid_routes = 1
        consec_counter = 0
        pos = 0
        y = 1
        x = sorted_joltages[pos]
        while 1 == 1:
            if x+y in sorted_joltages:
                consec_counter += 1
                y += 1
            else:
                if consec_counter <= 1:
                    valid_routes *= 1
                if consec_counter == 2:
                    valid_routes *= 2
                if consec_counter == 3:
                    valid_routes *= 4
                if consec_counter == 4:
                    valid_routes *= 7
                if consec_counter == 5:
                    valid_routes *= 13
                if consec_counter == 6:
                    valid_routes *= 22
                if consec_counter == 7:
                    valid_routes *= 42
                pos += consec_counter if consec_counter > 0 else 1
                if pos >= len(sorted_joltages) - 1:
                    break
                x = sorted_joltages[pos]
                y = 1
                consec_counter = 0

        return valid_routes


def main():
    adapter_joltage_list = get_input()
    answer_one = solve(adapter_joltage_list)
    print("Distribution range calculation came to: {}".format(answer_one))
    answer_two = solve(adapter_joltage_list, arrangement_finder=True)
    print("Number of valid chains: {}".format(answer_two))


if __name__ == "__main__":
    main()