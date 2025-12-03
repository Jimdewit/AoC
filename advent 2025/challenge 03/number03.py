from datetime import datetime


def find_max_joltage(battery: str, joltage: str = '', offset: int = -1, iterations: int = 0) -> str:
    joltage += max(battery[:offset] if offset != 0 else battery)
    max_jolt_index = battery.index(max(battery[:offset] if offset != 0 else battery))

    if len(joltage) == iterations:
        return joltage
    else:
        return find_max_joltage(battery[max_jolt_index+1:], joltage, offset+1, iterations)


def process_batteries(batteries: list[str], offset: int, iterations: int):
    joltage = 0
    for b in batteries:
        battery_joltage = ''

        battery_joltage += find_max_joltage(b, offset=offset, iterations=iterations)
        joltage += int(battery_joltage)
    print(f"Total max joltage: {joltage}")


def get_input() -> list[str]:
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
    return lines


def solve():
    start = datetime.now()
    daily_input = get_input()
    process_batteries(daily_input, -1, 2)
    process_batteries(daily_input, -11, 12)
    print(f"Recursion only took {datetime.now()-start} micros")


if __name__ == "__main__":
    solve()
