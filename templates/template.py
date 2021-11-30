

def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
    return lines


def solve():
    daily_input = get_input()
    print(daily_input)


if __name__ == "__main__":
    solve()