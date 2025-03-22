def is_turd(char):
    return char == '💩'


def find_poos(inp):
    x = 0
    poos = 0
    for y in range(len(inp)):
        #print(inp[y][x])
        print(f"checking line {y} {inp[y]} with x at {x} and length {len(inp[y])}")
        if is_turd(inp[y][x]):
            print(f"found shit at {y},{x}")
            poos += 1

        if y < len(inp)-1:
            x = (x + 2) % len(inp[y])
    print(poos)


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
    return lines


def solve():
    daily_input = get_input()
    find_poos(daily_input)


if __name__ == "__main__":
    solve()
