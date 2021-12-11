

def score_chunk_openers(chunk_openers):
    chunk_sum = 0
    chunk_openers.reverse()
    print('Matching {}'.format(chunk_openers))
    for char in chunk_openers:
        print('Matching {}'.format(char))
        if char == '(':
            chunk_sum = (chunk_sum * 5) + 1
        if char == '[':
            chunk_sum = (chunk_sum * 5) + 2
        if char == '{':
            chunk_sum = (chunk_sum * 5) + 3
        if char == '<':
            chunk_sum = (chunk_sum * 5) + 4
        print('Chunk sum at {}'.format(chunk_sum))
    return chunk_sum


def parse_chunks(chunk_list):
    unmatched_sum = 0
    chunk_scores = []
    for chunk in chunk_list:
        print('*** Starting chunk iteration: {}, sum at {}'.format(chunk, unmatched_sum))
        pos = 0
        chunk_openers = []
        illegal = None
        for char in chunk:
            if char in ['[', '{', '(', '<']:
                chunk_openers += [char]
            else:
                opener = chunk_openers[-1]
                print('Finding closing char for {}, pos at {} and unmatched openers = {}'.format(opener, pos, chunk_openers))
                if opener == '(':
                    if chunk[pos] == ')':
                        del chunk_openers[-1]
                    else:
                        illegal = chunk[pos]
                if opener == '[':
                    if chunk[pos] == ']':
                        del chunk_openers[-1]
                    else:
                        illegal = chunk[pos]
                if opener == '{':
                    if chunk[pos] == '}':
                        del chunk_openers[-1]
                    else:
                        illegal = chunk[pos]
                if opener == '<':
                    if chunk[pos] == '>':
                        del chunk_openers[-1]
                    else:
                        illegal = chunk[pos]
                if illegal:
                    print('Expecting {}, found {} instead'.format(opener, illegal))
                    if illegal == ')':
                        unmatched_sum += 3
                    if illegal == ']':
                        unmatched_sum += 57
                    if illegal == '}':
                        unmatched_sum += 1197
                    if illegal == '>':
                        unmatched_sum += 25137
                    break

            pos += 1

        if len(chunk_openers) > 0 and not illegal:
            chunk_scores += [score_chunk_openers(chunk_openers)]
                #print('Continue matching; pos at {}, unmatched sum at {}'.format(pos, unmatched_sum))
    chunk_scores.sort()
    return unmatched_sum, chunk_scores[round(len(chunk_scores)/2)]


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
    return lines


def solve():
    daily_input = get_input()
    unmatched_sum, chunk_score = parse_chunks(daily_input)
    print('Illegal chars add up to {}'.format(unmatched_sum))
    print('Unmatched chars add up to {}'.format(chunk_score))


if __name__ == "__main__":
    solve()
