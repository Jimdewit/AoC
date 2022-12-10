debug = False


def draw_sprite(sprite_pos, crt_pos):
    """
    sprite_pos: int: x_counter
    crt_pos: int: clock_cycle_counter -1
    """
    if crt_pos % 40 in range(sprite_pos, sprite_pos +3):
        return "#"
    else:
        return '.'


def process_add(x_counter, value):
    return x_counter + value


def process_noop():
    return


def process_operations(list_of_operations, start_cycle, end_cycle, cycle_step):
    crt_lines = [ ]
    current_crt_line = ''

    clock_cycle_counter = 0
    cycle_sum = 0
    x_counter = 1
    cycles_to_check = range(start_cycle, end_cycle, cycle_step)

    for op in list_of_operations:

        needs_increment_next_cycle = False
        if debug:
            print('Starting op for {}, cycles at {}, needs_inc = {}'.format(op, clock_cycle_counter, needs_increment_next_cycle))

        if op == 'noop':
            cycles = 1
        else:
            cycles = 2

        for x in range(0, cycles):
            clock_cycle_counter += 1
            if clock_cycle_counter in cycles_to_check:
                if debug:
                    print('Incrementing {} by {}, cycle counter at {}, x at {}'.format(cycle_sum, (clock_cycle_counter * x_counter), clock_cycle_counter, x_counter))
                cycle_sum += (clock_cycle_counter * x_counter)

            current_crt_line += (draw_sprite(x_counter, clock_cycle_counter))

            if needs_increment_next_cycle:
                x_counter = process_add(x_counter, op)
                needs_increment_next_cycle = False

            if isinstance(op, int):
                needs_increment_next_cycle = True

            if clock_cycle_counter % 40 == 0:
                crt_lines.append(current_crt_line)
                current_crt_line = ''

            if debug:
                print('Finished single iteration, clock at {}, x at {}'.format(clock_cycle_counter, x_counter))
                print(current_crt_line)

    return cycle_sum, crt_lines


def print_crt(scanlines):
    for x in scanlines:
        print(x)


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') if l.startswith('noop') else int(l.strip('\n').split()[1]) for l in input_file.readlines()]
    return lines


def solve():
    list_of_operations = get_input()
    cycle_sum, crt_lines = process_operations(list_of_operations, 20, 221, 40)
    print(cycle_sum)
    print_crt(crt_lines)


if __name__ == "__main__":
    solve()
