
def find_adjacent(x, y, height_map):
    try:
        above = [height_map[y-1][x][0], x, y]
    except (KeyError, IndexError):
        above = 10
    try:
        below = [height_map[y+1][x][0], x, y+1]
    except (KeyError, IndexError):
        below = 10
    try:
        left = [height_map[y][x-1][0] if x-1 >= 0 else 10, x-1, y]
    except (KeyError, IndexError):
        left = 10
    try:
        right = [height_map[y][x+1][0], x+1, y]
    except (KeyError, IndexError):
        right = 10

    return [above, below, left, right]


def is_height_lowest(height, neighbours):
    for neighbour in neighbours:
        if isinstance(neighbour, list):
            neighbour = neighbour[0]
        if height >= neighbour:
            return False
    return True


def score_heights(height_map):
    risk_counter = 0
    for y in height_map.keys():
        for single_height in height_map[y]:
            height, x = single_height[0], single_height[1]
            adjacent_numbers = find_adjacent(x, y, height_map)
            if is_height_lowest(height, adjacent_numbers):
                risk_counter += (height + 1)
    return risk_counter


def parse_single_basin(key, key_list, basin_map):
    k, x, y = key
    find_adjacent(x, y, basin_map)


def height_has_lower_neighbour(height, neighbours):
    lower_neighbours = []
    for neighbour in neighbours:
        if not isinstance(neighbour, list):
            continue
        else:
            if height < neighbour[0]:
                lower_neighbours += [neighbour]
    return lower_neighbours


def parse_heights(height_map, basins_found):
    for y in height_map.keys():
        print('Height map start: {}'.format(height_map[y]))
        height_adjacents = {}
        for single_height in height_map[y]:
            height_adjacents[y] = []
            height, x = single_height[0], single_height[1]
            adjacent_numbers = find_adjacent(x, y, height_map)
            next_to_check = []
            height_adjacents[y] += [[h, hx] for h, hx, hy in [single_height for single_height in height_has_lower_neighbour(height, adjacent_numbers)]]
            print('Removing single height {}'.format(single_height))
            height_map[y].pop(height_map[y].index(single_height))

        print('Height map finis: {}'.format(height_map[y]))
    return height_map


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
        line_counter = 0
        line_dict = {}
        for l in lines:
            line_dict[line_counter] = []
            pos = 0
            for x in l:
                line_dict[line_counter] += [[int(x), pos]]
                pos += 1
            line_counter += 1
    return line_dict


def solve():
    daily_input = get_input()
    print('Total risk equals {}'.format(score_heights(daily_input)))
    parse_heights(daily_input, None)


if __name__ == "__main__":
    solve()
