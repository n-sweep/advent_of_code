#/usr/bin/env python3
# Advent of Code 2015 Day 5
# https://adventofcode.com/2015/day/5

import re
from collections import Counter

with open('input.txt', 'r') as f:
    inp = f.read().split('\n')

def part_1():
    count = 0

    for line in inp:
        # check for bad strings
        if any([s in line for s in ('ab', 'cd', 'pq', 'xy')]):
            continue
        # check for 3 vowels
        counts = Counter(line)
        vowels = [counts[v] for v in 'aeiou']
        if sum(vowels) < 3:
            continue
        # check for double letters
        for i, l in enumerate(line, 1):
            if i < len(line) and l == line[i]:
                count += 1
                break
    return count

def part_2():
    count = 0

    for line in inp:
        xyx_re = r'(\w)\w\1'
        xyx_match = re.findall(xyx_re, line)
        if len(xyx_match) < 1:
            continue

        for pair in [line[i:i+2] for i in range(len(line)-1)]:
            matches = re.findall(r'{}'.format(pair), line)
            if len(matches) > 1:
                count += 1
                break
    return count


if __name__ == '__main__':
    print(part_2())
