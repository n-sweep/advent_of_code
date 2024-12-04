# Advent of Code 2024 Day 3
# https://adventofcode.com/2024/day/3

import re

exp = r'mul\((\d+),(\d+)\)'

with open('puzzle.txt', 'r') as f:
    data = f.read().strip()


def pt1():
    m = sum([(int(a) * int(b)) for a, b in re.findall(exp, data)])
    print(m)


def main():
    total = 0
    for do in data.split('do()'):
        do = do.split("don't()")[0]
        total += sum([(int(a) * int(b)) for a, b in re.findall(exp, do)])

    print(total)


if __name__ == '__main__':
    main()
