#!/usr/bin/env python3
# Advent of Code 2015 Day 11
# https://adventofcode.com/2015/day/11

import re

alpha = 'abcdefghijklmnopqrstuvwxyz'
tri = [alpha[i:i + 3] for i in range(len(alpha) - 2)]
skip = [alpha.index(c) - 1 for c in 'iol']


def is_valid(pw):
    matches = re.findall(r'(.)\1+', pw)
    if not (matches and len(matches) > 1):
        return False

    for t in tri:
        if t in pw:
            return True

    return False


def to_alpha(inp):
    return ''.join([alpha[n] for n in inp])


def to_numeric(inp):
    return [alpha.index(c) for c in inp]


def increment(inp):
    num = to_numeric(inp)[::-1]
    for i, n in enumerate(num):
        if n < (len(alpha) - 1):
            num[i] += 2 if num[i] in skip else 1
            return to_alpha(num[::-1])
        else:
            num[i] = 0


def find_password(pw):
    while True:
        pw = increment(pw)
        if is_valid(pw):
            return pw


def main():

    part_1 = find_password('vzbxkghb')
    part_2 = find_password(part_1)

    print(part_1)
    print(part_2)


if __name__ == '__main__':
    main()
