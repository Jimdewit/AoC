from operator import xor

def solve():
    raw = get_input('./input.txt')
    proper, wrong = check(raw)
    # proper, wrong = check(raw, position_check=True)
    print("Okay are: {}, wrong are: {}".format(proper, wrong))
    print("Total okay: {}".format(len(proper)))


def check(input_dict, position_check=False):

    proper_passwords = wrong_passwords = []
    fine = wrong = 0
    for key in input_dict:
        values = input_dict.get(key)
        min, max = values[0][0], values[0][1]
        letter_to_check = values[1]
        password = values[2]
        if position_check:
            if xor((password[min-1] == letter_to_check), (password[max-1] == letter_to_check)):
                print('{} is fine ({} in {} or {})'.format(password, letter_to_check, min-1, max-1))
                proper_passwords.append(password)
                fine += 1
            else:
                print('{} is wrong ({} occurrences)'.format(password, password.count(letter_to_check)))
                wrong_passwords.append(password)
                wrong += 1
        else:
            if min <= password.count(letter_to_check) <= max:
                print('{} is fine'.format(password))
                proper_passwords.append(password)
                fine += 1
            else:
                print('{} is wrong ({} occurrences)'.format(password, password.count(letter_to_check)))
                wrong_passwords.append(password)
                wrong += 1

    print("Fine: {}\nWrong: {}".format(fine, wrong))
    return proper_passwords, wrong_passwords


def get_input(inputfile):
    with open(inputfile, 'r') as keys:
        values = {}
        y = 0
        for key in keys:
            separated = key[:-1].split(' ')
            sizes = [int(x) for x in separated[0].split('-')]
            letter = separated[1][0]
            password = separated[2]

            values[y] = sizes, letter, password
            y += 1

        return values


def read_keys(raw):
    print(1)


if __name__ == "__main__":
    solve()