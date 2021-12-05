from collections import Counter


def process_single_coordinate_set(coordinate_pair, seen_coordinates, diagonal=False):
    x1 = int(coordinate_pair[0][0])
    y1 = int(coordinate_pair[0][1])
    x2 = int(coordinate_pair[1][0])
    y2 = int(coordinate_pair[1][1])

    if x1 == x2:
        for y_delta in range(y1, y2+1) if y2 > y1 else range(y2, y1+1):
            seen_coordinates += [(x1, y_delta)]

    elif y1 == y2:
        for x_delta in range(x1, x2+1) if x2 > x1 else range(x2, x1+1):
            seen_coordinates += [(x_delta, y1)]

    else:
        if diagonal:
            x_delta_counter = 0
            for y_delta in range(y1, y2+1) if y2 > y1 else range(y2, y1+1):
                seen_coordinates += [(x1 + x_delta_counter if y2 > y1 else x2 + x_delta_counter, y_delta)]
                if y2 > y1:
                    if x2 > x1:
                        x_delta_counter += 1
                    else:
                        x_delta_counter -= 1
                else:
                    if x2 > x1:
                        x_delta_counter -= 1
                    else:
                        x_delta_counter += 1

    return seen_coordinates


def process_coordinates(list_of_pairs, diagonal=False):
    seen_coordinates = []
    for pair in list_of_pairs:
        process_single_coordinate_set(pair, seen_coordinates, diagonal=diagonal)
    return sum(value >= 2 for value in Counter(seen_coordinates).values())


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [((pair1.split(',')), (pair2.split(','))) for pair1, pair2 in [l.strip('\n').split(' -> ') for l in input_file.readlines()]]
    return lines


def solve():
    daily_input = get_input()
    intersecting_lines = process_coordinates(daily_input)
    print('Found {} intersecting lines'.format(intersecting_lines))
    intersecting_lines = process_coordinates(daily_input, diagonal=True)
    print('Found {} intersecting lines'.format(intersecting_lines))


if __name__ == "__main__":
    solve()