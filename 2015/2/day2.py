#!/usr/bin/env python3
# Advent of Code 2015 Day 2
# https://adventofcode.com/2015/day/2

from math import prod

with open('input.txt', 'r') as f:
    inp = [l.replace('\n', '') for l in f.readlines()]
    presents = [[int(d) for d in p.split('x')] for p in inp]


def part_1():
    result = 0
    for l, w, h in presents:
        dims = [l*w, w*h, h*l]
        result += (sum(dims) * 2) + min(dims)

    return result

def part_2():
    result = 0
    for p in presents:
        vol = prod(p)
        small_dims = sorted(p)[:-1]

        result += (sum(small_dims) * 2) + vol

    return result

if __name__ == '__main__':
    print(part_2())

