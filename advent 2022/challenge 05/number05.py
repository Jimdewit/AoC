import copy
import re


def process_movement(stacks, instructions, process_multiple=False):
    stacks = copy.deepcopy(stacks)
    # An instruction consists of AMOUNT, SOURCE_STACK, TARGET_STACK
    for instruction in instructions:
        amount = instruction[0]
        source_stack = instruction[1]
        target_stack = instruction[2]
        if process_multiple:
            stacks[target_stack] += stacks[source_stack][-amount:]
            del stacks[source_stack][-amount:]
        else:
            for x in range(1, amount+1):
                stacks[target_stack] += stacks[source_stack].pop()

    code = ''
    for x in range(1, len(stacks.keys())+1):
        code += stacks[x][-1]
    return code


def get_input():
    with open('./input.txt', 'r') as input_file:
        stacks = {}
        instructions = []
        lines = [l.strip('\n') for l in input_file.readlines()]
        item_pattern = re.compile('([A-Z])+')
        instruction_pattern = re.compile('move (\d+) from (\d+) to (\d+)')
        for line in lines:

            item_groups = item_pattern.finditer(line)

            for item in item_groups:
                item_pos = int((item.span()[1]+2)/4)
                item_to_append = line[item.span()[0]]
                stacks.setdefault(item_pos, []).append(item_to_append)

            instruction_groups = instruction_pattern.findall(line)
            if instruction_groups:
                instructions.append(tuple(int(x) for x in instruction_groups[0]))

        # Reverse the stacks so we can append and pop to/from the end
        for stack in stacks:
            stacks[stack].reverse()

    return stacks, instructions


def solve():
    stacks, instructions = get_input()
    print("Single stacking: {}".format(process_movement(stacks, instructions)))
    print("Multiple stacking: {}".format(process_movement(stacks, instructions, process_multiple=True)))


if __name__ == "__main__":
    solve()
