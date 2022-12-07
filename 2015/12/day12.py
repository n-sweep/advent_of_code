#!/usr/bin/env python3
# Advent of Code 2015 Day 12
# https://adventofcode.com/2015/day/12

import json


def find_nums_recursive(data, i=0):
    t = type(data)
    if t == list:
        s = sum([find_nums_recursive(d, i) for d in data])
        return i + s
    elif t == dict:
        if 'red' in data.values():
            # part 2
            return 0
        s = sum([find_nums_recursive(d, i) for d in data.values()])
        return i + s
    elif t == int:
        return i + data
    else:
        return i + 0


def main():
    with open('input.json', 'r') as f:
        data = json.load(f)

    output = find_nums_recursive(data)

    print(output)


if __name__ == '__main__':
    main()
