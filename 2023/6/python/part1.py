#!/usr/bin/env python3
# Advent of Code 2022 Day 6
# https://adventofcode.com/2022/day/6

with open('../data/input.txt', 'r') as f:
    lines = f.read().strip().split('\n')


def process(lines):
    split = [l.split(":") for l in lines]
    races = list(zip(*[l[1].split() for l in split]))
    # races = [{split[i][0]: v for i, v in enumerate(val)} for val in vals]
    return races


def race(time, hold):
    travel = time - hold
    distance = travel * hold
    return distance


def main():
    total = 1
    races = process(lines)
    for time, rec in races:
        wins = 0
        time, rec = int(time), int(rec)
        for i in range(time):
            dist = race(time, i)
            if dist > rec:
                wins += 1

        total *= wins
    print(total)


if __name__ == '__main__':
    main()
