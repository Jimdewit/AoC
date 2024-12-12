import copy


class Coord:
    def __init__(self, x: int, y: int, char: str):
        self.x = x
        self.y = y
        self.char = char


def find_matches(char: str, antennaes: list[list[Coord]]) -> list:
    found = []
    for y in antennaes:
        found += [x for x in y if x.char == char]

    return found


def apply_translations(first: Coord, second: Coord, x_dist: int, y_dist: int, antinode_chart: [list[list[Coord]]], max_x: int, max_y: int, solve_two=False, recurse_depth=0):
    mirror_first = mirror_second = Coord(0, 0, '')

    if recurse_depth == 0 and solve_two:
        antinode_chart[first.y][first.x] = '#'
        antinode_chart[second.y][second.x] = '#'

    mirror_second.x = first.x + x_dist
    mirror_first.x = second.x - x_dist
    mirror_second.y = first.y + y_dist
    mirror_first.y = second.y - y_dist

    for c in [mirror_first, mirror_second]:
        if not 0 <= c.x < max_x:
            continue
        if not 0 <= c.y < max_y:
            continue

        c.char = "#"

        antinode_chart[c.y][c.x] = c.char

    if ((mirror_first.x > max_x or mirror_first.x < 0) and
            (mirror_second.x > max_x or mirror_second.x < 0) and
            (mirror_first.y > max_y or mirror_first.y < 0) and
            (mirror_second.y > max_y or mirror_second.y < 0)) or not solve_two:
        # for y in antinode_chart:
        #     print(''.join(list(x.char if type(x) == Coord else x for x in y)))
        return
    else:
        return apply_translations(mirror_first, mirror_second, x_dist, y_dist, antinode_chart, max_x, max_y, solve_two=solve_two, recurse_depth=recurse_depth+1)


def process_match(first: Coord, second: Coord, antinode_chart: list[list[Coord]], solve_two=False):
    max_x = len(antinode_chart[0])
    max_y = len(antinode_chart)
    if first == second:
        return
    x_dist = first.x - second.x
    y_dist = first.y - second.y
    # mirror

    apply_translations(first, second, x_dist, y_dist, antinode_chart, max_x, max_y, solve_two=solve_two)


def count_matches(antinode_chart: [list[list[Coord]]]):
    antinodes_found = 0
    for y in antinode_chart:
        print(''.join(list(x.char if type(x) == Coord else x for x in y)))
        antinodes_found += y.count("#")
    print(f"Found {antinodes_found} antinodes")


def solve(antennae: list[list[Coord]], solve_two=False):
    antinode_chart = copy.deepcopy(antennae)
    for row in antennae:
        for col in row:
            if col.char != '.':
                matches = find_matches(col.char, antennae)
                for m in matches:
                    process_match(col, m, antinode_chart, solve_two=solve_two)
    count_matches(antinode_chart)


def get_input() -> list:
    with open('./test_input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]

    antennae_map = []
    y = 0
    for l in lines:
        antennae_map += [[]]
        x = 0
        for c in l:
            antennae_map[y] += [Coord(x, y, c)]
            x += 1
        y += 1

    return antennae_map


def process():
    daily_input = get_input()
    print(daily_input)
    solve(daily_input, solve_two=False)
    solve(daily_input, solve_two=True)


if __name__ == "__main__":
    process()
