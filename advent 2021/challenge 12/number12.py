from collections import Counter


def find_next_points(possible_routes, route_list, finished_routes=[], multiple_visits=False):
    new_routes = []
    for route in possible_routes:
        last = route[-1]
        if last == 'end':
            if route not in finished_routes:
                finished_routes += [route]
            continue
        for elem in route_list:
            if last in elem:
                if 'end' in elem and 'end' not in route:
                    new_routes += [route + ['end']]
                elif 'start' not in elem:
                    if elem[1] == last:
                        if elem[0].islower():
                            if not multiple_visits:
                                if elem[0] not in route:
                                    new_routes += [[l for l in route] + [elem[0]]]
                            else:
                                if 2 not in Counter(l for l in route if l.islower()).values() and multiple_visits:
                                    new_routes += [[l for l in route] + [elem[0]]]
                                elif elem[0] not in route:
                                    new_routes += [[l for l in route] + [elem[0]]]
                        elif [elem[0], last, elem[0]] not in route:
                            new_routes += [[l for l in route] + [elem[0]]]
                        else:
                            continue
                    elif elem[0] == last:
                        if elem[1].islower():
                            if not multiple_visits:
                                if elem[1] not in route:
                                    new_routes += [[l for l in route] + [elem[1]]]
                            else:
                                if 2 not in Counter(l for l in route if l.islower()).values() and multiple_visits:
                                    new_routes += [[l for l in route] + [elem[1]]]
                                elif elem[1] not in route:
                                    new_routes += [[l for l in route] + [elem[1]]]
                        elif [elem[1], last, elem[1]] not in route:
                            new_routes += [[l for l in route] + [elem[1]]]
                        else:
                            continue
                    else:
                        continue
                else:
                    continue
    possible_routes = new_routes
    if len(new_routes) > 0:
        print('Continuing search, found {} routes so far'.format(len(finished_routes)))
        return find_next_points(possible_routes, route_list, finished_routes, multiple_visits=multiple_visits)
    return finished_routes


def find_starts(route_list):
    possible_routes = []
    for elem in route_list:
        if 'start' in elem:
            possible_routes += [[elem[0], elem[1]]] if elem[0] == 'start' else [[elem[1], elem[0]]]
    return possible_routes


def process_routes(route_list, multiple_visits=False):
    starts = find_starts(route_list)
    routes = find_next_points(starts, route_list, multiple_visits=multiple_visits)
    return routes


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [[x, y] for x, y in [l.strip('\n').split('-') for l in input_file.readlines()]]
    return lines


def solve():
    daily_input = get_input()
    routes = process_routes(daily_input)
    print("Found a grand total of {} routes".format(len(routes)))
    scenic_routes = process_routes(daily_input, multiple_visits=True)
    print("Taking the scenic route generates a possible {} routes".format(len(scenic_routes)))

if __name__ == "__main__":
    solve()
