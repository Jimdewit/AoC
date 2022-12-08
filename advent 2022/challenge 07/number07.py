import copy
from functools import reduce
import operator
import re


def sum_values(target_dict, cutoff_value):
    total = 0
    for key, value in target_dict.items():
        if isinstance(value, int):
            if value <= cutoff_value:
                total += value
        if isinstance(value, dict):
            total += sum_values(value, cutoff_value)
    return total


def find_deletion_candidates(target_dict, cutoff_value):
    candidates = []
    for key, value in target_dict.items():
        if isinstance(value, int):
            if value >= cutoff_value:
                candidates += [value]
        if isinstance(value, dict):
            candidates += find_deletion_candidates(value, cutoff_value)
    return candidates


def directory_to_delete(directory_structure, minimal_free, max_disk_space=70000000):
    total_size = directory_structure['/']['size']
    print('Currently in use: {}, will need: {}'.format(total_size, (minimal_free + total_size) - max_disk_space))
    needed = (minimal_free + total_size) - max_disk_space
    deletion_candidates = find_deletion_candidates(directory_structure, needed)
    return min(x for x in deletion_candidates)


def get_from_dict(target_dict, key_list):
    return reduce(operator.getitem, key_list, target_dict)


def set_in_dict(target_dict, key_list: list, value):
    get_from_dict(target_dict, key_list[:-1])[key_list[-1]] = value


def build_directory_structure(terminal_output):
    tree_dict = {'/':{}} # Instantiate first directory to prevent KeyErrors
    working_dir = []
    for line in terminal_output:
        if re.match('\$ cd \.\.', line):
            working_dir.pop()
        if re.match('\$ cd ([a-z]|/)+', line):
            working_dir += [line.split()[2]]
        if re.match('\$ ls', line):
            continue
        if re.match('dir \w', line):
            set_in_dict(tree_dict, working_dir+[line.split()[1]], {})
        if re.match('\d+', line.split()[0]):
            working_dir_copy = copy.deepcopy(working_dir)
            for x in range(0, len(working_dir)):
                current_size = get_from_dict(tree_dict, working_dir_copy).get('size', 0)
                set_in_dict(tree_dict, working_dir_copy+['size'], current_size + int(line.split()[0]))
                working_dir_copy.pop()
    return tree_dict



def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
    return lines


def solve():
    terminal_output = get_input()
    directory_structure = build_directory_structure(terminal_output)
    print('Total size of directories under {}: {}'.format(100000, sum_values(directory_structure, cutoff_value=100000)))
    print('Smallest deletable directory containing enough space: {}'.format(
        directory_to_delete(directory_structure, minimal_free=30000000)))

if __name__ == "__main__":
    solve()
