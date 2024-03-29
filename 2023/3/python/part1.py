#!/usr/bin/env python3
# Advent of Code 2022 Day 3
# https://adventofcode.com/2022/day/3

with open('../data/input.txt', 'r') as f:
    lines = f.readlines()
    # lines = data.split('\n')


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
        text = ''.join([l[cx:cy] for l in lines[rx:ry]]).replace('.', '')

        for char in text:
            if not char.isdigit():
                sum += num
                break

    print(sum)


if __name__ == '__main__':
    main()
