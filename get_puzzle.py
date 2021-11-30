import argparse
import os
import json
import subprocess

import requests


def parse_args():
    parser = argparse.ArgumentParser(description='Puzzle preparation parameters')
    parser.add_argument('-d', '--day', type=int, choices=range(0,25), metavar='[1-25]', default=1,
                        help='For which day to download the puzzle')
    parser.add_argument('-y', '--year', type=int, default=2020, help='The year for which to prepare (default = 2021)')
    parser.add_argument('-c', '--cookie', type=str, default='.aoc_session_cookie', help='The file which contains the AoC session cookie')
    args = parser.parse_args()

    if 0 < args.day < 9:
        day = '0{}'.format(args.day)
    else:
        print("day = {}".format(args.day))
        day = str(args.day)
    year = args.year
    print(args.cookie)
    cookie = json.loads(open(args.cookie, 'r').read())
    print(cookie)
    return day, year, cookie


def create_directory_from_template(day, year):
    year_path = './advent {}'.format(year)
    day_path = '{}/challenge {}'.format(year_path, day)
    if not os.path.exists(year_path):
        print('Creating yearly directory {}'.format(year_path))
        os.makedirs(year_path)
    if not os.path.exists(day_path):
        print('Creating daily directory {}'.format(day_path))
        os.makedirs(day_path)
    return day_path


def prepare_from_template(daily_path, day):
    with open('./templates/template.py', 'r') as templ:
        daily_filename = '{}/number{}.py'.format(daily_path, day)
        if not os.path.exists(daily_filename):
            with open('{}'.format(daily_filename), 'w+') as new_file:
                print('Creating file {}'.format(daily_filename))
                new_file.writelines(templ.readlines())


def get_puzzle_input(day, year, aoc_cookie, daily_path):
    # Convert day to int, since AoC doesn't use leading zeroes
    puzzle_input_path = '{}/input.txt'.format(daily_path)
    if not os.path.exists(puzzle_input_path):
        puzzle_input = requests.get('https://adventofcode.com/{}/day/{}/input'.format(year, int(day)), cookies=aoc_cookie)
        with open(puzzle_input_path, 'w+') as input_file:
            input_file.writelines(l for l in puzzle_input.text)
    else:
        print('Puzzle input already exists at {}\nAborting to prevent AoC overload!'.format(puzzle_input_path))


def open_daily_puzzle(day, year):
    puzzle_url = 'https://adventofcode.com/{}/day/{}'.format(year, int(day))
    subprocess.call(['firefox', '-new-tab', puzzle_url])


def process():
    day, year, cookie = parse_args()
    daily_path = create_directory_from_template(day, year)
    prepare_from_template(daily_path, day)
    puzzle_input = get_puzzle_and_input(day, year, cookie)
    process_puzzle_input(daily_path, puzzle_input)
    open_daily_puzzle(day, year)


if __name__ == '__main__':
    process()