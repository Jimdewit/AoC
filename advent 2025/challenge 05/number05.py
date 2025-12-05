from datetime import datetime


def check_freshness(ranges, i):
    for min_fresh, max_fresh in [range for range in ranges]:
        if min_fresh < i <= max_fresh:
            return 1
    return 0


def find_fresh_part_one(ranges, ingredients):
    fresh = 0
    for i in ingredients:
        fresh += check_freshness(ranges, int(i))
    print(f"Fresh count {fresh}")


def sort_and_merge_ranges(ranges):
    ranges.sort(key=lambda tup: tup[0])
    intervals = []
    current_start, current_end = ranges[0][0], ranges[0][1]
    for next_start, next_end in [ra for ra in ranges[1:]]:
        if current_end < next_start:
            intervals.append((current_start, current_end))
            current_start, current_end = next_start, next_end
        else:
            current_end = max(current_end, next_end)

    intervals.append((current_start, current_end))

    return intervals


def find_fresh_part_two_smart(ranges):
    start = datetime.now()
    print("STARTING FRESHER")

    merged = sort_and_merge_ranges(ranges)

    # range is inclusive
    print(f"Total amount of fresh ingredients: {sum(r[1]+1 - r[0] for r in merged)}")
    print(f"Finding fresh ingredients took {datetime.now() - start} - and it didn't crash!")


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
    ranges = []
    ingredients = []
    for l in lines:
        if len(l.split('-')) == 2:
            ranges.append((int(l.split('-')[0]), int(l.split('-')[1])))
        elif len(l) == 0:
            continue
        else:
            ingredients.append(l)
    return ranges, ingredients


def solve():
    ranges, ingredients = get_input()
    find_fresh_part_one(ranges, ingredients)
    # find_fresh_part_two(ranges)
    find_fresh_part_two_smart(ranges)


if __name__ == "__main__":
    solve()
