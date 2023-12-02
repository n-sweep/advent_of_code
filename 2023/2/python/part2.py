#!/usr/bin/env python3
# Advent of Code 2022 Day 2
# https://adventofcode.com/2022/day/2

from math import prod


with open('../data/input.txt', 'r') as f:
    lines = f.read().strip().split('\n')


def power(game):
    game_set = {}
    gid, results = game.split(': ')
    for result in results.split('; '):
        for cubes in result.split(', '):
            n, color = cubes.split(' ')
            n = int(n)
            if color not in game_set or game_set[color] < n:
                    game_set[color] = n

    return prod(game_set.values())

def main():
    p = 0
    for line in lines:
        p += power(line)
    print(p)

if __name__ == '__main__':
    main()
