import datetime
import sys

sys.setrecursionlimit(2000)

def find_neighbours(coords, route_list):
    x, y = coords
    y_neighbours = [route_list[y + 1][x]] if y == 0 else [route_list[y - 1][x]] if y == len(route_list)-1 else\
        [route_list[y - 1][x], route_list[y + 1][x]]
    x_neighbours = [route_list[y][x + 1]] if x == 0 else [route_list[y][x - 1]] if x == len(route_list[y])-1 else\
        [route_list[y][x - 1], route_list[y][x + 1]]
    return x_neighbours + y_neighbours


class Node:
    def __init__(self, node_coords, height=None, route_list=None):
        self.id = node_coords
        self.height = height
        self.adjacent = find_neighbours(node_coords, route_list)
        self.visited = False
        self.distance = 10000000
        self.previous = None

    def add_neighbours(self, route_list):
        self.adjacent = {}
        for neighbour in find_neighbours(self.id, route_list):
            if neighbour[-1] - self.height <= 1:
                self.adjacent[neighbour[0]] = 1

    def get_connections(self):
        return self.adjacent.keys()

    def get_id(self):
        return self.id

    def get_weight(self, neighbour):
        return self.adjacent[neighbour]

    def set_distance(self, dist):
        self.distance = dist

    def get_distance(self):
        return self.distance

    def set_previous(self, prev):
        self.previous = prev

    def set_visited(self):
        self.visited = True

    def __str__(self):
        return f'{str(self.id)} adjacent: {str([x for x in self.adjacent])}'


class Graph:
    def __init__(self):
        self.node_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.node_dict.values())

    def add_vertex(self, node, height=None, route_list=None):
        self.num_vertices = self.num_vertices + 1
        new_coord = Node(node, height, route_list)
        self.node_dict[node] = new_coord
        return new_coord

    def get_coord(self, n):
        if n in self.node_dict:
            return self.node_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost=0):
        if frm not in self.node_dict:
            self.add_vertex(frm)
        if to not in self.node_dict:
            self.add_vertex(to)

        self.node_dict[frm].add_neighbor(self.node_dict[to], cost)
        self.node_dict[to].add_neighbor(self.node_dict[frm], cost)

    def get_coords(self):
        return self.node_dict.keys()

    def set_previous(self, current):
        self.previous = current

    def get_previous(self, current):
        return self.previous


def shortest(v, path):
    if v.previous:
        path.append(v.previous.get_id())
        shortest(v.previous, path)
    return


import heapq


def dijkstra(vertex_graph, start, target):
    start.set_distance(0)

    # Put tuple pair into the priority queue
    unvisited_queue = [(v.get_distance(), v.id, v) for v in vertex_graph]
    heapq.heapify(unvisited_queue)

    while len(unvisited_queue):
        # Pops a vertex with the smallest distance
        unvisited = heapq.heappop(unvisited_queue)
        current = unvisited[2]
        print(f'current is {current}')
        current.set_visited()

        # for next in v.adjacent:
        if len(current.adjacent.keys()) > 0:
            for next in current.adjacent:
                print('checking stuff')
                # if visited, skip
                if next.visited:
                    continue
                new_dist = current.get_distance() + current.get_weight(next)

                if new_dist < next.get_distance():
                    next.set_distance(new_dist)
                    next.set_previous(current)
                    print(
                    'updated : current = %s next = %s new_dist = %s' \
                    % (current.get_id(), next.get_id(), next.get_distance()))
                else:
                    print(
                    'not updated : current = %s next = %s new_dist = %s' \
                    % (current.get_id(), next.get_id(), next.get_distance()))

        # Rebuild heap
        # 1. Pop every item
        while len(unvisited_queue):
            heapq.heappop(unvisited_queue)
        # 2. Put all vertices not visited into the queue
        unvisited_queue = [(v.get_distance(), v.id, v) for v in vertex_graph if not v.visited]
        heapq.heapify(unvisited_queue)

    path = [target.get_id()]
    print(f'Path is {[x for x in path]}')
    return shortest(target, path)


def get_input():
    with open('./test_input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
        y = 0
        route_list = []
        for l in lines:
            current_line = []
            for x in range(0, len(l)):
                height = ord(l[x]) - 96 if l[x] not in ('S', 'E') else 0 if l[x] == 'S' else 27
                current_line.append(((x, y), height))
            route_list.append(current_line)
            y += 1

        g = Graph()
        y = 0
        for l in lines:
            for x in range(0, len(l)):
                height = ord(l[x])-96 if l[x] not in ('S', 'E') else 0 if l[x] == 'S' else 27
                if l[x] == 'S':
                    start_coord = (x, y)
                if l[x] == 'E':
                    target_coord = (x, y)
                g.add_vertex((x, y), height, route_list)
                coord = g.get_coord((x,y))
                coord.add_neighbours
            y += 1
    return g, start_coord, target_coord


def solve():
    start = datetime.datetime.now()
    daily_input, start_coord, target_coord = get_input()
    shortest_path = dijkstra(daily_input, daily_input.get_coord(start_coord), daily_input.get_coord(target_coord))
    print(f'The shortest path is {shortest_path}, time taken {datetime.datetime.now() - start}')


if __name__ == "__main__":
    solve()
