from copy import deepcopy


def get_input():
    with open('./input.txt', 'r') as file:
        return_dict = {}
        addr_dict = {}
        x = 0
        y = 0
        for line in file:
            line = line[:-1]
            if line.split(' ')[0] == 'mask':
                if len(addr_dict) > 0:
                    return_dict[x] = addr_dict
                    addr_dict = {}
                    x += 1
                    y = 0
                addr_dict = {'mask': line.split(' ')[-1]}
                continue
            address = line.split(' ')[0][4:-1]
            value = format(int(line.split(' ')[-1]))
            addr_dict[y] = {'address': address, 'value': value}
            y += 1
        return_dict[x] = addr_dict
        print(return_dict)
        return return_dict


def sub_x(input_list, x_pos):
    output_list = []
    for elem in input_list:
        output_list += [elem[:x_pos] + '1' + elem[x_pos+1:], elem[:x_pos] + '0' + elem[x_pos+1:]]
    return output_list


def solve(dict_of_stuff, use_floats=False):
    memory_addresses = {}
    for subset in dict_of_stuff:
        for elem in dict_of_stuff[subset]:
            if elem == 'mask':
                mask = dict_of_stuff[subset][elem]
                continue

            if not use_floats:
                address = dict_of_stuff[subset][elem]['address']
                op_value = bin(int(dict_of_stuff[subset][elem]['value']))[2:].zfill(len(mask))
                print("Comparing op_value {} with compmask {}".format(op_value, mask))
                value_after_mask = ''
                for pos, x in enumerate(op_value):
                    value_after_mask = value_after_mask + mask[pos] if mask[pos] != 'X' and op_value[pos] != mask[pos] else value_after_mask + x
                print("Ended up with op_value {} with compmask {}".format(value_after_mask, mask))
                memory_addresses[address] = int(value_after_mask, 2)
                print(memory_addresses)
                memory_addresses[address] = int(value_after_mask, 2)
            else:
                address = bin(int(dict_of_stuff[subset][elem]['address']))[2:].zfill(len(mask))
                op_value = dict_of_stuff[subset][elem]['value']

                # Process single bitmask
                address_after_mask = ''
                for pos, x in enumerate(address):
                    if address[pos] != mask[pos] and mask[pos] != '0':
                        address_after_mask = address_after_mask + mask[pos]
                    else:
                        address_after_mask = address_after_mask + address[pos]

                # Create list of valid values after applying bitmask
                target_addresses = []
                for pos, x in enumerate(address_after_mask):
                    if x == 'X':
                        target_addresses = sub_x(target_addresses, pos) if len(target_addresses) > 0 else sub_x([address_after_mask], pos)

                # Add op_value value to target memory address value (if any)
                for address in target_addresses:
                    address = int(address, 2)
                    memory_addresses[address] = int(op_value)

    return sum(memory_addresses.values())


def main():
    input_bitmasks_and_addresses = get_input()
    memory_mapping = solve(input_bitmasks_and_addresses)
    print("Came up with a total of {} bytes written to memory".format(memory_mapping))
    memory_mapping2 = solve(input_bitmasks_and_addresses, use_floats=True)
    print("Came up with a total of {} bytes written to memory the second time around".format(memory_mapping2))

if __name__ == "__main__":
    main()