import datetime


def get_input():
    with open('./input.txt', 'r') as file:
        lines = file.readlines()
        input_list = [int(lines[0][:-1])]
        input_list += [int(x) if x != 'x' else x for x in lines[1][:-1].split(',')]
        return input_list


def get_nearest_bus(bus_schedule, find_next=True):
    waiting_times = []
    arrival_time = bus_schedule[0]
    departure_times = bus_schedule[1:]

    if find_next:
        for line_number in departure_times:
            if line_number == 'x':
                continue
            previous_time = arrival_time - (arrival_time % line_number)
            next_time = previous_time + line_number
            waiting_times += [[next_time-arrival_time, line_number]]
        return sorted(waiting_times)[0][0] * sorted(waiting_times)[0][1]
    else:
        start = datetime.datetime.now()
        period = 1
        timestamp = 0
        for line_number in departure_times:
            if line_number != 'x':
                while (timestamp % line_number) != 0:
                    timestamp += period
                period *= line_number
            timestamp += 1

        finish = datetime.datetime.now()
        return timestamp - len(departure_times), finish - start


def main():
    bus_times = get_input()
    time_to_wait = get_nearest_bus(bus_times)
    print("We'll have to wait a fraction of {} minutes to get to the airport!".format(time_to_wait))
    first_match, timetaken = get_nearest_bus(bus_times, find_next=False)
    print("Found the answer {}, which took a mere {} seconds".format(first_match, timetaken))


if __name__ == "__main__":
    main()