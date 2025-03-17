from pytz import UTC

from datetime import datetime


def normalise_time_zone(inp):
    tz_object = datetime.strptime(inp, '%Y-%m-%dT%H:%M:%S%z')
    normalised_tz_object = UTC.normalize(tz_object)
    return normalised_tz_object


def compare_counts(inp):
    for i in inp:
        if inp[i] >= 4:
            print(i)
            print(datetime.strftime(i, '%Y-%m-%dT%H:%M:%S%z'))


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
    return lines


def solve():
    daily_input = get_input()
    parsed = {}
    for i in daily_input:
        parsed_inp = normalise_time_zone(i)
        if parsed.get(parsed_inp):
            parsed[parsed_inp] += 1
        else:
            parsed[parsed_inp] = 1

    compare_counts(parsed)


if __name__ == "__main__":
    solve()
