# Advent of Code 2024 Day 4
# https://adventofcode.com/2024/day/4

import re
import numpy as np
from itertools import product


with open('puzzle.txt', 'r') as f:
    arr = np.array([list(r.strip()) for r in f.readlines()])


def pt1():
    diag = []
    for i in range(-arr.shape[0], arr.shape[0]):
        for a in [arr, np.fliplr(arr)]:
            diag.append(np.pad(np.diag(a, i), (0, abs(i)), 'empty'))

    diag = np.array(diag)
    search = '\n'.join([''.join(row) for row in [*arr, *arr.T, *diag]])

    print(len(re.findall(r'(?=(XMAS|SAMX))', search)))


def main():
    total = 0
    for y, x in list(zip(*np.where(arr=='A'))):
        win = arr[y-1:y+2, x-1:x+2]

        if tuple(win.shape) != (3, 3):
            continue

        d1 = ''.join(np.diag(win))
        d2 = ''.join(np.diag(np.fliplr(win)))

        if d1 in ['MAS', 'SAM'] and d2 in ['MAS', 'SAM']:
            total += 1

    print(total)


if __name__ == '__main__':
    main()
