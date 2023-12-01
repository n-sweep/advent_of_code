#!/usr/bin/env python3
# Advent of Code 2022 Day 9
# https://adventofcode.com/2022/day/9

import numpy as np
import logging

logging.basicConfig(filename='moves.log', level=logging.DEBUG)

with open('input.txt', 'r') as f:
    lines = [l.strip() for l in f.readlines()]


def main():
    # rope = [np.zeros(2) for _ in range(2)]  # pt 1
    rope = [np.zeros(2) for _ in range(10)]  # pt 2
    visited = set(tuple(rope[-1]))

    for line in lines:
        dir, dist = line.split()
        x = 1 if dir in 'UR' else -1
        move = (x, 0) if dir in 'LR' else (0, x)

        for _ in range(int(dist)):
            rope[0] += move
            for i in range(len(rope) - 1):
                j = i + 1
                delta = rope[i] - rope[j]
                if (np.absolute(delta) > 1).sum() > 0:
                    rope[j] += np.sign(delta)
                    if j + 1 == len(rope):
                        visited.add(tuple(rope[-1]))

    print(len(visited))


if __name__ == "__main__":
    main()
