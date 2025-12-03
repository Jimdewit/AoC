class OpCode:
    def __init__(self, instruction: int, first_address: int | None = None, second_address: int | None = None,
                 target_address: int | None = None):
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

    def get_operation(self, start: int) -> OpCode | None:
        inst = self._opcodes[start]
        if inst == 99:
            return OpCode(inst)
        if inst in [1, 2]:
            return OpCode(self._opcodes[start], self._opcodes[start + 1], self._opcodes[start + 2], self._opcodes[start + 3])
        if inst == 3:
            return OpCode(self._opcodes[start], self._opcodes[start + 1], self._opcodes[start + 2], self._opcodes[start + 3])
        return None


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
