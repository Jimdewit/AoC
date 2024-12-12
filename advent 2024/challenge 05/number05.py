from math import ceil, floor


def page_comes_after_previous(page, previous_page, ordering_rules):
    return (page, previous_page) in ordering_rules


def find_middle_numbers(correct_instructions):
    nums = 0
    for i in correct_instructions:
        nums += i[ceil(len(i)/2)-1]

    return nums


def process_pages_for_update_instructions(page_instructions, ruleset):
    correct_instructions = []
    incorrect_instructions = []
    for instruction in page_instructions:
        pages = []
        for x in range(len(instruction)):
            pages += [instruction[x]]
            if len(pages) == 1:
                continue
            if page_comes_after_previous(instruction[x], pages[x-1], ruleset):
                incorrect_instructions += [(instruction)]
                break

            if x == len(instruction)-1:
                correct_instructions += [(instruction)]

    return correct_instructions, incorrect_instructions


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]

    page_ordering_rules = []
    pages_for_update_rules = []

    for l in lines:
        if '|' in l:
            page_ordering_rules += [tuple(int(x) for x in l.split('|'))]
        elif ',' in l:
            pages_for_update_rules += [tuple(int(x) for x in l.split(','))]

    return page_ordering_rules, pages_for_update_rules


def no_bigger_number_in_list(x, orders, previous):
    return x in [i[1] for i in orders if i[0] == previous]


def fix_page_ordering(pageset, page_updating_rules):
    pageset = list(pageset)
    changes = 0
    pages = []
    x = 0
    while x < len(pageset):
        current_page = pageset[x]
        if len(pages) == 0:
            pages += [current_page]
            x += 1
            continue
        if no_bigger_number_in_list(current_page, page_updating_rules, pages[x - 1]):
            pages += [current_page]
        else:
            changes += 1
            pages = pages[:x - 1] + [current_page] + pages[x - 1:]
        x += 1

    if changes == 0:
        return pages
    else:
        print(f'Recursing for page {pages}')
        return fix_page_ordering(pages, page_updating_rules)


def fix_ordering_issues(badly_ordered_pages, page_updating_rules):
    print('Start part two')
    fixed_pages = []
    for pageset in badly_ordered_pages:
        fixed_pages += [fix_page_ordering(pageset, page_updating_rules)]

    print(fixed_pages)
    return fixed_pages




def solve():
    page_ordering_rules, page_rules = get_input()
    correct_instructions, incorrect_instructions = process_pages_for_update_instructions(page_rules, page_ordering_rules)
    print(find_middle_numbers(correct_instructions))
    corrected_pages = fix_ordering_issues(incorrect_instructions, page_ordering_rules)
    print(find_middle_numbers(corrected_pages))




if __name__ == "__main__":
    solve()
