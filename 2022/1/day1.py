#!/usr/bin/env python3
# Advent of Code 2022 Day 1
# https://adventofcode.com/2022/day/1


def main():
    with open('input.txt', 'r') as f:
        inp = f.read()

    elves = []
    for elf in inp.split('\n\n'):
        s = sum([int(i) for i in elf.strip().split('\n')])
        elves.append(s)

    # part 1
    print(max(elves))

    # part 2
    print(sum(sorted(elves)[-3:]))


if __name__ == '__main__':
    main()
