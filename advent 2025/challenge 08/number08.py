class Coord:
    def __init__(self, x: int, y: int, z: int):
        self._x = x
        self._y = y
        self._z = z
        self._circuit: int | None = None

    @property
    def x(self) -> int:
        return self._x

    @property
    def y(self) -> int:
        return self._y

    @property
    def z(self) -> int:
        return self._z

    @property
    def circuit(self) -> int:
        return self._circuit

    @circuit.setter
    def circuit(self, circuit: int):
        self._circuit = circuit

    @staticmethod
    def from_string(coord_string: str) -> 'Coord':
        x, y, z = coord_string.split(',')
        return Coord(int(x), int(y), int(z))


def get_distance(a: Coord, b: Coord) -> int:
    return (a.x - b.x)**2 + (a.y - b.y)**2 + (a.z - b.z)**2


def process_inputs(junction_boxes: list[Coord]):
    circuits = {}
    dists = []
    for a in junction_boxes:
        for b in junction_boxes:
            if a == b:
                continue
            dists.append((a, b, get_distance(a, b)))
    dists.sort(key=lambda tup: tup[2])

    deduped_dists = dists[::2]

    x = 0
    iterations = 0
    for a, b, dist in deduped_dists:
        if iterations == 10:
            res = 1
            for k in sorted(circuits, key=lambda key: len(circuits[key]), reverse=True)[:3]:
                print(f"Circuit {k} has length {len(circuits[k])}")
                res *= len(circuits[k])
            print(f"Part one: {res}")
        iterations += 1

        if a.circuit is None and b.circuit is None:
            x += 1
            a.circuit = x
            b.circuit = x
            circuits[x] = []
            circuits[x].append(a)
            circuits[x].append(b)
        elif a.circuit is not None and b.circuit is not None:
            if a.circuit != b.circuit:
                old_b = b.circuit
                for bb in circuits[b.circuit]:
                    bb.circuit = a.circuit
                    circuits[a.circuit].append(bb)
                circuits[old_b] = []
        elif b.circuit is not None:
            a.circuit = b.circuit
            circuits[b.circuit].append(a)
        elif a.circuit is not None:
            b.circuit = a.circuit
            circuits[a.circuit].append(b)

        if iterations > 10:
            if len(circuits[a.circuit]) == len(junction_boxes):
                print(f"Part two:{a.x * b.x}")
                break

    print("All done?")


def get_input() -> list[Coord]:
    with open('./input.txt', 'r') as input_file:
        lines = [Coord.from_string(l.strip('\n')) for l in input_file.readlines()]
    return lines


def solve():
    daily_input = get_input()
    process_inputs(daily_input)


if __name__ == "__main__":
    solve()
