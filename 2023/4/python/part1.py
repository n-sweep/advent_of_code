#!/usr/bin/env python3
# Advent of Code 2022 Day 4
# https://adventofcode.com/2022/day/4

with open('../data/input.txt', 'r') as f:
    lines = f.read().strip().split('\n')


def main():
    total = 0
    for line in lines:
        numbers = line.split(': ')[1]
        num_split = numbers.split(' | ')
        winning = {n.strip() for n in num_split[0].split()}
        have = {n.strip() for n in num_split[1].split()}
        matches = winning.intersection(have)

        score = 0
        for _ in matches:
            if score:
                score *= 2
            else:
                score = 1

        total += score

    print(total)


if __name__ == '__main__':
    main()
