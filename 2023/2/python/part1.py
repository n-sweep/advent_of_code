#!/usr/bin/env python3
# Advent of Code 2022 Day 2
# https://adventofcode.com/2022/day/2


with open('../data/input.txt', 'r') as f:
    lines = f.read().strip().split('\n')

limits = {
    'red': 12,
    'green': 13,
    'blue': 14
}

def is_possible(game):
    gid, results = game.split(': ')
    for result in results.split('; '):
        for cubes in result.split(', '):
            n, color = cubes.split(' ')
            if int(n) > limits[color]:
                return 0
    return int(gid.split(' ')[1])

def main():
    p = 0
    for line in lines:
        p += is_possible(line)

    print(p)

if __name__ == '__main__':
    main()
