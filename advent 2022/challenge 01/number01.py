import re


def get_input():
    with open('./input.txt', 'r') as input_file:
        elves = []
        calorie_counter = 0
        lines = [l.strip('\n') for l in input_file.readlines()]
        for elf in lines:
            if re.match('[0-9]+', elf):
                calorie_counter += int(elf)
            else:
                elves.append(calorie_counter)
                calorie_counter = 0

        elves.append(calorie_counter)

    return sorted(elves)


def solve():
    elves_with_calories = get_input()
    print(elves_with_calories[-1])
    print(sum(elves_with_calories[-3:]))


if __name__ == "__main__":
    solve()
