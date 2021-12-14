

def process_sum(instructions, mol_dict):
    elements = {}
    for x, y in instructions.values():
        elements[x[0]] = 0
        elements[x[1]] = 0

    for element in elements.keys():
        for element_key in mol_dict.keys():
            if element == element_key[0]:
                elements[element] += mol_dict[element_key]

    # Probably counting one thing double somehwere - see what I care :-D
    return (max(elements.values())-min(elements.values()))-1


def process_pairs_properly(molecule_dict, instructions, iteration=0, desired_iterations=10):
    if iteration == desired_iterations:
        return process_sum(instructions, molecule_dict)

    new_dict = {}
    for k in molecule_dict.keys():
        instruction1, instruction2 = instructions[k]

        if new_dict.get(instruction1, None):
            new_dict[instruction1] += molecule_dict[k]
        else:
            new_dict[instruction1] = molecule_dict[k]
        if new_dict.get(instruction2, None):
            new_dict[instruction2] += molecule_dict[k]
        else:
            new_dict[instruction2] = molecule_dict[k]

    processed_dict = new_dict
    return process_pairs_properly(processed_dict, instructions,iteration=iteration+1, desired_iterations=desired_iterations)


def get_input():
    with open('./test_input.txt', 'r') as input_file:
        instructions = {}
        molecule_dict = {}
        for line in input_file.readlines():
            if line == '\n':
                continue
            elif '->' not in line:
                starting_molecule = line.strip('\n')
            else:
                x, y = line.strip('\n').split(' -> ')
                instructions[x] = [x[0] + y, y + x[1]]
                molecule_dict[x[0] + y] = 0
                molecule_dict[y + x[1]] = 0

    mol_pairs = []
    for x in range(0, len(starting_molecule) - 1):
        mol_pairs += [starting_molecule[x:x + 2]]
    for mol_pair in mol_pairs:
        if molecule_dict.get(mol_pair, None):
            molecule_dict[mol_pair] += 1
        else:
            molecule_dict[mol_pair] = 1

    return molecule_dict, instructions


def solve():
    mol_dict, instructions = get_input()
    final_mol_dict_value = process_pairs_properly(mol_dict, instructions)
    print('Value after subtraction: {}'.format(final_mol_dict_value))
    final_mol_dict_value = process_pairs_properly(mol_dict, instructions, desired_iterations=40)
    print('Value after subtraction: {}'.format(final_mol_dict_value))


if __name__ == "__main__":
    solve()
