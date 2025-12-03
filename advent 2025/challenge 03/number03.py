from datetime import datetime


def find_max_joltage(battery: str, joltage: str = '', offset: int = -1, iterations: int = 0) -> str:
    joltage += max(battery[:offset] if offset != 0 else battery)
    max_jolt_index = battery.index(max(battery[:offset] if offset != 0 else battery))

    if len(joltage) == iterations:
        return joltage
    else:
        return find_max_joltage(battery[max_jolt_index+1:], joltage, offset+1, iterations)


def process_batteries_part_one(batteries: list[str]):
    joltage = 0
    for b in batteries:
        battery_joltage = ''

        battery_joltage += find_max_joltage(b, iterations=2)
        joltage += int(battery_joltage)
    print(f"Total max joltage: {joltage}")


def process_batteries_part_two(batteries: list[str]):
    joltage = 0
    for b in batteries:
        battery_joltage = ''

        battery_joltage += find_max_joltage(b, offset=-11, iterations=12)
        joltage += int(battery_joltage)
    print(f"Total max joltage: {joltage}")


def get_input() -> list[str]:
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
    return lines


def solve():
    start = datetime.now()
    daily_input = get_input()
    process_batteries_part_one(daily_input)
    process_batteries_part_two(daily_input)
    print(f"Recursion only took {datetime.now()-start} micros")


if __name__ == "__main__":
    solve()
