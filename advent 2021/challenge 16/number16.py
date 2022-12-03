
def parse_packet(packet_string, total_version=0):
    parsed_packet = ''
    literal = False
    version = int(packet_string[:3], 2)
    total_version += version
    packet_type_id = int(packet_string[3:6], 2)
    print("Version {}, packet type {}".format(version, packet_type_id))
    if packet_type_id == 4:
        print("Starting with packet {}")
        pos = 6
        number_string = ''
        while True:
            number_string += str(packet_string[pos:pos+5][1:])
            if pos + 5 >= len(packet_string):
                break
            else:
                print("Appending {}".format(str(packet_string[pos:pos+5][1:])))
                pos += 5
        print("Found literal number {}".format(int(number_string, 2)))
    else:
        length_type_id = int(packet_string[6], 2)
        if length_type_id == 0:
            print(packet_string[7:20])
            subpacket_length = int(packet_string[7:20], 2)
            subpackets = packet_string[20:20+subpacket_length]
            print('Length type 0, subpacket length {}, subpacket: {}'.format(subpacket_length, subpackets))
        else:
            subpacket_amount = int(packet_string[7:18], 2)
            subpacket_length = 11
            subpackets = packet_string[19:subpacket_length*subpacket_amount]
            print('Length type 1, subpacket amount {}, subpackets: {}'.format(subpacket_amount, subpackets))
            print(subpackets)
        parse_packet(subpackets, total_version=total_version)


def get_input():
    with open('./test_input.txt', 'r') as input_file:
        line = input_file.readline().strip('\n')

    binary_line = bin(int(line, 16))[2:]
    return binary_line


def solve():
    daily_input = get_input()
    print(daily_input)
    parse_packet(daily_input)


if __name__ == "__main__":
    solve()
