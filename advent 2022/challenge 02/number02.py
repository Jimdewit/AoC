
def process_strategy(results):
    total_score = 0

    for match in results:
        shape_score = 0
        if match[0] == 'A':
            if match[1] == 'X':
                result = 'loss'
                shape_score = 3
            if match[1] == 'Y':
                result = 'draw'
                shape_score = 1
            if match[1] == 'Z':
                result = 'win'
                shape_score = 2
        if match[0] == 'B':
            if match[1] == 'X':
                result = 'loss'
                shape_score = 1
            if match[1] == 'Y':
                result = 'draw'
                shape_score = 2
            if match[1] == 'Z':
                result = 'win'
                shape_score = 3
        if match[0] == 'C':
            if match[1] == 'X':
                result = 'loss'
                shape_score = 2
            if match[1] == 'Y':
                result = 'draw'
                shape_score = 3
            if match[1] == 'Z':
                result = 'win'
                shape_score = 1

        if result == 'win':
            round_score = 6
        if result == 'draw':
            round_score = 3
        if result == 'loss':
            round_score = 0

        total_score += round_score + shape_score

    return total_score


def process_matches(results):
    total_score = 0

    for match in results:
        shape_score = 0
        if match[0] == 'A':
            if match[1] == 'X':
                result = 'draw'
                shape_score = 1
            if match[1] == 'Y':
                result = 'win'
                shape_score = 2
            if match[1] == 'Z':
                result = 'loss'
                shape_score = 3
        if match[0] == 'B':
            if match[1] == 'X':
                result = 'loss'
                shape_score = 1
            if match[1] == 'Y':
                result = 'draw'
                shape_score = 2
            if match[1] == 'Z':
                result = 'win'
                shape_score = 3
        if match[0] == 'C':
            if match[1] == 'X':
                result = 'win'
                shape_score = 1
            if match[1] == 'Y':
                result = 'loss'
                shape_score = 2
            if match[1] == 'Z':
                result = 'draw'
                shape_score = 3

        if result == 'win':
            round_score = 6
        if result == 'draw':
            round_score = 3
        if result == 'loss':
            round_score = 0

        total_score += round_score + shape_score

    return total_score


def get_input():
    with open('./input.txt', 'r') as input_file:
        results = []
        lines = [l.strip('\n') for l in input_file.readlines()]
        for line in lines:
            results.append((line.split(' ')))

    return results


def solve():
    match_results = get_input()
    print(process_matches(match_results))
    print(process_strategy(match_results))


if __name__ == "__main__":
    solve()
