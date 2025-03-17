class Plot:
    def __init__(self, x: int, y: int, crop_type: str):
        self.x = x
        self.y = y
        self.crop_type = crop_type

    def __eq__(self, other):
        if not isinstance(other, Plot):
            # don't attempt to compare against unrelated types
            return NotImplemented

        return self.x == other.x and self.y == other.y


def find_adjacent_plots(plot: Plot, all_plots: list[list[Plot]], search_crop: str, y_bound: int, x_bound: int, region: list):
    x = plot.x
    y = plot.y
    left = all_plots[y][x-1] if x-1 >= 0 and all_plots[y][x-1].crop_type == search_crop and all_plots[y][x-1] not in region else None
    right = all_plots[y][x+1] if x+1 < x_bound and all_plots[y][x+1].crop_type == search_crop and all_plots[y][x+1] not in region else None
    above = all_plots[y-1][x] if y-1 >= 0 and all_plots[y-1][x].crop_type == search_crop and all_plots[y-1][x] not in region else None
    below = all_plots[y+1][x] if y+1 < y_bound and all_plots[y+1][x].crop_type == search_crop and all_plots[y+1][x] not in region else None

    return [a for a in [left, right, above, below] if a]


def find_region_for_plot(plot: Plot, all_plots: list[list[Plot]], search_crop: str, y_bound: int, x_bound: int, region=None):
    if not region:
        region = [plot]
    for r in region:
        adjacents = find_adjacent_plots(r, all_plots, search_crop, y_bound, x_bound, region)
        while len(adjacents) > 0:
            a = adjacents.pop()
            region += [a]
            return find_region_for_plot(plot, all_plots, search_crop, y_bound, x_bound, region)

    return region


def find_regions(plots: list[list[Plot]]):
    y_bound = len(plots)
    x_bound = len(plots[0])
    regions = []
    current_region_letter = ''
    for y in plots:
        for x in y:
            for r in regions:
                for r2 in r:
                    if r2 == x:
                        continue
            current_region_letter = x.crop_type if current_region_letter == '' else current_region_letter
            regions += [find_region_for_plot(x, plots, current_region_letter, y_bound, x_bound)]

    print(f'Found regions {regions}')


def get_input() -> list:
    with open('./test_input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]

    plots = []
    y = 0
    for l in lines:
        plots += [[]]
        x = 0
        for c in l:
            plots[y] += [Plot(x, y, c)]
            x += 1
        y += 1

    return plots


def solve():
    daily_input = get_input()
    print(daily_input)
    find_regions(daily_input)


if __name__ == "__main__":
    solve()
