def iterator(input_list, starting_pos=0):
    positions = input_list[starting_pos:starting_pos+4]
    if positions[0] == 1:
        input_list[positions[3]] = input_list[positions[1]] + input_list[positions[2]]
    if positions[0] == 2:
        input_list[positions[3]] = input_list[positions[1]] * input_list[positions[2]]

    if positions[0] == 99 or starting_pos + 4 >= len(input_list):
        print("Got output: {}".format(input_list))
        return input_list

    return iterator(input_list, starting_pos+4)


def get_input():
    with open('./input.txt', 'r') as inputfile:
        return [int(x) for x in inputfile.readline().rstrip('\n').split(',')]


def main():
    code = get_input()
    code[1] = 12
    code[2] = 2
    print("Input: {}".format(code))
    print("Final outcome: {}".format(iterator(code)[0]))


if __name__ == "__main__":
    main()