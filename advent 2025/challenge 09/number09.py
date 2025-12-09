from datetime import datetime

from shapely.geometry import Point
from shapely.geometry import Polygon


class Coord:
    def __init__(self, x: int, y: int):
        self._x = x
        self._y = y

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @staticmethod
    def from_string(coord_string: str) -> 'Coord':
        x, y = coord_string.split(',')
        return Coord(int(x), int(y))

    def is_inside(self, boundary: Polygon, opposite: 'Coord'):
        poly = Polygon([(self.x, self.y), (self.x, opposite.y), (opposite.x, opposite.y), (opposite.x, self.y), (self.x, self._y)])
        return boundary.covers(poly)


def get_surface(a: Coord, b: Coord) -> int:
    h = a.x+1 - b.x if a.x > b.x else b.x+1 - a.x
    v = a.y+1 - b.y if a.y > b.y else b.y+1 - a.y
    return h*v


def process_inputs(red_tiles: list[Coord]):
    start = datetime.now()
    dists = []
    for a in red_tiles:
        for b in red_tiles:
            if a == b:
                continue
            dists.append((a, b, get_surface(a, b)))

    green_tiles = []
    for idx, a in enumerate(red_tiles):
        if idx < len(red_tiles)-1:
            b = red_tiles[idx+1]
        else:
            b = red_tiles[0]
        if a.x > b.x:
            green_tiles += list((i, a.y) for i in range(a.x, b.x - 1, -1))
        if b.x > a.x:
            green_tiles += list((i, a.y) for i in range(a.x, b.x + 1))
        if a.y > b.y:
            green_tiles += list((a.x, i) for i in range(a.y, b.y - 1, -1))
        if b.y > a.y:
            green_tiles += list((a.x, i) for i in range(a.y, b.y + 1))

    dists.sort(key=lambda tup: tup[2])

    deduped_dists = dists
    deduped_dists.reverse()
    print(f"Part one: {deduped_dists[0][2]}")
    print(f"Part one only took {(datetime.now() - start).microseconds/1000000} seconds!")

    # Start part two
    boundary = Polygon(green_tiles)

    start = datetime.now()
    print(f"Starting part two. Sit back; this might take a while")
    for a, b, dist in deduped_dists:
        if a.is_inside(boundary, b) and a.x != b.x and a.y != b.y:
            print(f"Part two: {a.x, a.y, b.x, b.y} with dist {dist}")
            print(f"Part two only took {(datetime.now() - start).seconds} seconds!")
            break


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [Coord.from_string(l.strip('\n')) for l in input_file.readlines()]
    return lines


def solve():
    daily_input = get_input()
    process_inputs(daily_input)


if __name__ == "__main__":
    solve()
