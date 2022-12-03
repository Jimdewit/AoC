
def find_duplicates(rucksack_contents):
    letter_sum = 0
    all_duplicates = []

    for rucksack in rucksack_contents:
        rucksack_duplicates = []
        left = rucksack[:int(len(rucksack)/2)]
        right = rucksack[int(len(rucksack)/2):]
        for item in left:
            if item in right and item not in rucksack_duplicates:
                rucksack_duplicates.append(item)

        all_duplicates += rucksack_duplicates

    for letter in all_duplicates:
        letter_sum += ord(letter)-96 if letter.islower() else ord(letter)-38

    return letter_sum


def find_badges(rucksack_contents):
    current_elves_counter = 0
    letter_sum = 0
    badges = []

    for x in range(0, int(len(rucksack_contents)/3)):
        current_elves = rucksack_contents[current_elves_counter:current_elves_counter+3]
        print(current_elves)

        for item in current_elves[0]:
            if item in current_elves[1]:
                if item in current_elves[2]:
                    badges.append(item)
                    current_elves_counter += 3
                    break


    for letter in badges:
        letter_sum += ord(letter) - 96 if letter.islower() else ord(letter) - 38

    return letter_sum


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
    return lines


def solve():
    rucksacks = get_input()
    print(find_duplicates(rucksacks))
    print(find_badges(rucksacks))


if __name__ == "__main__":
    solve()
