#!/usr/bin/env python3
# Advent of Code 2015 Day 14
# https://adventofcode.com/2015/day/14

import re


def main():
    exp = (r'(\w+) can fly (\d+) km/s for (\d+) seconds, '
           r'but then must rest for (\d+) seconds.')
    race_time = 2503

    with open('./input.txt', 'r') as f:
        data = f.read()

    results = {}
    for name, fly_speed, fly_time, rest_time in re.findall(exp, data):
        fly_speed = int(fly_speed)
        fly_time = int(fly_time)
        rest_time = int(rest_time)

        # each reindeer has a fly/rest cycle
        cycle_time = fly_time + rest_time
        # find the total number of cycles a reindeer gets in the race time
        cycles = race_time // cycle_time

        # each cycle is a period of travel followed by a period of rest
        # so a partial cycle means the reindeer got some addtl travel time in
        mod = race_time % cycle_time
        partial = fly_speed * (mod if mod < fly_time else fly_time)

        total_distance = fly_speed * fly_time * cycles + partial
        results[name] = total_distance
        print(f'{name}: {str(total_distance).rjust(12 - len(name))}')

    print(max(results.values()))


if __name__ == '__main__':
    main()
