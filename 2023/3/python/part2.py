#!/usr/bin/env python3
# Advent of Code 2022 Day 3
# https://adventofcode.com/2022/day/3

from math import prod

with open('../data/input.txt', 'r') as f:
    lines = f.readlines()


def process_text(lines):
    nums = {}
    stars = []

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
                if char == '*':
                    stars.append((row, i))

    return nums, stars


def main():
    sum = 0
    nums, stars = process_text(lines)

    w = len(lines[0])
    l = len(lines)

    for s_row, x in stars:
        cx, cy = x - 1, x + 2
        cx = 0 if cx < 0 else cx
        cy = w if cy > w else cy

        adj = []
        for n in nums:
            n_row, i, j = n
            if n_row > s_row + 1 or n_row < s_row - 1: continue
            if set(range(i, j)).intersection(range(cx, cy)):
                adj.append(n)

        if len(adj) == 2:
            sum += prod([nums[key] for key in adj])

    print(sum)


if __name__ == '__main__':
    main()
