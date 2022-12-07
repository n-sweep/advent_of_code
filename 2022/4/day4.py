#!/usr/bin/env python3
# Advent of Code 2022 Day 4
# https://adventofcode.com/2022/day/4

with open('./input.txt', 'r') as f:
    inp = f.read().strip()
    pairs = inp.split('\n')


def pt1():
    total = 0
    for pair in pairs:
        [ax, ay], [bx, by] = [p.split('-') for p in pair.split(',')]
        ax, ay, bx, by = [int(i) for i in (ax, ay, bx, by)]
        b_in_a = ax <= bx and by <= ay
        a_in_b = bx <= ax and ay <= by
        if b_in_a or a_in_b:
            total += 1

    return total


def pt2():
    total = 0
    for pair in pairs:
        [ax, ay], [bx, by] = [p.split('-') for p in pair.split(',')]
        ax, ay, bx, by = [int(i) for i in (ax, ay, bx, by)]
        a_lt_b = ay < bx
        b_lt_a = by < ax
        if not (b_lt_a or a_lt_b):
            total += 1

    return total


def main():
    print(pt2())


if __name__ == '__main__':
    main()
