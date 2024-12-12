from itertools import product


def read_input():
    with open('input.txt') as f:
        return [list(map(int, ln.strip())) for ln in f]


def trailhead_locations(mat):
    return [(x, y) for x, y in product(range(len(mat)), range(len(mat[0]))) if mat[x][y] == 0]


def find_all_paths(mat, start, by_rating=False):
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    rows, cols = len(mat), len(mat[0])

    def is_in_bounds(x, y):
        return 0 <= x < rows and 0 <= y < cols

    def iterate(x, y, path):
        if not is_in_bounds(x, y):
            return 0

        cached_entry = (x, y) if not by_rating else (x, y, path)
        if cached_entry in visited:
            return 0

        visited.add(cached_entry)

        if mat[x][y] == 9:
            return 1

        path_count = 0
        for dx, dy in dirs:
            nx, ny = x + dx, y + dy
            if is_in_bounds(nx, ny) and mat[nx][ny] - mat[x][y] == 1:
                path_count += iterate(nx, ny, path + f"({nx},{ny})")

        return path_count

    return iterate(start[0], start[1], '')


mat = read_input()
trailheads = trailhead_locations(mat)
rows, cols = len(mat), len(mat[0])

print('solution 1:', sum(find_all_paths(mat, th) for th in trailheads))
print('solution 2:', sum(find_all_paths(mat, th, True) for th in trailheads))