def translate_tail(head_positions, tail_positions):
    head_pos = head_positions[-1]
    tail_pos = tail_positions[-1]
    head_x, head_y = head_pos[0], head_pos[1]
    tail_x, tail_y = tail_pos[0], tail_pos[1]
    print('Comparing {} and {}'.format(head_pos, tail_pos))
    if abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1:
        # print('No tail adjustment needed')
        return tail_positions
    else:
        print('Moving tail {} to {}'.format(tail_pos, head_positions[-2]))
        tail_positions.append(head_positions[-2])
        return tail_positions


def translate_x(amount, head_positions, tails, step):
    print('translating {} over x, heads at {}'.format(amount, head_positions))
    start_x = head_positions[-1][0]
    start_y = head_positions[-1][1]
    for x in range(start_x+step, start_x+amount, step):
        head_positions.append((x, start_y))
        new_tails = [translate_tail(head_positions, tails[0])]
        for tail_positions in tails[1:]:
            new_tails.append(translate_tail(new_tails[tails.index(tail_positions) - 1], tail_positions))
    return head_positions, new_tails


def translate_y(amount, head_positions, tails, step):
    print('translating {} over y, heads at {}'.format(amount, head_positions))
    start_x = head_positions[-1][0]
    start_y = head_positions[-1][1]
    for y in range(start_y+step, start_y+amount, step):
        head_positions.append((start_x, y))
        new_tails = [translate_tail(head_positions, tails[0])]
        for tail_positions in tails[1:]:
            new_tails.append(translate_tail(new_tails[tails.index(tail_positions)-1], tail_positions))
    return head_positions, new_tails


def translate_head(translation, head_positions, tails):
    direction = translation[0]
    amount = int(translation[1])
    if direction == 'U':
        head_positions, tails = translate_y(amount+1, head_positions, tails, 1)
    if direction == 'D':
        head_positions, tails = translate_y(-(amount+1), head_positions, tails, -1)
    if direction == 'L':
        head_positions, tails = translate_x(-(amount+1), head_positions, tails, -1)
    if direction == 'R':
        head_positions, tails = translate_x(amount+1, head_positions, tails, 1)

    return head_positions, tails


def process_instructions(instruction_set):
    head_positions = [(0, 0)]
    tails = [[(0, 0)] for x in range(0,9)]
    print(tails)
    for translation in instruction_set:
        head_positions, tails = translate_head(translation, head_positions, tails)
        print('Finished translation, heads at {} tail at {}'.format(head_positions, tails))
    print(len(set(tails[-1])))

def get_input():
    with open('test_input_part2.txt', 'r') as input_file:
        instructions = []
        lines = [l.strip('\n') for l in input_file.readlines()]
        for l in lines:
            instructions.append(tuple(i for i in l.split()))
    print(instructions)
    return instructions


def solve():
    instruction_set = get_input()

    process_instructions(instruction_set)


if __name__ == "__main__":
    solve()
