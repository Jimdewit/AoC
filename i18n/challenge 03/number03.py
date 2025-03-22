import re


def has_number(inp):
    num_regex = re.compile('[0-9]')
    return len(re.findall(num_regex, inp)) > 0


def has_uppercase_char(inp):
    for i in inp:
        if i.isupper():
            return True
    return False


def has_lowercase_char(inp):
    for i in inp:
        if i.islower():
            return True
    return False


def has_special_char(inp):
    special_regex = re.compile('[À-ỿ]')
    return len(re.findall(special_regex, inp)) > 0


def has_valid_length(inp):
    return 4 <= len(inp) <= 12


def password_is_valid(inp):
    valid = has_valid_length(inp) and has_lowercase_char(inp) and has_uppercase_char(inp) and has_number(inp) and has_special_char(inp)
    print(f"valid: {valid}: {inp}")
    return has_valid_length(inp) and has_lowercase_char(inp) and has_uppercase_char(inp) and has_number(inp) and has_special_char(inp)


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
    return lines


def solve():
    daily_input = get_input()
    valid = 0
    for i in daily_input:
        valid += 1 if password_is_valid(i) else 0
    print(valid)


if __name__ == "__main__":
    solve()
