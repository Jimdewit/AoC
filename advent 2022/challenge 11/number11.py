import copy
from datetime import datetime
from math import floor

debug = True

def resolve_monkey_business(monkeys, modulo, number_of_times):
    monkeys = copy.deepcopy(monkeys)
    start = datetime.now()
    for y in range(0, number_of_times):
        for x in range(0, len(monkeys.keys())):
            monkey = monkeys[x]
            if len(monkey['Items']) == 0:
                continue

            for current_value in monkey['Items']:
                operator, value = monkey['Operation'].split()[-2], int(monkey['Operation'].split()[-1]) if monkey['Operation'].split()[-1] != 'old' else current_value
                new_worry_level = eval('{} {} {}'.format(current_value, operator, value)) % modulo

                if number_of_times == 20:
                    new_worry_level = floor(new_worry_level / 3)

                if new_worry_level % int(monkey['Test'].split()[-1]) == 0:
                    target_monkey = int(monkey['If true'].split('monkey ')[-1])
                else:
                    target_monkey = int(monkey['If false'].split('monkey ')[-1])

                monkeys[target_monkey]['Items'] += [new_worry_level]
                monkey['Inspectometer'] += 1

            monkey['Items'] = []

        if debug:
            if number_of_times != 20:
                if y+1 == 1:
                    print('Currently at iteration {}, total time taken {}'.format(y, datetime.now() - start))
                    inspectometers = []
                    for x in range(0, len(monkeys)):
                        inspectometers += [monkeys[x]['Inspectometer']]

                    print(inspectometers)
                if y+1 == 20:
                    print('Currently at iteration {}, total time taken {}'.format(y, datetime.now() - start))
                    inspectometers = []
                    for x in range(0, len(monkeys)):
                        inspectometers += [monkeys[x]['Inspectometer']]

                    print(inspectometers)

            if (y+1) % 1000 == 0:
                print('Currently at iteration {}, total time taken {}'.format(y+1, datetime.now() - start))
                inspectometers = []
                for x in range(0, len(monkeys)):
                    inspectometers += [monkeys[x]['Inspectometer']]

                print(inspectometers)

    inspectometers = []
    print(monkeys)
    for x in range(0, len(monkeys)):
        inspectometers += [monkeys[x]['Inspectometer']]

    print(sorted(inspectometers))
    print('Stopping at {} iterations\nMonkeys throwing: {} * {} = {}'.format(y+1,sorted(inspectometers)[-1], sorted(inspectometers)[-2],
                                                      sorted(inspectometers)[-1] * sorted(inspectometers)[-2]))


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]
        monkeys = {}
        magic_modulo = 1
        current_monkey = 0
        for l in lines:
            if len(l) == 0:
                current_monkey += 1
                continue
            op, value = l.split(':')[0].strip(), l.split(':')[1].strip()
            if op == 'Monkey {}'.format(current_monkey):
                monkeys[current_monkey] = {}
                monkeys[current_monkey]['Inspectometer'] = 0
                continue
            if op == 'Starting items':
                op = 'Items'
                value = [int(x) for x in value.split(',')]
            if op == 'Test':
                magic_modulo *= int(value.split()[-1])

            monkeys[current_monkey][op] = value

    return monkeys, magic_modulo


def solve():
    monkey_start, magic_modulo = get_input()
    resolve_monkey_business(monkey_start, magic_modulo, 20)
    resolve_monkey_business(monkey_start, magic_modulo, 10000)


if __name__ == "__main__":
    solve()
