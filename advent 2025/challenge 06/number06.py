import re


def add(nums: list[int]) -> int:
    added = int(nums[0])
    for n in nums[1:]:
        added += int(n)
    print(f"Added outcome {added} for {nums}")
    return added


def mult(nums: list[int]) -> int:
    multed = int(nums[0])
    for n in nums[1:]:
        multed *= int(n)
    print(f"Multed outcome {multed} for {nums}")
    return multed


def process_instructions(inst: list):
    total = 0
    for i in inst:
        if i[-1] == '+':
            total += add(i[:-1])
        else:
            total += mult(i[:-1])

    print(f"Part one: {total}")


def parse_input_again(lines: list) -> list:
    parsed = []
    operands = re.findall(r'\+ +|\* +', lines[-1])
    instruction = []
    for idx, char in enumerate(lines[-1]):
        number = ''
        if char in ['+', '*']:
            if idx > 0:
                instruction.reverse()
                parsed.append(instruction[1:])
                instruction = []
            instruction.append(char)
        for l in lines:
            if l[idx] not in [' ', '+', '*']:
                number += l[idx]
        instruction.append(number)

    instruction.append(char)
    instruction.reverse()
    parsed.append(instruction[1:])
    
    parsed.reverse()
    
    return parsed


def get_input() -> (list, list):
    with open('./input.txt', 'r') as input_file:
        lines = [l for l in input_file.read().splitlines()]

    split_lines = []
    for i in lines:
        cnt = 0
        for elem in i.split():
            if lines.index(i) == 0:
                split = []
            else:
                split = split_lines[cnt]
            try:
                elem = int(elem)
            except:
                pass
            split.append(elem)
            if lines.index(i) == 0:
                split_lines.append(split)
            else:
                split_lines[cnt] = split

            cnt += 1

    proper_lines = parse_input_again(lines)

    return split_lines, proper_lines


def solve():
    daily_input, proper_input = get_input()
    process_instructions(daily_input)
    process_instructions(proper_input)


if __name__ == "__main__":
    solve()
