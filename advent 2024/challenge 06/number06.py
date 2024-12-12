import copy


class Coord:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def find_next_pos(direction: int, current_pos: Coord) -> Coord:
    if direction == 0:
        return Coord(current_pos.x, current_pos.y-1)
    if direction == 1:
        return Coord(current_pos.x+1, current_pos.y)
    if direction == 2:
        return Coord(current_pos.x, current_pos.y+1)
    if direction == 3:
        return Coord(current_pos.x-1, current_pos.y)


def is_loop(pos, direction, empty_map):
    loop_route = copy.deepcopy(empty_map)
    # 0 = UP, 1 = RIGHT, 2 = DOWN, 3 = RIGHT
    seen = 0
    needed = len(empty_map)*len(empty_map[0])*10
    press_pos = find_next_pos(direction, pos)
    direction = direction + 1 if direction < 3 else 0
    seen_once_already = False

    loop_route[press_pos.y][press_pos.x] = 'O'

    while True:
        if seen >= needed:
            return False
        next_pos = find_next_pos(direction, pos)
        try:
            next_pos_value = loop_route[next_pos.y][next_pos.x]
        except IndexError:
            break
        if next_pos_value == 'O':
            if seen_once_already:
                return True
            seen_once_already = True
        if next_pos_value not in ['#', 'O']:
            loop_route[next_pos.y][next_pos.x] = 'X'
            pos = next_pos
        else:
            direction = direction + 1 if direction < 3 else 0
        seen += 1


def process_route(empty_map: list, pos: Coord, needed=0, solve_two=False):
    route_taken = copy.deepcopy(empty_map)
    # 0 = UP, 1 = RIGHT, 2 = DOWN, 3 = RIGHT
    direction = 0
    loop_positions =0
    seen = 0
    while True:
        seen += 1
        if solve_two:
            print(f'Processing {seen}/{needed}')
        next_pos = find_next_pos(direction, pos)
        try:
            next_pos_value = empty_map[next_pos.y][next_pos.x]
        except IndexError:
            break
        if next_pos_value != '#':
            route_taken[next_pos.y][next_pos.x] = 'X'
            if solve_two:
                potential_press_position = find_next_pos(direction, next_pos)
                if potential_press_position.y > len(empty_map)-1 or potential_press_position.x > len(empty_map[0])-1:
                    pos = next_pos
                    continue
                current_next_value = route_taken[potential_press_position.y][potential_press_position.x]
                route_taken[potential_press_position.y][potential_press_position.x] = 'O'
                if is_loop(next_pos, direction, empty_map):
                    loop_positions += 1
                route_taken[potential_press_position.y][potential_press_position.x] = current_next_value

            pos = next_pos

        else:
            direction = direction + 1 if direction < 3 else 0

    for y in range(len(route_taken)):
        print(route_taken[y])

    poses_seen = 0
    for y in range(len(route_taken)):
        poses_seen += len([x for x in route_taken[y] if x == 'X'])

    print(f'Visited: {poses_seen}')
    if solve_two:
        print(f'Press positions: {loop_positions}')
    return poses_seen


def get_input() -> ([], Coord):
    empty_map = []
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]

    for l in lines:
        l = [ch for ch in l]
        empty_map += [l]
        if '^' in l:
            starting_pos = Coord(l.index('^'), len(empty_map)-1)

    return tuple(empty_map), starting_pos


def solve():
    empty_map, starting_pos = get_input()
    visited = process_route(empty_map, starting_pos)
    process_route(empty_map, starting_pos, visited, solve_two=True)


if __name__ == "__main__":
    solve()
