#!/usr/bin/env python3
# Advent of Code 2022 Day 8
# https://adventofcode.com/2022/day/8

from math import prod
from pyperclip import copy

with open('./input.txt', 'r') as f:
    inp = f.read().strip()

grid = [[int(c) for c in row] for row in inp.split('\n')]
inverse_grid = [[r[i] for r in grid] for i in range(len(grid[0]))]


def find_visible(seg, indicies=None):
    seg_max = max(seg)
    i = seg.index(seg_max)

    if indicies:
        indicies.append(i)
    else:
        indicies = [i]

    if i > 0:
        find_visible(seg[:i], indicies)

    return indicies


def check_row(row):
    row_max = max(row)
    il = row.index(row_max)
    ir = len(row) - row[::-1].index(row_max) - 1
    trees = [il, ir]

    vis_lt = find_visible(row[:il])
    trees += vis_lt

    vis_rt_reverse = find_visible(row[ir + 1:][::-1])
    vis_rt = [len(row) - v - 1 for v in vis_rt_reverse]
    trees += vis_rt

    return sorted(trees)


def pt1():
    indicies = []
    for i, row in enumerate(grid):
        indicies += [(i, n) for n in check_row(row)]
    for i, row in enumerate(inverse_grid):
        indicies += [(n, i) for n in check_row(row)]

    return len(set(indicies))


def view_distance(tree, view):
    if not view:
        return 0

    for i, t in enumerate(view, 1):
        if t >= tree:
            return i

    return len(view)


def pt2():
    xr = range(len(grid[0]))
    yr = range(len(grid))
    output = 0
    for x, y in [(x, y) for y in yr for x in xr]:
        row = grid[y]
        irow = inverse_grid[x]
        tree = row[x]

        east = row[x + 1:]
        west = row[:x][::-1]
        north = irow[:y][::-1]
        south = irow[y + 1:]

        distances = [view_distance(tree, d) for d in [north, south, east, west]]
        score = prod(distances)

        if score > output:
            output = score

    return output


def main():
    # result = pt1()
    result = pt2()
    print(result)
    copy(result)


if __name__ == '__main__':
    main()
