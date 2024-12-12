import numpy as np


def check_array(array: list[int]) -> bool:
    # Get differences
    a = np.diff(array)
    # If all are in range then return true
    return np.all((a>=1) & (a<=3)) | np.all((a<=-1) & (a>=-3))


def check_safe_row(row: list[int], part2: bool) -> bool:
    if check_array(row):
        return True
    if part2:
        for i in range(len(row)):
            if check_array(row[:i] + row[i+1:]):
                return True
    return False


# Parse input
data = [[int(x) for x in line.split()] for line in open('./input.txt')]

# Part 1
print(f'Part 1: {sum(check_safe_row(row, False) for row in data)}')
# Part 2
print(f'Part 2: {sum(check_safe_row(row, True) for row in data)}')