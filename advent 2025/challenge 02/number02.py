import re


def validate_ids(ids: list[str]):
    total = 0
    for id in ids:
        rng = id.split('-')
        for i in range(int(rng[0]), int(rng[1])+1):
            if len(str(i)) % 2 != 0 or str(i).startswith('0'):
                continue
            stri = str(i)
            first = stri[:int(len(stri)/2)]
            second = stri[int(len(stri)/2):]
            if first == second:
                total += int(i)
    print(total)


def build_re(match_str: str):
    regex = re.compile(f"^{match_str}({match_str})+$")
    return regex


def regex_validate_ids(ids: list[str]):
    total = 0
    l = len(ids)
    cnt = 0
    for id in ids:
        rng = id.split('-')
        for i in range(int(rng[0]), int(rng[1])+1):
            if str(i).startswith('0'):
                continue
            stri = str(i)
            for x in range(int(len(stri)/2)):
                rx = build_re(stri[:x+1])

                if re.match(rx, stri):
                    print(f"invalid: {stri}")

                    total += int(i)
                    break
        cnt += 1
        if int(l/cnt) % 100 == 0:
            print(f"currently at {cnt}/{l}")

    print(total)


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
        ids = lines[0].split(',')
    return ids


def solve():
    daily_input = get_input()
    print(daily_input)
    validate_ids(daily_input)
    regex_validate_ids(daily_input)

if __name__ == "__main__":
    solve()
