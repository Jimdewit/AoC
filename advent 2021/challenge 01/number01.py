

def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
    return lines


def process_depth(depth_list, use_sliding_window=False):
    increase_counter = 0
    if not use_sliding_window:
        previous_depth = depth_list[0]
        for depth in depth_list:
            if int(depth) > int(previous_depth):
                increase_counter += 1
            previous_depth = depth
        return increase_counter
    else:
        starting_pos = 0
        previous_window = sum(int(x) for x in depth_list[starting_pos:starting_pos+3])
        for depth in depth_list:
            current_window = sum(int(x) for x in depth_list[starting_pos:starting_pos+3])
            if current_window > previous_window:
                increase_counter += 1
            previous_window = current_window
            starting_pos += 1
        return increase_counter


def solve():
    depth_list = get_input()
    increment_counter = process_depth(depth_list)
    print(increment_counter)
    increment_counter = process_depth(depth_list, use_sliding_window=True)
    print(increment_counter)


if __name__ == "__main__":
    solve()