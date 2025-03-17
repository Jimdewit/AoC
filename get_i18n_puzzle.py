import argparse
import os
import json
import subprocess

import requests


def parse_args():
    parser = argparse.ArgumentParser(description='Puzzle preparation parameters')
    parser.add_argument('-d', '--day', type=int, choices=range(0,25), metavar='[1-25]', default=1,
                        help='For which day to download the puzzle')
    parser.add_argument('-c', '--cookie', type=str, default='.i18n_session_cookie', help='The file which contains the AoC session cookie')

    args = parser.parse_args()
    if 0 < args.day < 10:
        day = '0{}'.format(args.day)
    else:
        print("day = {}".format(args.day))
        day = str(args.day)
    cookie = json.loads(open(args.cookie, 'r').read())

    return day, cookie


def create_directory_from_template(day):
    base_path = './i18n'
    day_path = '{}/challenge {}'.format(base_path, day)
    if not os.path.exists(day_path):
        print('Creating daily directory {}'.format(day_path))
        os.makedirs(day_path)
    return day_path


def prepare_from_template(daily_path, day):
    number_phile = 'number{}'.format(day)
    with open('./templates/template.py', 'r') as templ:
        daily_filename = '{}/{}.py'.format(daily_path, number_phile)
        if not os.path.exists(daily_filename):
            with open(daily_filename, 'w+') as new_file:
                new_file.writelines(templ.readlines())

    with open('./templates/test_template.py', 'r') as test_templ:
        daily_filename = '{}/test{}.py'.format(daily_path, day)
        if not os.path.exists(daily_filename):
            with open(daily_filename, 'a+') as new_file:
                for line in test_templ.readlines():
                    if line.strip('\n') == 'from xx import solve':
                        line = line.replace('xx', number_phile)
                    new_file.write(line)

    daily_filename = '{}/test_input.txt'.format(daily_path, day)
    if not os.path.exists(daily_filename):
        with open(daily_filename, 'w+') as test_input_file:
            test_input_file.writelines('')


def get_and_process_puzzle_input(day, aoc_cookie, daily_path):
    # Convert day to int, since AoC doesn't use leading zeroes
    puzzle_input_path = '{}/input.txt'.format(daily_path)
    if not os.path.exists(puzzle_input_path):
        puzzle_input = requests.get('https://i18n-puzzles.com/puzzle/{}/input'.format(int(day)), cookies=aoc_cookie)
        with open(puzzle_input_path, 'w+') as input_file:
            input_file.writelines(l for l in puzzle_input.text)
    else:
        raise('Puzzle input already exists at {}\nAborting to prevent AoC overload!'.format(puzzle_input_path))


def open_daily_puzzle(day):
    puzzle_url = 'https://i18n-puzzles.com/puzzle/{}'.format(int(day))
    subprocess.call(['firefox', '-new-tab', puzzle_url])


def process():
    day, cookie = parse_args()
    daily_path = create_directory_from_template(day)
    prepare_from_template(daily_path, day)
    get_and_process_puzzle_input(day, cookie, daily_path)
    open_daily_puzzle(day)


if __name__ == '__main__':
    process()