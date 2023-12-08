#!/usr/bin/env python3
# Advent of Code 2022 Day 8
# https://adventofcode.com/2022/day/8

with open('../data/input.txt', 'r') as f:
    data = f.read().strip().split('\n\n')


def process_nodes(text):
    output = {}

    for ln in text.split('\n'):
        node, conn = ln.split(' = ')
        output[node] = conn[1:-1].split(', ')

    return output


def main():
    instr, nodes = data
    nodes = process_nodes(nodes)
    node = 'AAA'
    steps = 0

    while node != 'ZZZ':
        for i in instr:
            left, right = nodes[node]
            node = left if i == 'L' else right
            steps += 1

    print(steps)


if __name__ == '__main__':
    main()
