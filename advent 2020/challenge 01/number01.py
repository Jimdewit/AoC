def puzzle_1_solver():
    raw = get_input('./input.txt')
    grouped = read_and_group(raw)
    large, small = estimate_candidates(grouped)
    answer = solve(large, small)
    print(answer)


def puzzle_1b_solver():
    raw = get_input('./input.txt')
    try:
        one, two, three = estimate_candidates(raw, brute_force_mode=True)
        answer = one * two * three
        print(answer)
    except FuckYouException:
        print("HOLY CRAP! FAILUREZ!!")


def get_input(inputfile):
    with open(inputfile, 'r') as numbers:
        ints = [int(number[:-1]) for number in numbers]
        return ints


def read_and_group(input):
    sizes = {}
    y = 1
    while y < 5:
        sizes[str(y)] = []
        for x in input:
            if len(str(x)) == y:
                sizes[str(y)].append(x)
        y += 1
    return sizes


class FuckYouException(object):
    pass


def estimate_candidates(input, brute_force_mode=False):
    if brute_force_mode:
        for first in input:
            try:
                for second in input:
                    if first + second > 2020:
                        continue
                    try:
                        for third in input:
                            try:
                                assert first + second + third == 2020
                                print('MATCH FOUND: {}, {} and {}'.format(first, second, third))
                                return first, second, third
                            except AssertionError:
                                pass
                    except AssertionError:
                        pass
            except AssertionError:
                pass
        raise FuckYouException

    for large_value in input['4']:
        try:
            for smaller_value in input['2']:
                assert large_value + smaller_value == 2020
                print('GOTCHA! {} and {}'.format(large_value, smaller_value))
                return large_value, smaller_value
        except AssertionError:
            pass
        try:
            for smaller_value in input['3']:
                assert large_value + smaller_value == 2020
                print('GOTCHA! {} and {}'.format(large_value, smaller_value))
                return large_value, smaller_value
        except AssertionError:
            pass


def solve(big_one, small_one):
    return big_one * small_one


if __name__ == "__main__":
    puzzle_1b_solver()
