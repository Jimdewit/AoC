def add_x(x: int, start: tuple) -> list[tuple]:
    start_pos = start[0]
    ret = []
    for i in range(1, x+1):
        ret.append((start_pos+i, start[1]))
    return ret


def sub_x(x: int, start: tuple) -> list[tuple]:
    start_pos = start[0]
    ret = []
    for i in range(1, x+1):
        ret.append((start_pos-i, start[1]))
    return ret


def add_y(y: int, start: tuple) -> list[tuple]:
    start_pos = start[1]
    ret = []
    for i in range(1, y+1):
        ret.append((start[0], start_pos+i))
    return ret


def sub_y(y: int, start: tuple) -> list[tuple]:
    start_pos = start[1]
    ret = []
    for i in range(1, y+1):
        ret.append((start[0], start_pos-i))
    return ret


class Wire:
    def __init__(self, route: list[str]):
        self._route = route
        self._coords = self._coords_from_route(route)

    @property
    def coords(self):
        return self._coords

    def step_count(self, coord):
        return self._coords.index(coord) + 1

    def intersects(self, target_coords: list[tuple]):
        return set(self._coords).intersection(target_coords)

    @staticmethod
    def _coords_from_route(route: list[str]):
        coords = []
        for r in route:
            start = (0,0) if len(coords) == 0 else coords[-1]
            direction, diff = r[0], int(r[1:])
            if direction == "U":
                coords += add_y(diff, start)
            if direction == "D":
                coords += sub_y(diff, start)
            if direction == "L":
                coords += sub_x(diff, start)
            if direction == "R":
                coords += add_x(diff, start)

        return coords


def get_wires(inp):
    first = Wire(inp[0])
    second = Wire(inp[1])
    intersections = first.intersects(second.coords)
    print(f"Checking intersections {intersections}")
    smallest = None
    for i in intersections:
        if not smallest:
            smallest = sum(list(i))
        if sum(list(i)) < smallest:
            smallest = sum(list(i))

    print(f"Part one: {smallest}")
    smallest = None
    for i in intersections:
        steps = first.step_count(i) + second.step_count(i)
        if not smallest:
            smallest = steps
        if steps < smallest:
            smallest = steps
    print(f"Part two: {smallest}")


def get_input():
    with open('./input.txt', 'r') as file:
        return [x for x in [l.rstrip('\n').split(',') for l in file.readlines()]]


def main():
    inp = get_input()
    get_wires(inp)


if __name__ == "__main__":
    main()