from copy import deepcopy


def get_input():
    with open('./input.txt', 'r') as file:
        free_seats_dict = {}
        line_counter = 0
        for seats in file:
            free_seats_dict[line_counter] = dict(list(enumerate(seats.rstrip('\n'))))
            line_counter += 1
        return free_seats_dict


def get_surrounding_grid_info(xcoord, ycoord, seats_dict=None):
    def _find_seat(current_seats, starting_pos, directions):
        # Find seat in given direction from starting position. Left/Up is specified as -1, Right/Down as 1
        x = starting_pos[0] + directions[0]
        y = starting_pos[1] + directions[1]
        while 1 == 1:
            try:
                row_dict = current_seats[y]
                try:
                    if row_dict[x] == '#':
                        return '#'
                    elif row_dict[x] == 'L':
                        return 'L'
                    else:
                        x += directions[0]
                        y += directions[1]
                        continue
                except IndexError:
                    return '.'
            except KeyError:
                return '.'

    x = xcoord
    y = ycoord
    start = [xcoord, ycoord]
    if seats_dict:
        neighbours = []
        neighbours += [_find_seat(seats_dict, start, [-1, -1]), _find_seat(seats_dict, start, [0, -1]), _find_seat(seats_dict, start, [1, -1])]
        neighbours += [_find_seat(seats_dict, start, [-1, 0]), _find_seat(seats_dict, start, [1, 0])]
        neighbours += [_find_seat(seats_dict, start, [-1, 1]), _find_seat(seats_dict, start, [0, 1]), _find_seat(seats_dict, start, [1, 1])]
        return neighbours
    else:
        neighbours = {y - 1: {x - 1: '.', x: '.', x + 1: '.'}, y: {x - 1: '.', x + 1: '.'}, y + 1: {x - 1: '.', x: '.', x + 1: '.'}}
        return neighbours


def count_values(input_iterable, sought_value):
    if isinstance(input_iterable, dict):
        counter = 0
        for x in input_iterable:
            for k in input_iterable[x]:
                if input_iterable[x][k] == sought_value:
                    counter += 1
        return counter
    else:
        return input_iterable.count('#')


def appoint_seats(seat_allotment, visibility_toggle=False, debug_mode=False):
    neighbour_tolerance = 4 if not visibility_toggle else 5
    new_seat_distribution = deepcopy(seat_allotment)
    for y, columns in new_seat_distribution.items():
        for x in columns:
            if columns[x] == '.':
                continue
            if not visibility_toggle:
                surrounding_keys = get_surrounding_grid_info(x, y)
                occupied_neighbours = count_values(surrounding_keys, '#')
                for y2, columns2 in surrounding_keys.items():
                    for x2 in columns2:
                        try:
                            if seat_allotment[y2][x2] == '#':
                                surrounding_keys[y2][x2] = '#'
                            elif seat_allotment[y2][x2] == '.':
                                continue
                            elif seat_allotment[y2][x2] == 'L':
                                surrounding_keys[y2][x2] = 'L'
                        except IndexError:
                            pass
                        except KeyError:
                            pass
            else:
                surrounding_keys = get_surrounding_grid_info(x, y, seats_dict=seat_allotment)
                occupied_neighbours = count_values(surrounding_keys, '#')
            if occupied_neighbours >= neighbour_tolerance:
                if debug_mode:
                    print("Emptying seat ({}, {}) because {} has {} occupied neighbours (from {})".format(
                       x, y, seat_allotment[y][x], count_values(surrounding_keys, '#'), surrounding_keys))
                new_seat_distribution[y][x] = 'L'
            elif occupied_neighbours == 0:
                if debug_mode:
                    print("Filling seat ({}, {}) because {} has {} occupied neighbours (from {})".format(
                        x, y, seat_allotment[y][x], count_values(surrounding_keys, '#'), surrounding_keys))
                new_seat_distribution[y][x] = '#'
            else:
                if debug_mode:
                    print("Not touching seat ({}, {}) because {} has {} occupied neighbours (from {})".format(
                        x, y, seat_allotment[y][x], count_values(surrounding_keys, '#'), surrounding_keys))
                continue

    if debug_mode:
        print("Input seats: {}".format(seat_allotment))
        print("Output seats: {}".format(new_seat_distribution))
    return new_seat_distribution if new_seat_distribution == seat_allotment else appoint_seats(new_seat_distribution, visibility_toggle=visibility_toggle, debug_mode=debug_mode)


def main():
    free_seats = get_input()
    seatmap = appoint_seats(free_seats, debug_mode=True)
    print("Total seats occupied: {}".format(count_values(seatmap, '#')))
    second_seatmap = appoint_seats(free_seats, visibility_toggle=True, debug_mode=False)
    print("Total seats occupied with new visibility rules: {}".format(count_values(second_seatmap, '#')))


if __name__ == "__main__":
    main()