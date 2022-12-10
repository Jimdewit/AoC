from math import ceil

debug = False

def translate_tail(head_positions, tail_positions):
    head_pos = head_positions[-1]
    tail_pos = tail_positions[-1]
    head_x, head_y = head_pos[0], head_pos[1]
    tail_x, tail_y = tail_pos[0], tail_pos[1]
    if debug:
        print('Comparing {} and {}'.format(head_pos, tail_pos))
    if abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1:
        if debug:
            print('No tail adjustment needed')
        tail_positions.append(tail_pos)
        return tail_positions
    else:
        dx = ceil((head_x - tail_x) / 2) if head_x > tail_x else -ceil((tail_x - head_x) /2)
        dy = ceil((head_y - tail_y) / 2) if head_y > tail_y else -ceil((tail_y - head_y) /2)
        new_tail_pos = int(tail_x+dx), int(tail_y+dy)
        if debug:
            print('Moving tail {} to {}'.format(tail_pos, new_tail_pos))
        tail_positions.append(new_tail_pos)
        return tail_positions


def translate_x(amount, head_positions, tails, step):
    if debug:
        print('translating {} over x, heads at {}'.format(amount, head_positions))
    start_x = head_positions[-1][0]
    start_y = head_positions[-1][1]
    for x in range(start_x+step, start_x+amount, step):
        head_positions.append((x, start_y))
        new_tails = [translate_tail(head_positions, tails[0])]
        if len(tails) > 1:
            for tail_positions in tails[1:]:
                new_tails.append(translate_tail(new_tails[tails.index(tail_positions) - 1], tail_positions))
    return head_positions, new_tails


def translate_y(amount, head_positions, tails, step):
    if debug:
        print('translating {} over y, heads at {}'.format(amount, head_positions))
    start_x = head_positions[-1][0]
    start_y = head_positions[-1][1]
    for y in range(start_y+step, start_y+amount, step):
        head_positions.append((start_x, y))
        new_tails = [translate_tail(head_positions, tails[0])]
        if len(tails) > 1:
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


def process_instructions(instruction_set, tail_size):
    head_positions = [(0, 0)]
    tails = [[(0, 0)] for x in range(0,tail_size)]
    for translation in instruction_set:
        head_positions, tails = translate_head(translation, head_positions, tails)
        if debug:
            print('Finished translation, heads at {} tail at {}'.format(head_positions, tails))
            print('Number of tails: {}'.format(len(tails)))
    print(len(set(tails[-1])))


def get_input():
    with open('input.txt', 'r') as input_file:
        instructions = []
        lines = [l.strip('\n') for l in input_file.readlines()]
        for l in lines:
            instructions.append(tuple(i for i in l.split()))
    return instructions


def solve():
    instruction_set = get_input()
    process_instructions(instruction_set, 1)
    process_instructions(instruction_set, 9)


if __name__ == "__main__":
    solve()
