#!/usr/bin/env python3
# Advent of Code 2015 Day 13
# https://adventofcode.com/2015/day/13

import re
from itertools import permutations

exp = r'(\w+) would (lose|gain) (\d+) happiness units by sitting next to (\w+).'


def get_data():
    with open('./input.txt', 'r') as f:
        data = f.read()

    output = {}
    for key, pos_neg, val, name in re.findall(exp, data):
        if key not in output:
            output[key] = {}
        output[key].update({
            name: int(val) if pos_neg == 'gain' else -int(val)
        })

    return output


def arrangements(data):
    perms = list(permutations(data.keys()))

    output = []
    for perm in perms:
        happiness = 0
        for i, name in enumerate(perm):
            left = perm[i + 1 if i + 1 < len(perm) else 0]
            right = perm[i - 1]
            neighbors = data[name]
            happiness += neighbors[left] + neighbors[right]

        output.append(happiness)

    print(max(output))


def main():
    data = get_data()
    keys = data.keys()
    me = 'Sweep'

    # part_2
    for k in keys:
        data[k][me] = 0

    data[me] = {k: 0 for k in data.keys()}

    arrangements(data)


if __name__ == '__main__':
    main()
