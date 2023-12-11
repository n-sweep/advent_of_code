#!/usr/bin/env python3
# Advent of Code 2022 Day 9
# https://adventofcode.com/2022/day/9

with open('../data/input.txt', 'r') as f:
    lines = [[int(i) for i in l.split()] for l in f.read().strip().split('\n')]


def diffs(lst):
    output = []
    for i in range(len(lst) - 1):
        j = i + 1
        output.append(lst[j] - lst[i])

    return output


def extrapolate(lst):
    for i, row in enumerate(lst[::-1]):
        if i < 1:
            row.append(0)
        else:
            row.append(row[-1] + lst[::-1][i - 1][-1])

    return lst


def main():
    total = 0
    for line in lines:
        rows = [line]
        while sum(line) > 0:
            line = diffs(line)
            rows.append(line)

        total += extrapolate(rows)[0][-1]

    print(total)

if __name__ == '__main__':
    main()
