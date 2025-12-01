def process_instructions(inp: list[str]):
    dial = 50
    zeroes_end = 0
    zeroes_seen = 0
    for i in inp:
        side, amt = i[0], int(i[1:])
        diff = range(dial if side == 'R' else dial, dial + amt+1 if side == 'R' else dial-amt-1, 1 if side == 'R' else -1)
        zeroes_seen += len([x for x in diff if x % 100 == 0])
        dial += amt if side == 'R' else -amt

        if dial % 100 == 0:
            zeroes_end += 1
            zeroes_seen -= 1
    print(zeroes_end)
    print(zeroes_seen)


def get_input() -> list:
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
    return lines


def solve():
    daily_input = get_input()
    process_instructions(daily_input)


if __name__ == "__main__":
    solve()
