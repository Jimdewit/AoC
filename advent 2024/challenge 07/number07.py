
def mult(a, b):
    return a * b


def add(a, b):
    return a + b


def concat(a,b):
    return int(f'{a}{b}')


def try_operators(operands, shared_results, desired_result, pos=0, part_two=False):
    _results = []
    for r in shared_results:
        r1 = add(r, operands[pos])
        r2 = mult(r, operands[pos])
        r3 = concat(r, operands[pos]) if part_two else 0
        _results += [r1, r2, r3] if part_two else [r1, r2]

    pos += 1
    shared_results = [x for x in _results if (x != 0 and x <= desired_result)]

    if pos == len(operands):
        return desired_result if desired_result in shared_results else 0
    else:
        return try_operators(operands, shared_results, desired_result, pos, part_two=part_two)


def solve_one(results):
    sum_of_correct_numbers = 0
    for r in results:
        desired_result, operands = r
        sum_of_correct_numbers += try_operators(operands, [0], desired_result)

    print(f'Correct: {sum_of_correct_numbers}')


def solve_two(results):
    sum_of_correct_numbers = 0
    numbers_seen = 1

    for r in results:
        if numbers_seen % 10 == 0:
            print(f'Seen {numbers_seen}/{len(results)}')

        desired_result, operands = r
        sum_of_correct_numbers += try_operators(operands, [operands[0]], desired_result, 1, True)

        numbers_seen += 1

    print(f'Correct two: {sum_of_correct_numbers}')


def get_input():
    all_results = []
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]

    for l in lines:
        result, operands = int(l.split(':')[0]), list(int(x) for x in l.split(':')[1].split())
        all_results += [(result, operands)]

    return all_results


def solve():
    daily_input = get_input()
    solve_one(daily_input)
    solve_two(daily_input)


if __name__ == "__main__":
    #print(97902811429005 - 97902809384118)
    solve()


