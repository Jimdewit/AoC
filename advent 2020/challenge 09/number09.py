class Constants:
    def __init__(self):
        pass

    PREAMBLE_LENGTH = 5


def get_input():
    with open('./test_input.txt', 'r') as file:
        return [int(x[:-1]) for x in file]


def list_parser(code, preamble_length):
    for x in code:
        if code.index(x) < preamble_length:
            continue
        subset = code[(code.index(x) - preamble_length):code.index(x)]
        match_found = False
        for y in subset:
            z = x-y
            if z in subset and (z != y or subset.count(y) == 1):
                match_found = True
                continue
            else:
                continue
        if not match_found:
            return x


def find_summable_set(code, number):
    matching_set_found = False

    for x in code:
        matching_set = [x]
        pos = code.index(x)+1
        while not matching_set_found:
            matching_set += [code[pos]]
            pos += 1
            if sum(matching_set) > number:
                break
            elif sum(matching_set) == number:
                return sorted(matching_set)[0] + sorted(matching_set)[len(matching_set)-1]
            else:
                continue


def main():
    code = get_input()
    broken_number = list_parser(code, Constants.PREAMBLE_LENGTH)
    print("Found a number that's not properly summed: {}".format(broken_number))
    final_number = find_summable_set(code, broken_number)
    print("Found final number {}".format(final_number))



if __name__ == "__main__":
    main()