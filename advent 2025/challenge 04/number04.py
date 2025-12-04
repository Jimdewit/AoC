import copy


class Floorspot:
    def __init__(self, value: str, coords: tuple[int, int]):
        self._coords = coords
        self._value = value
        self._neighbours: int = 0

    @property
    def coords(self):
        return self._coords

    @property
    def x(self):
        return self._coords[1]

    @property
    def y(self):
        return self._coords[0]

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_val):
        assert isinstance(new_val, str)
        self._value = new_val

    @property
    def neighbours(self):
        return self._neighbours

    def add_neighbour(self):
        self._neighbours += 1

    def reset_neighbours(self):
        self._neighbours = 0


def has_roll(direction: str, roll: Floorspot, floor_map: list[list[Floorspot]]) -> bool:
    if direction == 'n':
        return floor_map[roll.y-1][roll.x].value != '.' if roll.y > 0 else False
    if direction == 'ne':
        return floor_map[roll.y-1][roll.x+1].value != '.' if roll.y > 0 and roll.x < len(floor_map[0]) else False
    if direction == 'e':
        return floor_map[roll.y][roll.x+1].value != '.' if roll.x < len(floor_map[0]) else False
    if direction == 'se':
        return floor_map[roll.y+1][roll.x+1].value != '.' if roll.y < len(floor_map) and roll.x < len(floor_map[0]) else False
    if direction == 's':
        return floor_map[roll.y+1][roll.x].value != '.' if roll.y < len(floor_map) else False
    if direction == 'sw':
        return floor_map[roll.y+1][roll.x-1].value != '.' if roll.y < len(floor_map) and roll.x > 0 else False
    if direction == 'w':
        return floor_map[roll.y][roll.x-1].value != '.' if roll.x > 0 else False
    if direction == 'nw':
        return floor_map[roll.y-1][roll.x-1].value != '.'if roll.y > 0 and roll.x > 0 else False
    raise


def find_neighbours(roll: Floorspot, floor_map: list[list[Floorspot]]):
    for direction in ['n', 'ne', 'e', 'se', 's', 'sw', 'w', 'nw']:
        try:
            if has_roll(direction, roll, floor_map):
                roll.add_neighbour()
        except IndexError:
            continue
        except Exception as e:
            print(f"Got weird thing {e}, it's probably nothing!")


def process_floor_map_part_one(floor_map: list[list[Floorspot]]):
    accessible = 0
    for y in range(len(floor_map)):
        for x in range(len(floor_map[y])):
            floorspot = floor_map[y][x]
            if floorspot.value == '.':
                continue
            find_neighbours(floorspot, floor_map)
            if floorspot.neighbours < 4:
                accessible += 1
    print(f"Part two - Can reach: {accessible}")


def process_floor_map_part_two(floor_map: list[list[Floorspot]]):
    total_removed = 0
    final_try = False
    while True:
        removed = 0
        for y in range(len(floor_map)):
            for x in range(len(floor_map[y])):
                floorspot = floor_map[y][x]
                if floorspot.value == '.':
                    continue
                if floorspot.value == 'X':
                    floorspot.value = '.'
                    continue
                floorspot.reset_neighbours()
                find_neighbours(floorspot, floor_map)
                if floorspot.neighbours < 4:
                    print(f"Removing from ({floorspot.y},{floorspot.x})")
                    floorspot.value = 'X'
                    removed += 1
        total_removed += removed
        if removed == 0:
            if final_try:
                break
            final_try = True
        else:
            final_try = False

    print(f"Part two - Removed: {total_removed}")


def get_input() -> list[list[Floorspot]]:
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
        # coords are y, x:
        all_lines = []
        for y in range(len(lines)):
            current_line = []
            for x in range(len(lines[y])):
                current_line.append(Floorspot(lines[y][x], (y, x)))
            all_lines.append(current_line)
    return all_lines


def solve():
    floor_map = get_input()
    process_floor_map_part_one(copy.deepcopy(floor_map))
    process_floor_map_part_two(copy.deepcopy(floor_map))


if __name__ == "__main__":
    solve()
