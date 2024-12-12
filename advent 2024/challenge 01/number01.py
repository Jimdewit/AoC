
def determine_distance(left, right):
    total_distance = 0
    x = 0
    while x < len(left):
        total_distance += abs(left[x]-right[x])
        x += 1

    return total_distance


def calculate_similarity_score(left, right):
    total = 0
    for l in left:
        total += l * right.count(l)

    return total


def get_input():
    with open('./input.txt', 'r') as input_file:
        left, right = [], []
        lines = [l.strip('\n').split() for l in input_file.readlines()]
        for l in lines:
            left += [int(l[0])]
            right += [int(l[1])]
    left.sort()
    right.sort()
    return left, right


def solve():
    l, r = get_input()
    print(determine_distance(l, r))
    print(calculate_similarity_score(l, r))


if __name__ == "__main__":
    solve()
