from copy import deepcopy


def get_input():
    instruction_set = []
    with open('./input.txt', 'r') as file:
        for op in file:
            instruction_set += [[op[:-1].split(' ')[0], int(op[:-1].split(' ')[1][1:]) if op[:-1].split(' ')[1][0] == 0 else int(op[:-1].split(' ')[1])]]
        return instruction_set


def iterator(pos=0, accumulator=0, shadow_instructions=None, instruction_set=None, jumper_finder=False, change_pos=0, second_iteration=False):
    if not shadow_instructions:
        shadow_instructions = deepcopy(instruction_set)
        for i in shadow_instructions:
            i += [0]

    try:
        op, value = instruction_set[pos]
    except IndexError:
        return True, accumulator

    if shadow_instructions[pos][2] == 1:
        if not jumper_finder:
            return accumulator
        else:
            return False, accumulator

    if op == 'nop':
        shadow_instructions[pos][2] += 1
        pos += 1
    elif op == 'acc':
        shadow_instructions[pos][2] += 1
        accumulator += value
        pos += 1
    elif op == 'jmp':
        shadow_instructions[pos][2] += 1
        pos += value
    else:
        pass

    return iterator(pos=pos, accumulator=accumulator, shadow_instructions=shadow_instructions, instruction_set=instruction_set, jumper_finder=jumper_finder, change_pos=change_pos, second_iteration=second_iteration)


def second_wrapper(instruction_set):
    second_iteration=False
    loop_broken = False
    change_pos = 0
    while not loop_broken:
        new_instructions = deepcopy(instruction_set)
        if change_pos > len(instruction_set)-1:
            print(instruction_set[len(new_instructions) - 1])
            change_pos = 0
            second_iteration = True
            continue
        if not second_iteration:
            if new_instructions[change_pos][0] == 'jmp':
                new_instructions[change_pos][0] = 'nop'
                print("Changing {} at pos {} to jmp".format(new_instructions[change_pos][0], change_pos))
        elif second_iteration:
            if new_instructions[change_pos][0] == 'nop':
                new_instructions[change_pos][0] = 'jmp'
                print("Changing {} at pos {} to nop".format(new_instructions[change_pos][0], change_pos))
        else:
            print("CRAP")
        change_pos += 1
        loop_broken, accumulator = iterator(instruction_set=new_instructions, jumper_finder=True)

    return accumulator


def solve():
    instructions = get_input()
    final_value = iterator(instruction_set=instructions)
    print("Loop is starting while accumulator at {}".format(final_value))
    second_final_value = second_wrapper(instruction_set=instructions)
    print("Program ran until accumulator at {}".format(second_final_value))


def main():
    solve()


if __name__ == "__main__":
    main()