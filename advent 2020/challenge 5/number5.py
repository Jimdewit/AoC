import re


def solve():
    seats = get_and_split_seats()
    seat_ids = []
    for seat in seats:
        row = find_row_and_seat(seats[seat][0], range(128))
        column = find_row_and_seat(seats[seat][1], range(8))
        seat_ids += [row * 8 + column]
    my_seat = find_missing_seat(sorted(seat_ids))

    print("Highest seat id is {}".format(sorted(seat_ids)[-1]))
    print("Your seat id is {}".format(my_seat))


def find_missing_seat(seat_ids, pos=0):
    return seat_ids[pos] + 1 if seat_ids[pos+1] - seat_ids[pos] == 2 else find_missing_seat(seat_ids, pos+1)


def find_row_and_seat(input_letters, range_to_check):
    current_letter = input_letters[:1]

    lower_half = range_to_check[:len(range_to_check) // 2]
    upper_half = range_to_check[len(range_to_check) // 2:]

    range_to_check = lower_half if current_letter in ['F', 'L'] else upper_half

    input_letters = input_letters[1:]
    if len(input_letters) == 0:
        return range_to_check[0]

    return find_row_and_seat(input_letters, range_to_check)


def get_and_split_seats():
    seats = {}
    with open('./input.txt', 'r') as seatsfile:
        for seat in seatsfile:
            row = re.search('[BF]{1,7}', seat)
            column = re.search('[LR]{1,3}', seat)
            seats[seat[:-1]] = [row.group(), column.group()]
        return seats


if __name__ == "__main__":
    solve()