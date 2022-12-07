#!/usr/bin/env python3
# Advent of Code 2022 Day 3
# https://adventofcode.com/2022/day/3

alpha = "abcdefghijklmnopqrstuvwxyz"
alpha = alpha + alpha.upper()

with open("input.txt", "r") as f:
    inp = f.read().strip()


def pt1():
    sacks = inp.split("\n")
    total = 0
    for sack in sacks:
        half = len(sack) // 2
        item = set(sack[:half]).intersection(set(sack[half:])).pop()
        total += alpha.index(item) + 1

    return total


def pt2():
    sacks = inp.split("\n")
    total = 0
    for i in range(0, len(sacks), 3):
        a, b = i, i + 3
        e0, e1, e2 = sacks[a:b]
        badge = set(e0).intersection(set(e1)).intersection(set(e2)).pop()
        total += alpha.index(badge) + 1

    return total


def main():
    print(pt2())


if __name__ == "__main__":
    main()
