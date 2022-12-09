def translate_tail(head_positions, tail_positions):
    head_pos = head_positions[-1]
    tail_pos = tail_positions[-1]
    head_x, head_y = head_pos[0], head_pos[1]
    tail_x, tail_y = tail_pos[0], tail_pos[1]
    if abs(head_x - tail_x) <= 1 and abs(head_y - tail_y) <= 1:
        return tail_positions
    else:
        tail_positions.append(head_positions[-2])
        return tail_positions


def translate_x(amount, head_positions, tail_positions, step):
    start_x = head_positions[-1][0]
    start_y = head_positions[-1][1]
    for x in range(start_x+step, start_x+amount, step):
        head_positions.append((x, start_y))
        tail_positions = translate_tail(head_positions, tail_positions)
    return head_positions, tail_positions


def translate_y(amount, head_positions, tail_positions, step):
    start_x = head_positions[-1][0]
    start_y = head_positions[-1][1]
    for y in range(start_y+step, start_y+amount, step):
        head_positions.append((start_x, y))
        tail_positions = translate_tail(head_positions, tail_positions)
    return head_positions, tail_positions


def translate_head(translation, head_positions, tail_positions):
    direction = translation[0]
    amount = int(translation[1])
    if direction == 'U':
        head_positions, tail_positions = translate_y(amount+1, head_positions, tail_positions, 1)
    if direction == 'D':
        head_positions, tail_positions = translate_y(-(amount+1), head_positions, tail_positions, -1)
    if direction == 'L':
        head_positions, tail_positions = translate_x(-(amount+1), head_positions, tail_positions, -1)
    if direction == 'R':
        head_positions, tail_positions = translate_x(amount+1, head_positions, tail_positions, 1)

    return head_positions, tail_positions


def process_instructions(instruction_set):
    head_positions = [(0, 0)]
    tail_positions = [(0, 0)]
    for translation in instruction_set:
        head_positions, tail_positions = translate_head(translation, head_positions, tail_positions)
    print(len(set(tail_positions)))


def get_input():
    with open('./input.txt', 'r') as input_file:
        instructions = []
        lines = [l.strip('\n') for l in input_file.readlines()]
        for l in lines:
            instructions.append(tuple(i for i in l.split()))
    return instructions


def solve():
    instruction_set = get_input()
    process_instructions(instruction_set)


if __name__ == "__main__":
    solve()
