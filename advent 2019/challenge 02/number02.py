def iterator(input_list, starting_pos=0):
    positions = input_list[starting_pos:starting_pos+4]
    if positions[0] == 1:
        input_list[positions[3]] = input_list[positions[1]] + input_list[positions[2]]
    if positions[0] == 2:
        input_list[positions[3]] = input_list[positions[1]] * input_list[positions[2]]

    if positions[0] == 99 or starting_pos + 3 >= len(input_list):
        return input_list

    return iterator(input_list, starting_pos+4)


def input_wrapper(code, puzzle_part):
    if puzzle_part == 1:
        code[1] = 12
        code[2] = 2
        return iterator(code)

    for noun in range(100):
        for verb in range(100):
            code = get_input()
            code[1] = noun
            code[2] = verb
            outcome = iterator(code)[0]
            if outcome == 19690720:
                return noun * 100 + verb


def get_input():
    with open('./input.txt', 'r') as inputfile:
        return [int(x) for x in inputfile.readline().rstrip('\n').split(',')]


def main():
    code = get_input()

    print("Input: {}".format(code))
    print("Final outcome: {}".format(input_wrapper(code, 1)[0]))
    print("Final final outcome: {}".format(input_wrapper(code, 2)))


if __name__ == "__main__":
    main()