#!/usr/bin/env python3
# Advent of Code 2022 Day 2
# https://adventofcode.com/2022/day/2

with open('input.txt', 'r') as f:
    inp = f.read()

# map RPS to the values they beat
rps = list('RPS')
win_map = dict(zip(rps, list('SRP')))
lose_map = dict(zip(rps, list('PSR')))


def pt1():
    # map keys from input to RPS
    key_map = dict(zip(list('ABCXYZ'), rps * 2))

    total = 0
    rounds = inp.strip().split('\n')

    for round in rounds:
        p2, p1 = [key_map[p] for p in round.split(' ')]

        # add points for choice
        total += rps.index(p1) + 1

        # 0 pts for a loss
        if p1 == p2:
            # 3 pts for a tie
            total += 3
        elif p2 == win_map[p1]:
            # 6 pts for a win
            total += 6

    return total


def pt2():
    # map keys from input to RPS
    key_map = dict(zip(list('ABCXYZ'), rps + list('LTW')))

    total = 0
    rounds = inp.strip().split('\n')

    for round in rounds:
        p2, ltw = [key_map[p] for p in round.split(' ')]

        if ltw == 'W':
            p1 = lose_map[p2]
            total += 6 + rps.index(p1) + 1
        elif ltw == 'T':
            total += 3 + rps.index(p2) + 1
        else:
            p1 = win_map[p2]
            total += rps.index(p1) + 1

    return total


def main():
    print(pt1())
    print(pt2())


if __name__ == '__main__':
    main()
