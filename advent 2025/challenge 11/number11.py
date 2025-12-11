def count_paths(routes, start, end):
    if start not in routes:
        return 0

    # store how many paths from curr(dict key) to end
    cache = {}

    def dfs(curr, end):
        if curr == end:
            return 1
        if curr in cache:
            return cache[curr]

        count = sum(dfs(_next, end) for _next in routes.get(curr, []))
        cache[curr] = count
        return count

    return dfs(start, end)


def part_two(interfaces):
    count1a = count_paths(interfaces, 'svr','fft')
    count1b = count_paths(interfaces, 'fft','dac')
    count1c = count_paths(interfaces, 'dac','out')
    count1 = count1a * count1b * count1c

    count2a = count_paths(interfaces, 'svr','dac')
    count2b = count_paths(interfaces, 'dac','fft')
    count2c = count_paths(interfaces, 'fft','out')
    count2 = count2a * count2b * count2c

    print(f"Part two: {count1 + count2}")


def get_input():
    server_interfaces = {}
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]

    for k, v in [l.split(':') for l in lines]:
        server_interfaces[k] = v.strip().split(' ')
    return server_interfaces


def solve():
    daily_input = get_input()
    print(f"Part one: {count_paths(daily_input, 'you','out')}")
    part_two(daily_input)


if __name__ == "__main__":
    solve()
