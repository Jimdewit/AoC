def solve():
    weight_input = get_input()
    fuel_needed = part_a(weight_input)
    total_fuel_needed = part_b(weight_input)
    print("Fuel needed for part A: {}\nFuel needed for part B: {}".format(fuel_needed, total_fuel_needed))


def part_a(input_weight):
    fuel_needed = []
    for i in input_weight:
        fuel_needed += [i // 3 - 2]
    return sum(fuel_needed)


def part_b(input_weight):
    def _fuel_weight_iterator(fuel, fuel_fuel=0):
        fuel_to_add = fuel // 3 - 2
        fuel_fuel += fuel_to_add if fuel_to_add > 0 else 0
        return fuel_fuel if fuel_to_add <= 0 else _fuel_weight_iterator(fuel_to_add, fuel_fuel)

    total_weight = 0
    for i in input_weight:
        fuel_needed = i // 3 - 2
        aggregate_fuel_needed = fuel_needed + _fuel_weight_iterator(fuel_needed)
        total_weight += aggregate_fuel_needed

    return total_weight


def get_input():
    weight_list = []
    with open('./input.txt', 'r') as lines:
        for line in lines:
            weight_list += [int(line.rstrip('\n'))]
    return weight_list

if __name__ == "__main__":
    solve()