def get_input():
    with open('./input.txt', 'r') as file:
        return [[f[:-1][0], int(f[:-1][1:])] for f in file]


def process_directions(directionset, use_waypoint=False, debug_mode=False):
    north = 0
    east = 0
    wp = [1, 10]
    heading = 1
    for instruction, amount in directionset:
        # Process ship rotations - heading is mapped starting at 0 for North, and increasing clockwise
        if instruction == 'L':
            heading = int(heading - amount/90 if heading - amount/90 >= 0 else 4 - abs(heading - amount/90))
        elif instruction == 'R':
            heading = int(heading + amount/90 if heading + amount/90 <= 3 else (heading + amount/90) - 4)

        # Process waypoint rotations
        if instruction in ['L', 'R'] and use_waypoint:
            if amount == 90:
                wp = [wp[1], -wp[0]] if instruction == 'L' else [-wp[1], wp[0]]
            elif amount == 180:
                wp = [-wp[0], -wp[1]]
            elif amount == 270:
                wp = [-wp[1], wp[0]] if instruction == 'L' else [wp[1], -wp[0]]
            else:
                raise

        # Process absolute motion
        if not use_waypoint:
            north = north + amount if (instruction == 'N') else north - amount if (instruction == 'S') else north
            east = east + amount if (instruction == 'E') else east - amount if (instruction == 'W') else east
        else:
            wp[0] = wp[0] + amount if (instruction == 'N') else wp[0] - amount if (instruction == 'S') else wp[0]
            wp[1] = wp[1] + amount if (instruction == 'E') else wp[1] - amount if (instruction == 'W') else wp[1]

        # Process forward motion
        if instruction == 'F':
            if not use_waypoint:
                north = north + amount if heading == 0 else north - amount if heading == 2 else north
                east = east + amount if heading == 1 else east - amount if heading == 3 else east
            else:
                north += wp[0] * amount
                east += wp[1] * amount

        if debug_mode:
            print("Finished processing {}{} with heading {}, North at {} and East at {}\nWaypoint at (N{},E{})".format(instruction, amount, heading, north, east, wp[0], wp[1]))
    return abs(north) + abs(east)


def main():
    directions = get_input()
    manhattan_distance = process_directions(directions)
    manhattan_distance2 = process_directions(directions, use_waypoint=True)
    print("Part 1: found Manhattan distance {}".format(manhattan_distance))
    print("Part 2: found Manhattan distance {}".format(manhattan_distance2))


if __name__ == "__main__":
    main()