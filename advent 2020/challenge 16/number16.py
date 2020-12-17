from collections import defaultdict, deque


def get_input():
    with open('./input.txt', 'r') as file:
        valid_ranges = {}
        nearby_tickets = []
        lines = file.readlines()
        for thing in lines:
            if thing == '\n':
                continue
            elif len(thing.split(": ")) > 1:
                range_signifier = thing.split(': ')[0]
                for ranges in thing.split(': '):
                    if ranges == range_signifier:
                        continue
                    for valid_range in ranges[:-1].split(' or '):
                        range_min = int(valid_range.split('-')[0])
                        range_max = int(valid_range.split('-')[1]) + 1
                        single_signifier_range = list(range(range_min, range_max))
                        try:
                            valid_ranges[range_signifier] += single_signifier_range
                        except KeyError:
                            valid_ranges[range_signifier] = single_signifier_range
            elif thing.split(":")[0] == 'your ticket':
                my_ticket = [int(x) for x in lines[lines.index(thing)+1][:-1].split(',')]
            elif thing.split(":")[0] == 'nearby tickets':
                continue
            else:
                if [int(x) for x in thing.split(',')] == my_ticket:
                    continue
                nearby_tickets += [[int(x) for x in thing[:-1].split(',')]]

        return valid_ranges, my_ticket, nearby_tickets


def find_limiting_value(values, rangedict):
    valid_ranges = []
    invalid_ranges = []
    for range_name, ranges in rangedict.items():
        for value in values:
            if value not in ranges:
                invalid_ranges += [range_name]
        if not range_name in invalid_ranges:
            valid_ranges += [range_name]
    return valid_ranges, invalid_ranges


def validate_tickets(valid_ranges, tickets_to_check, own_ticket):
    invalid_numbers = []
    valid_numbers = []
    valid_tickets = []

    for k,v in valid_ranges.items():
        valid_numbers += v
    for ticket in tickets_to_check:
        error_counter = 0
        for value in ticket:
            if value not in valid_numbers:
                invalid_numbers += [value]
                error_counter += 1
        if error_counter == 0:
            valid_tickets += [ticket]

    column_index = 0
    ranges_with_columns = defaultdict(deque)

    while column_index < len(valid_tickets[0]):
        this_column_values = []

        for ticket in valid_tickets:
            this_column_values.append(ticket[column_index])
        ranges_to_check, ranges_to_ignore = find_limiting_value(this_column_values, valid_ranges)
        for check_range in ranges_to_check:
            ranges_with_columns[check_range].append(column_index)
        column_index += 1

    columnized_keys = {}
    columns_processed = []
    counter = 1
    iteration_finished = False
    while not iteration_finished:
        for key, values_for_column in ranges_with_columns.items():
            if len(values_for_column) == counter:
                for column_number in values_for_column:
                    if column_number not in columns_processed:
                        columnized_keys[key] = column_number
                        columns_processed += [column_number]
                        counter += 1
        if len(columnized_keys) == len(ranges_with_columns):
            iteration_finished = True

    values_to_multiply = []
    for column_name, cindex in columnized_keys.items():
        if column_name.split(' ')[0] == 'departure':
            values_to_multiply += [own_ticket[cindex]]

    departure_multiplier = 1
    for multiplication_value in values_to_multiply:
        departure_multiplier *= multiplication_value

    return sum(invalid_numbers), departure_multiplier


def solve():
    valid_ranges, my_ticket, nearby_tickets = get_input()
    error_rate, final_solution = validate_tickets(valid_ranges, nearby_tickets, my_ticket)
    print("Got an error rate of {} for the presented tickets".format(error_rate))
    print("Multiplied departure values to {}".format(final_solution))


def main():
    solve()


if __name__ == "__main__":
    main()