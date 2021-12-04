

def bingo_finder(bingo_card):
    for letter in ['B', 'I', 'N', 'G', 'O']:
        seen_bits_in_column = 0
        for x in range(0, 5):
            if bingo_card[letter][x]['seen'] == 1:
                seen_bits_in_column += 1
        if seen_bits_in_column == 5:
            return True

    for x in range(0, 5):
        column_seen_bits = 0
        for letter in ['B', 'I', 'N', 'G', 'O']:
            if bingo_card[letter][x]['seen'] == 1:
                column_seen_bits += 1
        if column_seen_bits == 5:
            return True

    return False


def process_single_card(bingo_card, ordered_numbers):
    bingo_numbers_seen = 0
    for bingo_number in ordered_numbers:
        bingo_numbers_seen += 1
        for letter in ['B', 'I', 'N', 'G', 'O']:
            for x in range(0, 5):
                number, seen = bingo_card[letter][x].values()
                if number == bingo_number:
                    bingo_card[letter][x]['seen'] = 1
                    if bingo_finder(bingo_card):
                        return bingo_numbers_seen, bingo_number, bingo_card


def score_bingo_cards(ordered_numbers, bingo_cards, find_best=True):
    current_best = len(ordered_numbers) if find_best else 0
    best_bingo_card = {}
    for card in bingo_cards:
        card_counter, winning_number, processed_card = process_single_card(card, ordered_numbers)
        if find_best:
            if card_counter < current_best:
                current_best = card_counter
                best_bingo_card = {'winning_card': processed_card, 'card_counter': card_counter, 'winning_number': winning_number}
                print('Requiring only {} numbers, with winning number {} the best bingo card is {}'.format(
                    best_bingo_card['card_counter'], best_bingo_card['winning_number'],
                    best_bingo_card['winning_card']))
        else:
            if card_counter > current_best:
                current_best = card_counter
                best_bingo_card = {'winning_card': processed_card, 'card_counter': card_counter, 'winning_number': winning_number}
                print('Requiring no less than {} numbers, with winning number {} the worst bingo card is {}'.format(
                    best_bingo_card['card_counter'], best_bingo_card['winning_number'],
                    best_bingo_card['winning_card']))

    return sum_bingo_card_numbers(best_bingo_card['winning_card']) * best_bingo_card['winning_number']


def sum_bingo_card_numbers(bingo_card):
    unseen_number_sum = 0
    for letter in ['B', 'I', 'N', 'G', 'O']:
        for x in range(0, 5):
            if bingo_card[letter][x]['seen'] == 0:
                unseen_number_sum += bingo_card[letter][x]['number']
    return unseen_number_sum


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
        bingo_cards = []
        bingo_numbers = [int(x) for x in lines.pop(0).split(',')]
        # get rid of first empty line
        lines.pop(0)

        row_counter = 0
        bingo_card = {'B': {}, 'I': {}, 'N': {}, 'G': {}, 'O': {}}
        for line in lines:
            split_line = line.split()
            if len(split_line) == 0:
                bingo_cards += [bingo_card]
                row_counter = 0
                bingo_card = {'B': {}, 'I': {}, 'N': {}, 'G': {}, 'O': {}}
                continue

            bingo_card['B'][row_counter] = {'number': int(split_line[0]), 'seen': 0}
            bingo_card['I'][row_counter] = {'number': int(split_line[1]), 'seen': 0}
            bingo_card['N'][row_counter] = {'number': int(split_line[2]), 'seen': 0}
            bingo_card['G'][row_counter] = {'number': int(split_line[3]), 'seen': 0}
            bingo_card['O'][row_counter] = {'number': int(split_line[4]), 'seen': 0}
            row_counter += 1

    bingo_cards += [bingo_card]
    return bingo_cards, bingo_numbers


def solve():
    bingo_cards, bingo_numbers = get_input()
    print('Multiplication of winning number and unseen numbers equals {}'.format(score_bingo_cards(bingo_numbers, bingo_cards)))
    bingo_cards, bingo_numbers = get_input()
    print('Multiplication of winning number and unseen numbers equals {}'.format(score_bingo_cards(bingo_numbers, bingo_cards, find_best=False)))


if __name__ == "__main__":
    solve()