

def translate(axis, translation, aim=None, use_aim=False):
    if not use_aim:
        axis += translation
    else:
        axis += (translation * aim)
    return axis


def parse_instructions(puzzle_input, use_aim=False):
    x = 0
    z = 0
    aim = 0
    for instruction, translation in puzzle_input:
        if not use_aim:
            if instruction == 'forward':
                x = translate(x, translation)
            elif instruction == 'down':
                z = translate(z, translation)
            elif instruction == 'up':
                z = translate(z, -translation)
        else:
            if instruction == 'forward':
                x = translate(x, translation)
                z = translate(z, translation, aim, use_aim=use_aim)
            elif instruction == 'down':
                aim = translate(aim, translation)
            elif instruction == 'up':
                aim = translate(aim, -translation)
    return x, z


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [[x, int(y)] for x, y in (l.strip('\n').split(' ') for l in input_file.readlines())]
    return lines


def solve():
    daily_input = get_input()
    forward, depth = parse_instructions(daily_input)
    print(forward * depth)
    forward, depth = parse_instructions(daily_input, use_aim=True)
    print(forward * depth)


if __name__ == "__main__":
    solve()