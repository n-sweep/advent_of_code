#!/usr/bin/env python3
# Advent of Code 2015 Day 14
# https://adventofcode.com/2015/day/14

import re


def main():
    exp = (r'(\w+) can fly (\d+) km/s for (\d+) seconds, '
           r'but then must rest for (\d+) seconds.')

    with open('./input.txt', 'r') as f:
        data = f.read()

    all_results = []
    for race_time in range(1, 2504):
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

        all_results.append(results)

    score = {k: 0 for k in all_results[0].keys()}
    for result in all_results:
        max_val = max(result.values())
        for k, v in result.items():
            if v == max_val:
                score[k] += 1

    score_string = '\n'.join([f'{k}: {str(v).rjust(12 - len(k))}' for k, v in score.items()])
    winner = max(score, key=score.get)
    print(score_string)
    print(f'\nWinner:\n{winner} {score[winner]}')


if __name__ == '__main__':
    main()
