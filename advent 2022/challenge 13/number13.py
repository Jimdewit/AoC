import json


def process_list_and_list(p1, p2):
    # print(f'Processing {p1} and {p2}')
    for x in range(0, len(p1)):
        try:
            if type(p1[x]) != type(p2[x]):
                #print(f'{type(p1[x])} for {p1[x]} and {type(p2[x])} for {p2[x]} are not compatible; harmonizing!')
                return harmonize_and_process_pair(p1[x], p2[x])
            if isinstance(p1[x], list) and isinstance(p2[x], list):
                #print(f'Unpacking lists {p1[x]} and {p2[x]}')
                return harmonize_and_process_pair(p1[x], p2[x])
            if p1[x] > p2[x]:
                return False
            if p1[x] < p2[x]:
                #print(f'Smaller is true for {p1[x]} AND {p2[x]}\n(from lists {p1} AND {p2})\n')
                return True
        except IndexError as e:
            return False
        # if x == 0 and len(p1) == len(p2) and p1[x] == p2[x]:
        #     return False

    print(f'Left {p1} ran out faster than {p2}')

    return True

def process_int_and_int(p1, p2):
    if p1 < p2:
        return True
    else:
        return False


def process_int_and_list(p1, p2):
    p1 = [p1]
    return p1, p2


def process_list_and_int(p1, p2):
    p2 = [p2]
    return p1, p2


def harmonize_and_process_pair(p1, p2):
    if type(p1) == type(p2):
        # print(f'process_{type(p1).__name__}_and_{type(p2).__name__}({p1}, {p2})')
        p1_is_smaller = eval(f'process_{type(p1).__name__}_and_{type(p2).__name__}({p1}, {p2})')
        return p1_is_smaller
    else:
        p1, p2 = eval(f'process_{type(p1).__name__}_and_{type(p2).__name__}({p1}, {p2})')
        return harmonize_and_process_pair(p1, p2)


def process_pairs(list_of_pairs):
    list_counter = 0
    valid_counter = 0
    for p1, p2 in list_of_pairs:
        is_valid_message = harmonize_and_process_pair(p1, p2)
        if is_valid_message:
            # print(f'counter {valid_counter} + {list_counter} because p1 smaller is {is_valid_message} for {p1} and {p2}')
            valid_counter += list_counter
        list_counter += 1
    print(valid_counter)



def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
        list_pairs = []
        current_set = []
        for l in lines:
            if len(l) == 0:
                list_pairs += [current_set]
                current_set = []
            else:
                l = json.loads(l)
                current_set += [l]
        list_pairs += [current_set]

    return list_pairs


def solve():
    list_of_pairs = get_input()
    process_pairs(list_of_pairs)


if __name__ == "__main__":
    solve()
