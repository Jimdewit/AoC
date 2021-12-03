def convert_to_decimal(number, base):
    return int(number, base)


def find_oxygen(binary_input, pos=0, keep_high=True):
    remaining_numbers = []
    most_common = parse_binary(binary_input, starting_pos=pos, keep_high=keep_high)
    for number in binary_input:
        if int(most_common) == int(number[pos]):
            remaining_numbers += [number]
        else:
            continue
    if pos < len(binary_input[0]) -1 and len(remaining_numbers) > 1:
        return find_oxygen(remaining_numbers, pos+1, keep_high=keep_high)
    else:
        return remaining_numbers[0]


def parse_binary(binary_input, binary_output='', starting_pos=0, keep_high=True, recurse=False):
    counter = 0
    for number in binary_input:
        if keep_high:
            if int(number[starting_pos]) == 1:
                counter += 1
            else:
                counter += 0
        else:
            if int(number[starting_pos]) == 1:
                counter += 0
            else:
                counter += 1

    if counter > len(binary_input) / 2:
        binary_output += '1'
    elif counter == len(binary_input) / 2:
        binary_output += '1' if keep_high else '0'
    else:
        binary_output += '0'

    if recurse and starting_pos < len(binary_input[0]) -1:
        return parse_binary(binary_input, binary_output, starting_pos+1, keep_high=keep_high, recurse=recurse)
    return binary_output


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
    return lines


def solve():
    daily_input = get_input()
    gamma_binary = parse_binary(daily_input, recurse=True)
    epsilon_binary = parse_binary(daily_input, keep_high=False, recurse=True)
    power_consumption = convert_to_decimal(gamma_binary, 2) * convert_to_decimal(epsilon_binary, 2)
    print('Power consumption: {}'.format(power_consumption))
    oxygen_binary = find_oxygen(daily_input, keep_high=True)
    co2_binary = find_oxygen(daily_input, keep_high=False)
    ls_rating = convert_to_decimal(oxygen_binary, 2) * convert_to_decimal(co2_binary, 2)
    print('Life support rating: {}'.format(ls_rating))


if __name__ == "__main__":
    solve()
