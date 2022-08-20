#!/usr/bin/env python3
# Advent of Code 2015 Day 8
# https://adventofcode.com/2015/day/8

import re
from collections import Counter

pattern = r"(\\[\\|\"]|\\x[\d\w]{2})"
with open ('input.txt', 'r') as f:
    strings = f.readlines()

def part_1():
    count = len(strings) * 2
    joined = ''.join(strings)
    matches = re.findall(pattern, joined)
    
    for match in matches:
        count += 3 if 'x' in match else 1
    
    print('part 1:', count)

def part_2():
    joined = ''.join(strings)
    chars = Counter(joined)
    count = (len(strings) * 2) + chars['"'] + chars['\\']

    print('part 2:', count)

if __name__ == '__main__':
    part_2()
