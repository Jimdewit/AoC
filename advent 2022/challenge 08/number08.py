def tree_if_bigger_than_neighbours(grid, x, y):
    left_neighbours = [grid[y][xl] for xl in range(0, x)]
    right_neighbours = [grid[y][xr] for xr in range(x+1, len(grid[y]))]
    top_neighbours = [grid[yt][x] for yt in range(0, y)]
    bottom_neighbours = [grid[yb][x] for yb in range(y+1, len(grid))]

    if grid[y][x] > max(left_neighbours) or grid[y][x] > max(right_neighbours) or grid[y][x] > max(top_neighbours) or grid[y][x] > max(bottom_neighbours):
            return True
    return False


def find_visible(tree_grid):
    x = 0
    visible = 0
    trees_counted = []
    for y in range(0, len(tree_grid)):
        line = tree_grid[y]
        for x in range(0, len(line)):
            if y == 0 or y == len(tree_grid)-1:
                if (x, y) not in trees_counted:
                    visible += 1
                    trees_counted.append((x, y))
            elif x == 0 or x == len(line)-1:
                if (x, y) not in trees_counted:
                    visible += 1
                    trees_counted.append((x, y))
            else:
                if tree_if_bigger_than_neighbours(tree_grid, x, y):
                    if (x, y) not in trees_counted:
                        visible += 1
                        trees_counted.append((x, y))

    return visible


def calculate_single_tree(grid, x, y):
    visible_left = visible_right = visible_top = visible_bottom = 0
    current_height = grid[y][x]
    left_neighbours = [grid[y][xl] for xl in range(0, x)]
    right_neighbours = [grid[y][xr] for xr in range(x + 1, len(grid[y]))]
    top_neighbours = [grid[yt][x] for yt in range(0, y)]
    bottom_neighbours = [grid[yb][x] for yb in range(y + 1, len(grid))]

    left_neighbours.reverse()
    top_neighbours.reverse()

    for tree in left_neighbours:
        if tree < current_height:
            visible_left += 1
        else:
            visible_left += 1
            break

    for tree in right_neighbours:
        if tree < current_height:
            visible_right += 1
        else:
            visible_right += 1
            break

    for tree in top_neighbours:
        if tree < current_height:
            visible_top += 1
        else:
            visible_top += 1
            break

    for tree in bottom_neighbours:
        if tree < current_height:
            visible_bottom += 1
        else:
            visible_bottom += 1
            break

    return visible_left * visible_right * visible_top * visible_bottom


def calculate_scenic_score(tree_grid):
    current_best = 0
    for y in range(0, len(tree_grid)):
        line = tree_grid[y]
        for x in range(0, len(line)):
            if y == 0 or y == len(tree_grid) - 1:
                continue
            elif x == 0 or x == len(line) - 1:
                continue
            else:
                tree_score = calculate_single_tree(tree_grid, x, y)
                current_best = tree_score if tree_score > current_best else current_best
    return  current_best


def get_input():
    with open('./input.txt', 'r') as input_file:
        tree_grid = []
        lines = [l.strip('\n') for l in input_file.readlines()]
        for l in lines:
            tree_grid += [[int(x) for x in l]]
    return tree_grid


def solve():
    tree_grid = get_input()
    print(find_visible(tree_grid))
    print(calculate_scenic_score(tree_grid))


if __name__ == "__main__":
    solve()
