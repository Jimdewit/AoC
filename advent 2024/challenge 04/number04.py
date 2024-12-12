

class Coord:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


def up_left(coord: Coord, inp: list) -> bool:
    if coord.x -3 < 0 or coord.y - 3 < 0:
        return False
    try:
        if inp[coord.y - 1][coord.x - 1] == 'M' \
                and inp[coord.y - 2][coord.x - 2] == 'A' \
                and inp[coord.y - 3][coord.x - 3] == 'S':
            print(f"Found XMAS at ({coord.y},{coord.x}) ({coord.y - 1},{coord.x - 1})"
                  f" ({coord.y - 2},{coord.x - 2}) ({coord.y - 3},{coord.x - 3})")
            return True
        else:
            return False
    except IndexError:
        return False


def up(coord: Coord, inp: list) -> bool:
    if coord.y - 3 < 0:
        return False
    try:
        if inp[coord.y - 1][coord.x] == 'M' \
                and inp[coord.y - 2][coord.x] == 'A' \
                and inp[coord.y - 3][coord.x] == 'S':
            print(f"Found XMAS at ({coord.y},{coord.x}) ({coord.y - 1},{coord.x})"
                  f" ({coord.y - 2},{coord.x}) ({coord.y - 3},{coord.x})")
            return True
        else:
            return False
    except IndexError:
        return False


def up_right(coord: Coord, inp: list) -> bool:
    if coord.y - 3 < 0:
        return False
    try:
        if inp[coord.y - 1][coord.x + 1] == 'M' \
                and inp[coord.y - 2][coord.x + 2] == 'A' \
                and inp[coord.y - 3][coord.x + 3] == 'S':
            print(f"Found XMAS at ({coord.y},{coord.x}) ({coord.y - 1},{coord.x + 1})"
                  f" ({coord.y - 2},{coord.x + 2}) ({coord.y - 3},{coord.x + 3})")
            return True
        else:
            return False
    except IndexError:
        return False


def right(coord: Coord, inp: list) -> bool:
    try:
        if inp[coord.y][coord.x + 1] == 'M' \
                and inp[coord.y][coord.x + 2] == 'A' \
                and inp[coord.y][coord.x + 3] == 'S':
            print(f"Found XMAS at ({coord.y},{coord.x}) ({coord.y},{coord.x + 1})"
                  f" ({coord.y},{coord.x + 2}) ({coord.y},{coord.x + 3})")
            return True
        else:
            return False
    except IndexError:
        return False


def down_right(coord: Coord, inp: list) -> bool:
    try:
        if inp[coord.y + 1][coord.x + 1] == 'M' \
                and inp[coord.y + 2][coord.x + 2] == 'A' \
                and inp[coord.y + 3][coord.x + 3] == 'S':
            print(f"Found XMAS at ({coord.y},{coord.x}) ({coord.y+1},{coord.x + 1})"
                  f" ({coord.y+2},{coord.x + 2}) ({coord.y+3},{coord.x + 3})")
            return True
        else:
            return False
    except IndexError:
        return False


def down(coord: Coord, inp: list) -> bool:
    try:
        if inp[coord.y + 1][coord.x] == 'M' \
                and inp[coord.y + 2][coord.x] == 'A' \
                and inp[coord.y + 3][coord.x] == 'S':
            print(f"Found XMAS at ({coord.y},{coord.x}) ({coord.y+1},{coord.x})"
                  f" ({coord.y+2},{coord.x}) ({coord.y+3},{coord.x})")
            return True
        else:
            return False
    except IndexError:
        return False


def down_left(coord: Coord, inp: list) -> bool:
    if coord.x - 3 < 0:
        return False
    try:
        if inp[coord.y + 1][coord.x - 1] == 'M' \
                and inp[coord.y + 2][coord.x - 2] == 'A' \
                and inp[coord.y + 3][coord.x - 3] == 'S':
            print(f"Found XMAS at ({coord.y},{coord.x}) ({coord.y+1},{coord.x - 1})"
                  f" ({coord.y+2},{coord.x - 2}) ({coord.y+3},{coord.x - 3})")
            return True
        else:
            return False
    except IndexError:
        return False


def left(coord: Coord, inp: list) -> bool:
    if coord.x - 3 < 0:
        return False
    try:
        if inp[coord.y][coord.x - 1] == 'M' \
                and inp[coord.y][coord.x - 2] == 'A' \
                and inp[coord.y][coord.x - 3] == 'S':
            print(f"Found XMAS at ({coord.y},{coord.x}) ({coord.y},{coord.x-1})"
                  f" ({coord.y},{coord.x-2}) ({coord.y},{coord.x-3})")
            return True
        else:
            return False
    except IndexError:
        return False


# SOLVE PART TWO


def two_up_left(coord: Coord, inp: list) -> bool:
    if coord.x - 1 < 0 or coord.y - 1 < 0:
        return False
    try:
        if inp[coord.y - 1][coord.x - 1] == 'M' \
                and inp[coord.y + 1][coord.x + 1] == 'S':
            print(f"Found MAS at ({coord.y-1},{coord.x-1}) ({coord.y},{coord.x})"
                  f" ({coord.y + 1},{coord.x + 1})")
            return True
        else:
            return False
    except IndexError:
        return False


def two_up_right(coord: Coord, inp: list) -> bool:
    if coord.x - 1 < 0 or coord.y - 1 < 0:
        return False
    try:
        if inp[coord.y - 1][coord.x + 1] == 'M' \
                and inp[coord.y + 1][coord.x - 1] == 'S':
            return True
        else:
            return False
    except IndexError:
        return False


def two_down_right(coord: Coord, inp: list) -> bool:
    if coord.x - 1 < 0 or coord.y - 1 < 0:
        return False
    try:
        if inp[coord.y + 1][coord.x + 1] == 'M' \
                and inp[coord.y - 1][coord.x - 1] == 'S':
            return True
        else:
            return False
    except IndexError:
        return False


def two_down_left(coord: Coord, inp: list) -> bool:
    if coord.x - 1 < 0 or coord.y - 1 < 0:
        return False
    try:
        if inp[coord.y + 1][coord.x - 1] == 'M' \
                and inp[coord.y - 1][coord.x + 1] == 'S':
            return True
        else:
            return False
    except IndexError:
        return False


def get_input() -> (list, list):
    inp = []
    xes = []
    aes = []
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
        y = 0
        for l in lines:
            x = 0
            inp += [l]
            for letter in l:
                if letter == 'X':
                    xes += [Coord(x, y)]
                if letter == 'A':
                    aes += [Coord(x, y)]
                x += 1
            y += 1

    return inp, xes, aes


def number_of_neighbours(inp: list, xes: list) -> int:
    xmas_found = 0
    for x_coord in xes:
        xmas_found += 1 if up_left(x_coord, inp) else 0
        xmas_found += 1 if up(x_coord, inp) else 0
        xmas_found += 1 if up_right(x_coord, inp) else 0
        xmas_found += 1 if right(x_coord, inp) else 0
        xmas_found += 1 if down_right(x_coord, inp) else 0
        xmas_found += 1 if down(x_coord, inp) else 0
        xmas_found += 1 if down_left(x_coord, inp) else 0
        xmas_found += 1 if left(x_coord, inp) else 0

    return xmas_found


def two_number_of_neighbours(inp: list, aes: list) -> int:
    xmas_found = 0
    for a_coord in aes:
        cross_count = 0
        cross_count += 1 if two_up_left(a_coord, inp) else 0
        cross_count += 1 if two_up_right(a_coord, inp) else 0
        cross_count += 1 if two_down_right(a_coord, inp) else 0
        cross_count += 1 if two_down_left(a_coord, inp) else 0
        xmas_found += 1 if cross_count >= 2 else 0

    return xmas_found


def solve():
    inp, xes, aes = get_input()
    print(number_of_neighbours(inp, xes))
    print(two_number_of_neighbours(inp, aes))


if __name__ == "__main__":
    solve()
