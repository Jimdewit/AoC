def find_overlapping_ranges(list_of_plots):
    overlap_counter = 0
    for plots in list_of_plots:
        if plots[0][0] <= plots[1][0] <= plots[0][1]\
        or plots[0][0] <= plots[1][1] <= plots[0][1]:
            overlap_counter += 1
        elif plots[1][0] <= plots[0][0] <= plots[1][1]\
        or plots[1][0] <= plots[0][1] <= plots[1][1]:
            overlap_counter += 1

    return overlap_counter

def find_contained_ranges(list_of_plots):
    contained_counter = 0
    for plots in list_of_plots:
        if plots[0][0] >= plots[1][0] and plots[0][1] <= plots[1][1]:
            contained_counter += 1
        elif plots[1][0] >= plots[0][0] and plots[1][1] <= plots[0][1]:
            contained_counter += 1

    return contained_counter


def get_input():
    with open('./input.txt', 'r') as input_file:
        assigned_plot_list = []
        lines = [l.strip('\n') for l in input_file.readlines()]
        for p1, p2 in [l.split(',') for l in lines]:

            assigned_plot_list.append((((int(p1.split('-')[0]), int(p1.split('-')[1])),
                                        (int(p2.split('-')[0]), int(p2.split('-')[1])))))
        print(assigned_plot_list)
    return assigned_plot_list


def solve():
    list_of_plots = get_input()
    print(find_contained_ranges(list_of_plots))
    print(find_overlapping_ranges(list_of_plots))


if __name__ == "__main__":
    solve()
