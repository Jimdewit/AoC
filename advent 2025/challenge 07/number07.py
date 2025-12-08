import copy
import time


class Floorspot:
    def __init__(self, value: str, coords: tuple[int, int]):
        self._coords = coords
        self._value = value
        self._number_of_beams: int = 0

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
    def number_of_beams(self):
        return self._number_of_beams

    @number_of_beams.setter
    def number_of_beams(self, amount: int):
        self._number_of_beams = amount


def process_floor_map(floor_map: list[list[Floorspot]]):
    split = 0
    for y in range(len(floor_map)):
        for x in range(len(floor_map[y])):
            floorspot = floor_map[y][x]
            if floorspot.value == 'S':
                floor_map[y][x].number_of_beams = 1
            if floorspot.value == '^' and floor_map[y-1][x].number_of_beams > 0:
                split += 1
                floor_map[y+1][x-1].number_of_beams += floor_map[y-1][x].number_of_beams
                floor_map[y+1][x+1].number_of_beams += floor_map[y-1][x].number_of_beams
            if floor_map[y - 1][x].number_of_beams > 0 and floorspot.value != '^':
                floor_map[y][x].number_of_beams += floor_map[y-1][x].number_of_beams

    print(f"Part one: {split} splits")
    print(f"Part two: {sum(x.number_of_beams for x in floor_map[-1])} timelines")
    return floor_map


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
    daily_input = get_input()
    process_floor_map(copy.deepcopy(daily_input))


if __name__ == "__main__":
    solve()
