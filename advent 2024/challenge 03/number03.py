import re


def process_instructions(instruction_set):
    res = sum([int(x) * int(y) for x, y in instruction_set if x and y])

    return res


def part_two():
    with open("./input.txt") as f:
        line = "".join(x.strip() for x in f)
    pattern = r"mul\((\d{1,3}),(\d{1,3})\)|(do\(\))|(don't\(\))"
    res = 0
    enabled = True
    for a, b, c, d in re.findall(pattern, line):
        if len(d) > 0:
            enabled = False
        elif len(c) > 0:
            enabled = True
        elif enabled:
            res += int(a) * int(b)
    print(res)


def get_input(with_do=False):
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]

    mul_regex = re.compile('mul\((\d{1,3}),(\d{1,3})\)')
    mult_instructions = []
    for l in lines:
        if with_do:
            # l = re.sub(r"don't\(\).*?do\(\)", "", l, flags=re.DOTALL)
            # l = re.sub(r"don't\(\).*", "", l, flags=re.DOTALL)
            print(l)
            mult_instructions += re.findall(r"(?:don't\(\).*?do\(\))|mul\((\d{1,3}),(\d{1,3})\)", l)
        else:
            mult_instructions += re.findall(mul_regex, l)
    print(mult_instructions)
    return mult_instructions


def solve():
    daily_input = get_input()
    print(process_instructions(daily_input))
    part_two()


if __name__ == "__main__":
    solve()
