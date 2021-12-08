import statistics


def check_positions(list_of_positions, increase_expense=False):
    fuel_sum = 0
    if not increase_expense:
        median = int(statistics.median(list_of_positions))
        for x in list_of_positions:
            fuel_sum += median - x if median > x else x - median
    else:
        # Rounding off high or low can probably be found in a neater way
        mean = int(round(statistics.mean(list_of_positions)))-1
        for x in list_of_positions:
            dx = mean - x if mean > x else x - mean
            fuel_sum += sum(range(dx+1))

    return fuel_sum


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [int(l) for l in input_file.read().strip('\n').split(',')]
    return lines


def solve():
    daily_input = get_input()
    total_fuel = check_positions(daily_input)
    print('Crab fuel used: {}'.format(total_fuel))
    more_expensive_fuel = check_positions(daily_input, increase_expense=True)
    print('More expensive fuel used: {}'.format(more_expensive_fuel))


if __name__ == "__main__":
    solve()
