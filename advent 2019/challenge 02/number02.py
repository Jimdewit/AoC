class OpCode:
    def __init__(self, instruction, first_address, second_address, target_address):
        self._instruction = instruction
        self._first_address = first_address
        self._second_address = second_address
        self._target_address = target_address

    @property
    def instruction(self):
        return self._instruction

    @property
    def first_address(self):
        return self._first_address

    @property
    def second_address(self):
        return self._second_address

    @property
    def target_address(self):
        return self._target_address


class Memory:
    def __init__(self, opcodes: list[int]):
        self._opcodes = opcodes

    @property
    def opcodes(self):
        return self._opcodes

    def get_operation(self, start: int) -> OpCode:
        return OpCode(self._opcodes[start], self._opcodes[start + 1], self._opcodes[start + 2], self._opcodes[start + 3])

    def process_operation(self, opcode: OpCode) -> int:
        if opcode.instruction == 99:
            return -1

        if opcode.instruction == 1:
            self._opcodes[opcode.target_address] = self._add(opcode.first_address, opcode.second_address)
        if opcode.instruction == 2:
            self._opcodes[opcode.target_address] = self._mult(opcode.first_address, opcode.second_address)

        return 4

    def _add(self, one, two):
        return self._opcodes[one] + self._opcodes[two]

    def _mult(self, one, two):
        return self._opcodes[one] * self._opcodes[two]


def process_opcodes(input_list):
    x = 0
    offset = 0
    opcodes = Memory(input_list)
    while offset >= 0:
        opcode = opcodes.get_operation(x)
        offset = opcodes.process_operation(opcode)
        x += offset

    return opcodes.opcodes


def part_one(inp):
    inp[1] = 12
    inp[2] = 2
    print(process_opcodes(inp)[0])


def part_two(inp):
    for x in range(0, 100):
        for y in range(0, 100):
            test_inp = inp.copy()
            test_inp[1] = x
            test_inp[2] = y
            res = process_opcodes(test_inp)
            if res[0] == 19690720:
                print(f"Got {x} and {y}, result = {x*100+y}")
                break
        else:
            continue

        break


def get_input():
    with open('./input.txt', 'r') as inputfile:
        return [int(x) for x in inputfile.readline().rstrip('\n').split(',')]


def main():
    code = get_input()
    part_one(code)
    code = get_input()
    part_two(code)


if __name__ == "__main__":
    main()