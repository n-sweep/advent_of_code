#!/usr/bin/env python3
# Advent of Code 2015 Day 4
# https://adventofcode.com/2015/day/4

import hashlib

def part_1(): 
    i = 1
    while True:
        key = f'yzbqklnj{i}'
        result = hashlib.md5(key.encode()).hexdigest()
        # part 1
        # if result[:5] == '00000':
        # part 2
        if result[:6] == '000000':
            break

        i += 1
    
    return i

if __name__ == '__main__':
    print(part_1())

