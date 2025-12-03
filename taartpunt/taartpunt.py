import copy
import random


class Taartpunt:
    def __init__(self, a, b, c, d, e, f):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.lst = [self.a, self.b, self.c, self.d, self.e, self.f]
        self.slv = copy.deepcopy(self.lst)

    def randomise(self):
        letter_to_replace = random.randint(0, 5)
        self.lst[letter_to_replace] = '?'
        starting_letter = random.randint(0, 5)
        self.lst = self.lst[starting_letter:] + self.lst[:starting_letter]
        self.slv = self.slv[starting_letter:] + self.slv[:starting_letter]
        self.direction = random.randint(0, 1) # 0 for clockwise, 1 for counter-clockwise
        self.direction = 1
        self.lst = list(reversed(self.lst)) if self.direction == 1 else self.lst
        self.slv = list(reversed(self.slv)) if self.direction == 1 else self.slv

    def solution(self):
        empty_grid = f"""
        {'<--' if self.direction == 1 else '-->'}
       ______
      /\\  {self.slv[5]} /\\
     /{self.slv[4]} \\  / {self.slv[0]}\\
    /____\\/____\\
    \\    /\\    /
     \\{self.slv[3]} /  \\ {self.slv[1]}/
      \\/_{self.slv[2]}__\\/

"""
        print(empty_grid)

    def puzzle(self):
        empty_grid = f"""
       ______
      /\\  {self.lst[5]} /\\
     /{self.lst[4]} \\  / {self.lst[0]}\\
    /____\\/____\\
    \\    /\\    /
     \\{self.lst[3]} /  \\ {self.lst[1]}/
      \\/_{self.lst[2]}__\\/

"""
        print(empty_grid)


def process():
    word = 'MOEITE'
    taart = Taartpunt(*word)
    taart.randomise()
    print('PUZZEL')
    taart.puzzle()
    print('OPLOSSING')
    taart.solution()


if __name__ == '__main__':
    process()
