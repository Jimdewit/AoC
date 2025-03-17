import re


def calculate_lcms(x: tuple, y: tuple):
    x_lcm = y_lcm = []
    for i in range(1,10):
        for i2 in range(1, 10):
            x_lcm += [(x[0]*i + x[1] * i2, i, i2)]
    for i in range(1,10):
        for i2 in range(1, 10):
            y_lcm += [(y[0]*i + y[1] * i2, i, i2)]

    return (x_lcm, y_lcm)


def process_lcms(lcms: tuple[list[int, int, int]], target: tuple[int, int]):
    x_target, y_target = target
    for lcm in lcms:
        x_lcms, y_lcms = lcm[0]
        for x in x_lcms:
            if x_target % x[0] == 0:
                pass


def part_one(inp):
    for i in inp:
        xs = i[0][0], i[1][0]
        ys = i[0][1], i[1][1]
        target_x = i[2][0]
        target_y = i[2][1]
        lcms = calculate_lcms(xs, ys)




def get_input():
    with open('./test_input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
    buttons = []
    button = []
    for l in lines:
        if len(l) == 0:
            buttons += [button]
            button = []
        button_a = re.findall(r'.?A: X\+(\d+), Y\+(\d+)', l)
        button_b = re.findall(r'.?B: X\+(\d+), Y\+(\d+)', l)
        target = re.findall(r'.?: X=(\d+), Y=(\d+)', l)
        if button_a:
            button += (button_a)
        if button_b:
            button += (button_b)
        if target:
            button += (target)

    return buttons


def solve():
    daily_input = get_input()
    print(daily_input)
    part_one(daily_input)


if __name__ == "__main__":
    solve()
