#!/usr/bin/env python3
# Advent of Code 2022 Day 8
# https://adventofcode.com/2022/day/8

with open('../data/input.txt', 'r') as f:
    data = f.read().strip().split('\n\n')


def process_nodes(text):
    nodes = {}
    start_nodes = set()

    for ln in text.split('\n'):
        node, conn = ln.split(' = ')
        if node.endswith('A'):
            start_nodes.add(node)
        nodes[node] = conn[1:-1].split(', ')

    return start_nodes, nodes


def main():
    instr, nodes = data
    start_nodes, all_nodes = process_nodes(nodes)
    instructions = [int(lr) for lr in instr.replace('L', '0').replace('R', '1')]
    steps = 0

    while any(n[-1] != 'Z' for n in start_nodes):
        for move in instructions:
            start_nodes = [all_nodes[node][move] for node in start_nodes]
            steps += 1

    print(steps)


if __name__ == '__main__':
    main()
