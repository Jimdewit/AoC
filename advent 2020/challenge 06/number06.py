import string


def get_and_group_input(count_all=False):
    "Returns a dict of groups; each group is a dict of letters"
    with open('./input.txt', 'r') as answersfile:
        groups = {}
        single_group = {i: 0 for i in string.ascii_lowercase[:26]}
        single_group['group_size'] = 0
        x = 0
        for line in answersfile:
            if line[0] == '\n':
                groups[x] = single_group
                single_group = {i: 0 for i in string.ascii_lowercase[:26]}
                single_group['group_size'] = 0
                x += 1
                continue
            else:
                for letter in line.rstrip('\n'):
                    single_group[letter] += 1 if count_all else 1
                single_group['group_size'] += 1
        groups[x] = single_group
    return groups


def count_occurrences_per_group(input_dict, no_more_naysayers=False):
    count = 0
    for answer_group in input_dict:
        for x in input_dict[answer_group]:
            if input_dict[answer_group][x] > 0 and x != 'group_size' and not no_more_naysayers:
                count += 1
            elif no_more_naysayers and input_dict[answer_group][x] == input_dict[answer_group]['group_size'] and x != 'group_size':
                count += 1
            else:
                continue
    return count


def main():
    print("Total count is {}".format(count_occurrences_per_group(get_and_group_input())))
    print("Total count of yessirs is {}".format(count_occurrences_per_group(get_and_group_input(), no_more_naysayers=True)))


if __name__ == "__main__":
    main()