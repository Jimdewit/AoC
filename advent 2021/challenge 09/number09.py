import numpy


def find_neighbour_coords(i, j, shape_h, shape_v):
    print("H {} V {}".format(shape_h, shape_v))
    left = [i-1, j] if i-1 >= 0 else None
    right = [i+1, j] if i+1 < shape_h else None
    above = [i, j-1] if j-1 >= 0 else None
    below = [i, j+1] if j+1 < shape_v else None
    print(left, right, above, below)
    return [left, right, above, below]


def find_adjacents(x, y, height_map, processed=[]):
    neighbours = []
    neighbour_coords = find_neighbour_coords(x, y, height_map.shape[0]-1, height_map.shape[1]-1)
    for coord in neighbour_coords:
        if coord and coord not in processed:
            neighbours += [height_map[coord[0]][coord[1]]]
            processed += [[coord[0],coord[1]]]
        else:
            neighbours += [10]

    return neighbours, processed


def is_height_lowest(height, neighbours):
    for neighbour in neighbours:
        if isinstance(neighbour, list):
            neighbour = neighbour[0]
        if height >= neighbour:
            return False
    return True


def is_height_highest(height, neighbours):
    return [n for n in neighbours if height < n]


def score_heights(height_map):
    risk_counter = 0
    for x in range(height_map.shape[0]):
        for y in range(height_map.shape[1]):
            height = height_map[x, y]
            adjacent_numbers, processed = find_adjacents(x, y, height_map)
            print(adjacent_numbers)
            if is_height_lowest(height, adjacent_numbers):
                risk_counter += (height + 1)
    return risk_counter


def find_basins(height_map):
    for x in range(height_map.shape[0]):
        for y in range(height_map.shape[1]):
            height = height_map[x, y]
            adjacent_numbers = find_adjacents(x, y, height_map)
            # if is_height_highest()
    print(1)


def get_input():
    with open('./test_input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
        height_list = []
        for l in lines:
            single_line = []
            for x in l:
                single_line += [int(x)]
            height_list += [single_line]
    return numpy.array(height_list)


def solve():
    daily_input = get_input()
    print('Total risk equals {}'.format(score_heights(daily_input)))
    # score_heights(daily_input, find_basins=True)


if __name__ == "__main__":
    solve()