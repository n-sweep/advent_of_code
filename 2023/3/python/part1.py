#!/usr/bin/env python3
# Advent of Code 2022 Day 3
# https://adventofcode.com/2022/day/3

import re

with open('../data/input.txt', 'r') as f:
    data = f.read().strip()
    lines = data.split('\n')


def process_text(lines):
    nums = {}

    for row, line in enumerate(lines):
        num, start = '', 0
        for i, char in enumerate(line):
            if char.isdigit():
                num += char
                if not start:
                    start = i
            else:
                if num:
                    nums[(row, start, i)] = int(num)
                    num, start = '', 0

    return nums


def main():
    sum = 0
    symbols = set()
    nums = process_text(lines)
    w = len(lines[0])
    l = len(lines)
    for key, num in nums.items():
        row, x, y = key
        rx, ry = row - 1, row + 2
        cx, cy = x - 1, y + 1
        rx = 0 if rx < 0 else rx
        ry = w if ry > w else ry
        cx = 0 if cx < 0 else cx
        cy = l if cy > l else cy

        found = False
        for row in range(rx, ry):
            for col in range(cx, cy):
                char = lines[row][col]
                if char != '.':
                    found = True
                    sum += num
                    # print(key, num)
                    # print('cols:', cx, cy, ', rows:', rx, ry)
                    # print(row, col, char)
                    # print('\n'.join(lines[rx:ry]), '\n')
                    # input()
                    break
            if found:
                break

    print(sum)
    # print(symbols)


if __name__ == '__main__':
    main()
