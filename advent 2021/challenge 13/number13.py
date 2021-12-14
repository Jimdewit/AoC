import copy

import numpy as np


def process_fold(star_map, folding_instructions, full_sum=False):
    for fold in folding_instructions:
        if fold[0] == 'x':
            fold_along = int(fold[2:])
            max_x = star_map.shape[1]
            fold_range = [int(x) for x in range(fold_along, max_x)]
            fold_range.reverse()
            temp_map = copy.deepcopy(star_map)
            for x in fold_range:
                for y in range(star_map.shape[0]):
                    if star_map[y][x] == 1:
                        fold_x = x - fold_along
                        temp_map[y][fold_along - fold_x] = 1
            temp_map = np.delete(temp_map, fold_range, axis=1)
            star_map = temp_map
        else:
            fold_along = int(fold[2:])
            max_y = star_map.shape[0]
            fold_range = [int(x) for x in range(fold_along, max_y)]
            fold_range.reverse()
            temp_map = copy.deepcopy(star_map)
            for y in fold_range:
                for x in range(star_map.shape[1]):
                    if temp_map[y][x] == 1:
                        fold_y = y - fold_along
                        temp_map[fold_along - fold_y][x] = 1

            temp_map = np.delete(temp_map, fold_range, axis=0)
            star_map = temp_map

        if not full_sum:
            return sum(sum(s for s in star_map))

    return star_map


def get_input():
    with open('./input.txt', 'r') as input_file:
        folding = []
        star_coords = []
        for line in input_file.readlines():
            if line.startswith('fold'):
                folding += [line.strip('\n').split()[-1]]
            elif line == '\n':
                continue
            else:
                x, y = line.strip('\n').split(',')
                star_coords += [[int(x), int(y)]]
        max_x = max([x[0] for x in star_coords]) + 1  # Increase by one because of range() behaviour
        max_y = max([x[1] for x in star_coords]) + 1  # Increase by one because of range() behaviour

        star_map = np.zeros((max_y, max_x), np.int8)
        for star in star_coords:
            x, y = star
            star_map[y][x] = 1
    return star_map, folding


def solve():
    star_map, instructions = get_input()
    single_sum = process_fold(star_map, instructions)
    print('Sum after 1 fold: {}'.format(single_sum))
    star_map, instructions = get_input()
    final_map = process_fold(star_map, instructions, full_sum=True)
    print('Eventually stuff looks like:\n{}'.format(final_map))


if __name__ == "__main__":
    solve()
