import datetime
from dateutil.parser import parse
import re

import pytz


class Trip:
    def __init__(self, departure_timezone: pytz.timezone, departure_time: datetime.datetime,
                 arrival_timezone: pytz.timezone, arrival_time: datetime.datetime):
        self.departure_timezone = departure_timezone
        self.departure_time = departure_time
        self.arrival_timezone = arrival_timezone
        self.arrival_time = arrival_time


def calculate_travel_times(trips: [Trip]):
    total_travel_time = 0
    t: Trip
    for t in trips:
        print(f"checking trip {t.departure_timezone} to {t.arrival_timezone}")
        normalised_departure = t.departure_timezone.normalize(t.departure_timezone.localize(t.departure_time)).astimezone(pytz.UTC)
        normalised_arrival = t.arrival_timezone.normalize(t.arrival_timezone.localize(t.arrival_time)).astimezone(pytz.UTC)
        travel_time = (normalised_arrival - normalised_departure).seconds
        print(f"got time travel {travel_time/60} for {normalised_departure} to {normalised_arrival}")
        total_travel_time += travel_time

    print(int(total_travel_time/60))


def get_input():
    with open('./input.txt', 'r') as input_file:
        lines = [l.strip('\n') for l in input_file.readlines()]

    iteneraries: [Trip] = []

    for l in lines:
        if l.startswith('Departure'):
            departure_timezone = pytz.timezone(re.findall(r'Departure: +([A-Za-z_-]+(?:/[A-Za-z_-]+)*)', l)[0])
            departure_time = parse(re.findall(r'[A-Z][a-z]{2} \d{2}, \d{4}, \d{2}:\d{2}', l)[0])
        if l.startswith('Arrival'):
            arrival_timezone = pytz.timezone(re.findall(r'Arrival: +([A-Za-z_-]+(?:/[A-Za-z_-]+)*)', l)[0])
            arrival_time = parse(re.findall(r'[A-Z][a-z]{2} \d{2}, \d{4}, \d{2}:\d{2}', l)[0])
        if len(l) == 0:
            iteneraries += [Trip(departure_timezone, departure_time, arrival_timezone, arrival_time)]

    if departure_timezone:
        iteneraries += [Trip(departure_timezone, departure_time, arrival_timezone, arrival_time)]

    return iteneraries


def solve():
    trips = get_input()
    calculate_travel_times(trips)


if __name__ == "__main__":
    solve()
