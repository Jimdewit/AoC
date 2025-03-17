
def is_valid_sms(inp):
    return len(inp.encode('utf-8')) <= 160


def is_valid_tweet(inp):
    return len(inp) <= 140


def get_costs(inp):
    if is_valid_sms(inp):
        if is_valid_tweet(inp):
            return 13
        return 11
    if is_valid_tweet(inp):
        return 7
    return 0


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
    return lines


def solve():
    daily_input = get_input()
    costs = 0
    for i in daily_input:
        costs += get_costs(i)
    print(costs)


if __name__ == "__main__":
    solve()
