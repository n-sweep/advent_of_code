#!/usr/bin/env python3
# Advent of Code 2015 Day 6
# https://adventofcode.com/2015/day/6

import re
import numpy as np

pattern = r'(.+) (\d+,\d+) through (\d+,\d+)'
with open('input.txt', 'r') as f:
    instructions = re.findall(pattern, f.read())

size = 1000
board = np.zeros((size, size))

def part_1():
    for inst, a, b in instructions:
        a, b = ([int(n) + i for n in t.split(',')] for i, t in enumerate((a, b)))
        if 'turn on' == inst:
            output = 1
        elif 'turn off' == inst:
            output = 0
        elif 'toggle' == inst:
            subset = board[a[0]:b[0], a[1]:b[1]]
            output = np.where(subset < 1, 1, 0)
        else:
            print('this never prints')

        board[a[0]:b[0], a[1]:b[1]] = output

    return board.sum()

def part_2():
    for inst, a, b in instructions:
        a, b = ([int(n) + i for n in t.split(',')] for i, t in enumerate((a, b)))
        subset = board[a[0]:b[0], a[1]:b[1]]
        if 'turn on' == inst:
            output = 1
        elif 'turn off' == inst:
            output = np.where(subset > 0, -1, 0)
        elif 'toggle' == inst:
            output = 2
        else:
            print('this never prints')

        board[a[0]:b[0], a[1]:b[1]] = subset + output

    return board.sum()

if __name__ == '__main__':
    p = part_2()
    print(p)
