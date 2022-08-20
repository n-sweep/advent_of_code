#!/usr/bin/env python3
# Advent of Code 2015 Day 10
# https://adventofcode.com/2015/day/10

import sys

sys.setrecursionlimit(10000)

inp = '1113222113'

def count(n):
    c = 0
    s = list(str(n))
    output = ''
    while s:
        c += 1
        p = s.pop(0)
        if not s or p != s[0]:
            output += f'{c}{p}'

    return output

def part_1(i):
    for c in range(40):
        i0 = len(i)
        i = count(i)
        i1 = len(i)
        d = i1 - i0
        print(f'{c} {i0} + {d}')
    return i

if __name__ == '__main__':
    p = part_1(inp)
    print(p)
