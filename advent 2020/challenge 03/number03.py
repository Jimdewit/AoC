def solve(route_steps):
    empty_list = []
    for route_step in route_steps:
        number_of_trees = pos = line_counter = 0
        with open('./input.txt', 'r') as roadmap:
            for line in roadmap:
                new_pos = pos + route_step
                while len(line[:-1]) < pos + 1:
                    line = line[:-1] + line
                if line[pos] == '#':
                    number_of_trees += 1
                # if route_step == 7:
                #     print("Line {}: {}, at position {} (python index {})".format(line_counter, line[pos], pos + 1, pos))
                #     print("Line {}: {}".format(line_counter, line))
                pos = new_pos
                line_counter += 1
                # if pos > 100:
                #     break
        empty_list += [number_of_trees]

    with open('./input.txt', 'r') as roadmap:
        skipper = False
        number_of_trees = pos = line_counter = 0
        for line in roadmap:
            line_counter += 1
            new_pos = pos + 1
            if skipper:
                print("Skipping line {}".format(line_counter))
                skipper = False
                continue
            while len(line[:-1]) < pos + 1:
                line = line[:-1] + line
            print("Line {}: {}, at position {} (python index {})".format(line_counter, line[pos], pos+1, pos))
            print("Line {}: {}".format(line_counter,line))
            if line[pos] == '#':
                number_of_trees += 1
            pos = new_pos
            skipper = True
            # if pos > 20:
            #     break
        empty_list += [number_of_trees]

    print(empty_list)

    x = 1
    for y in empty_list:
        x = x*y

    print(x)
    print(87 * 278 * 88 * 98 * 43)

if __name__ == "__main__":
    route_steps = [1, 3, 5, 7]
    # route_steps = [7]
    solve(route_steps)


    # TODO: 8968942752 and 9278216640 are incorrect