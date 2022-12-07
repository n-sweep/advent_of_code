#!/usr/bin/env python3
# Advent of Code 2015 Day 10
# https://adventofcode.com/2015/day/10

import re
import sys


def parse(inp):
    parsed = re.findall(r'((.)\2*)', inp)
    return ''.join([str(len(x)) + y for x, y in parsed])


def iterate(i):
    inp = '1113222113'

    for _ in range(i):
        inp = parse(inp)

    return len(inp)


def main():
    part_1 = iterate(40)
    part_2 = iterate(50)

    print(part_2)


if __name__ == '__main__':
    main()
