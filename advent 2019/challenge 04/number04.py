from collections import Counter


def get_input():
    with open('./input.txt', 'r') as input_file:
        num_range = [l.strip('\n') for l in input_file.readlines()][0]
        min_num, max_num = int(num_range.split('-')[0]), int(num_range.split('-')[1])
    return min_num, max_num


def check_sizes(number):
    previous_digit = 0
    second_previous_digit = 0
    double = False
    treble = False
    for digit in str(number):
        digit = int(digit)
        matching_numbers = []
        if digit < previous_digit:
            return False, double, True
        if digit == previous_digit:
            double = True
        if digit == second_previous_digit:
            treble = True
            matching_numbers += [digit]
        second_previous_digit = previous_digit
        previous_digit = digit
    return True, double, treble


def check_candidates_again(candidates):
    filtered_candidates = []
    for number in candidates:
        number_check = Counter(y for y in str(number)).values()
        if max(number_check) > 2 and not 2 in number_check:
            continue
        elif 2 in number_check:
            filtered_candidates += [number]
    return filtered_candidates


def solve():
    min_num, max_num = get_input()
    candidates_a = []
    for x in range(min_num, max_num):
        valid, double, treble = check_sizes(x)
        if not valid:
            continue
        if not double:
            continue
        else:
            candidates_a += [x]

    candidates_b = check_candidates_again(candidates_a)

    print(len(candidates_a))
    print(candidates_b)
    print(len(candidates_b))


if __name__ == "__main__":
    solve()