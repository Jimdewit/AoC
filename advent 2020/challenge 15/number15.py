from collections import defaultdict, deque


def get_input():
    with open('./input.txt', 'r') as file:
        for line in file:
            return [int(x) for x in line[:-1].split(',')]


def solve(numbers, turns):
    turn_counter = 1
    spoken_numbers_dict = defaultdict(deque)

    for number in numbers:
        spoken_numbers_dict[number].append(turn_counter)
        turn_counter += 1

    number = 0

    while turn_counter <= turns:
        i = len(spoken_numbers_dict[number])
        if i > 1:
            number = spoken_numbers_dict[number][-1] - spoken_numbers_dict[number][-2]
            spoken_numbers_dict[number].append(turn_counter)
        elif i == 1:
            number = 0
            spoken_numbers_dict[number].append(turn_counter)
        else:
            number = 0
            spoken_numbers_dict[number].append(turn_counter)

        turn_counter += 1
        if turn_counter % 1000 == 0:
            print("Still working, currently at turn {}".format(turn_counter))

    return number


def main():
    starting_numbers = get_input()
    endloesung = solve(starting_numbers, 2020)
    print(endloesung)
    endendloesung = solve(starting_numbers, 30000000)
    print(endendloesung)


if __name__ == "__main__":
    main()