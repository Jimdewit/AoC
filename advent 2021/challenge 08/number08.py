

def find_unique_lengths(signal_list: list):
    easy_counter = 0
    for signal, code in signal_list:
        for item in code:
            for length in [2, 3, 4, 7]:
                if len(item) == length:
                    easy_counter += 1
    return easy_counter


def compare_two_letters(first, second):
    same_counter = 0
    for letter in first:
        if letter in second:
            same_counter += 1
    return same_counter


def process_length_five_and_six(fives, sixes, processed_signals):
    first_five, second_five, third_five = fives
    two = five = six = zero = nine = 0

    # Find three
    diff_first_third = compare_two_letters(first_five, third_five)
    diff_second_third = compare_two_letters(second_five, third_five)
    if diff_first_third == 4:
        if diff_second_third == 4:
            three = third_five
            two_and_five = [first_five, second_five]
        else:
            three = first_five
            two_and_five = [second_five, third_five]
    else:
        three = second_five
        two_and_five = [first_five, third_five]

    # Find zero
    for number in sixes:
        diff_three_and_six = compare_two_letters(three, number)
        if diff_three_and_six == 5:
            nine = sixes.pop(sixes.index(number))

    # Find 5 and 2
    for number in two_and_five:
        diff_nine_and_five = compare_two_letters(nine, number)
        if diff_nine_and_five == 5:
            five = two_and_five.pop(two_and_five.index(number))
            two = two_and_five[0]

    # Find 6 and 0
    for number in sixes:
        diff_five_and_six = compare_two_letters(five, number)
        if diff_five_and_six == 5:
            six = sixes.pop(sixes.index(number))
            zero = sixes[0]

    processed_signals[two] = 2
    processed_signals[three] = 3
    processed_signals[five] = 5
    processed_signals[six] = 6
    processed_signals[nine] = 9
    processed_signals[zero] = 0

    return processed_signals


def decode_signals(signal_list):
    processed_codes = 0
    for current_signals, code in signal_list:
        processed_single_code = ''
        processed_signals = {}
        fives, sixes = [], []
        for signal in current_signals:
            if len(signal) == 2:
                processed_signals[signal] = 1
            elif len(signal) == 3:
                processed_signals[signal] = 7
            elif len(signal) == 4:
                processed_signals[signal] = 4
            elif len(signal) == 5:
                fives += [signal]
            elif len(signal) == 6:
                sixes += [signal]
            elif len(signal) == 7:
                processed_signals[signal] = 8
            else:
                continue

        processed_signals = process_length_five_and_six(fives, sixes, processed_signals)
        for encoded_number in code:
            for k in processed_signals.keys():
                if len(k) == len(encoded_number) and compare_two_letters(encoded_number, k) == len(encoded_number):
                    processed_single_code += str(processed_signals[k])
        processed_codes += int(processed_single_code)

    return processed_codes


def get_input():
    with open('./input.txt', 'r') as input_file:
        signals = []
        lines = [l.strip('\n') for l in input_file.readlines()]
        for line in lines:
            signal, code = line.split(' | ')
            signals += [[signal.split(), code.split()]]
    return signals


def solve():
    daily_input = get_input()
    unique_number_count = find_unique_lengths(daily_input)
    print('Found {} unique numbers'.format(unique_number_count))
    numbers_summed = decode_signals(daily_input)
    print('Summing all codes leads to {}'.format(numbers_summed))


if __name__ == "__main__":
    solve()
