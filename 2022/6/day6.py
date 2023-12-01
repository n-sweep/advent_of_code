#!/usr/bin/env python3
# Advent of Code 2022 Day 6
# https://adventofcode.com/2022/day/6

with open('./input.txt', 'r') as f:
    inp = f.read().strip()


def get_marker(n):
    for i in range(len(inp)):
        j = i + n
        substr = set(inp[i:j])
        if len(substr) == n:
            return i + n


def main():
    pt_1 = get_marker(4)
    print(pt_1)
    pt_2 = get_marker(14)
    print(pt_2)


if __name__ == '__main__':
    main()
