import re


def calculate_calories(elf_calories, find_multiple=False):
    if not find_multiple:
        return max(elf_calories)
    else:
        elf_sum = 0
        for x in range(0, 3):
            elf_sum += max(elf_calories)
            elf_calories.pop(elf_calories.index(max(elf_calories)))

        return elf_sum


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

    return elves


def solve():
    elves_with_calories = get_input()
    print(elves_with_calories)
    print(calculate_calories(elves_with_calories))
    print(calculate_calories(elves_with_calories, find_multiple=True))


if __name__ == "__main__":
    solve()
