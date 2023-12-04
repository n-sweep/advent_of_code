#!/usr/bin/env python3
# Advent of Code 2022 Day 4
# https://adventofcode.com/2022/day/4

with open('../data/test_1.txt', 'r') as f:
    lines = f.read().strip().split('\n')


def process(lines):
    wins = []
    for line in lines:
        numbers = line.split(': ')[1].split(' | ')
        winning = {n.strip() for n in numbers[0].split()}
        have = {n.strip() for n in numbers[1].split()}
        n_matches = len(winning.intersection(have))

        score = 0
        for _ in range(n_matches):
            if score:
                score *= 2
            else:
                score = 1

        wins.append(n_matches)

    return wins


def recur(wins, a=0, b=0, total=0):
    b = b if b else len(wins)
    for num in (sub:=wins[a:b]):
        total += 1
        x = a + 1
        y = x + num
        total = recur(wins, x, y, total)

    return total

def main():
    wins = process(lines)
    total = recur(wins)
    print(total)


if __name__ == '__main__':
    main()
