

def route_check(routes, coords, current_route):
    for r in routes:
        for r2 in routes:
            if r[-1] < r2[-1]:
                print(1)


def cheapest_path(cave_chart, m, n):
    # Instead of following line, we can use int tc[m + 1][n + 1] or
    # dynamically allocate memory to save space. The following
    # line is used to keep te program simple and make it working
    # on all compilers.
    tc = [[0 for x in range(len(cave_chart[0]))] for x in range(len(cave_chart))]

    tc[0][0] = 0

    # Initialize first column of total cost(tc) array
    for i in range(1, m + 1):
        tc[i][0] = tc[i - 1][0] + cave_chart[i][0]

    # Initialize first row of tc array
    for j in range(1, n + 1):
        tc[0][j] = tc[0][j - 1] + cave_chart[0][j]

    # Construct rest of the tc array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            tc[i][j] = min(tc[i - 1][j],
                           tc[i + 1][j] if i + 1 < m+1 else 100,
                           tc[i][j - 1],
                           tc[i][j + 1] if j + 1 < n+1 else 100) + cave_chart[i][j]

    print(tc)
    return tc[m][n]


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
        height_list = []
        for l in lines:
            single_line = []
            for x in l:
                single_line += [int(x)]
            height_list += [single_line]
    return height_list


def solve():
    daily_input = get_input()
    print(cheapest_path(daily_input, len(daily_input)-1, len(daily_input)-1))
    #print('Total risk equals {}'.format(score_heights(daily_input)))


if __name__ == "__main__":
    solve()