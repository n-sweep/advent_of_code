# Advent of Code 2024 Day 4
# https://adventofcode.com/2024/day/4

import re
import numpy as np

with open('puzzle.txt', 'r') as f:
    data = f.read().strip()


def pt1():
    arr = np.array([list(r.strip()) for r in data.splitlines()])

    diag = []
    for i in range(-arr.shape[0], arr.shape[0]):
        for a in [arr, np.fliplr(arr)]:
            diag.append(np.pad(np.diagonal(a, i), (0, abs(i)), 'empty'))

    diag = np.array(diag)
    search = '\n'.join([''.join(row) for row in [*arr, *arr.T, *diag]])

    print(len(re.findall(r'(?=(XMAS|SAMX))', search)))


def main():
    pt1()


if __name__ == '__main__':
    main()
