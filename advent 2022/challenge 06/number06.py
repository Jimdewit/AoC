
def find_start_marker(code, look_for_marker=True):
    start = 0
    if look_for_marker:
        for x in range(0, len(code)-3):
            potential_marker = code[start:start+4]
            if len(set(potential_marker)) == 4:
                return start+4
            else:
                start += 1
    else:
        for x in range(0, len(code) - 13):
            potential_message = code[start:start + 14]

            if len(set(potential_message)) == 14:
                return start+14
            else:
                start += 1


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()][0]
    return lines


def solve():
    encrypted_signal = get_input()
    print(find_start_marker(encrypted_signal))
    print(find_start_marker(encrypted_signal, look_for_marker=False))


if __name__ == "__main__":
    solve()
