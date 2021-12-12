import numpy


def find_start(x):
    start = x-1 if x-1 >= 0 else 0
    return start


def find_end(x, shape):
    end = x+1 if x+1 <= shape else shape
    return end


def process_flash(octo_list, x_orig, y_orig, flashed):
    row_start, row_end = find_start(x_orig), find_end(x_orig, octo_list.shape[0])
    col_start, col_end = find_start(y_orig), find_end(y_orig, octo_list.shape[1])

    octo_list[x_orig][y_orig] += 1
    flashed += [(x_orig, y_orig)]
    for y in range(octo_list.shape[0]):
        for x in range(octo_list.shape[1]):
            if row_start <= x <= row_end:
                if col_start <= y <= col_end:
                    if (x,y) != (x_orig, y_orig):
                        octo_list[x][y] += 1
                        if octo_list[x][y] >= 10 and (x, y) not in flashed:
                            octo_list, flashed = process_flash(octo_list, x, y, flashed)

    return octo_list, flashed


def process_octopi(octopi_list, keep_searching=False):
    process_counter = 0
    flash_counter = 0
    while True:
        flashed = []
        current_counter = 0

        # Increase octopi flash counters
        for y in range(octopi_list.shape[0]):
            for x in range(octopi_list.shape[1]):
                octo = octopi_list[x, y]
                octopi_list[x, y] = octo + 1

        # Process octopi flashing
        for y in range(octopi_list.shape[0]):
            for x in range(octopi_list.shape[1]):
                octo = octopi_list[x, y]
                if octo >= 10 and (x, y) not in flashed:
                    flashed += [(x, y)]
                    octopi_list, flashed = process_flash(octopi_list, x, y, flashed)

        for y in range(octopi_list.shape[0]):
            for x in range(octopi_list.shape[1]):
                octo = octopi_list[x, y]
                if octo > 9:
                    current_counter += 1
                    octopi_list[x, y] = 0
        if process_counter == 100 and not keep_searching:
            return flash_counter
        elif current_counter == 100:
            return process_counter
        else:
            flash_counter += current_counter
            process_counter += 1


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
        octopus_list = []
        for l in lines:
            single_line = []
            for x in l:
                single_line += [int(x)]
            octopus_list += [single_line]
    return numpy.array(octopus_list)


def solve():
    daily_input = get_input()
    print("100 iterations leads to {} flashes".format(process_octopi(daily_input)))
    print("Simultaneousness achieved at iteration {}".format(process_octopi(daily_input, keep_searching=True)))


if __name__ == "__main__":
    solve()
