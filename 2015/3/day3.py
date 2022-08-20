#!/usr/bin/env python3
# Advent of Code 2015 Day 3
# https://adventofcode.com/2015/day/3

with open('input.txt', 'r') as f:
    inp = f.read()

def part_1():
    locs = [(0, 0)]
    
    for move in inp:
        new = list(locs[-1])
        drc = 1 if move in '^>' else -1
        ax = 0 if move in '<>' else 1
        new[ax] += drc
        
        locs.append(tuple(new))

    return len(set(locs))

def part_2():
    output = set()
    santa = inp[::2]
    robo_santa = inp[1::2]
    
    for moves in [santa, robo_santa]:
        locs = [(0,0)]
        for move in moves:
            new = list(locs[-1])
            drc = 1 if move in '^>' else -1
            ax = 0 if move in '<>' else 1
            new[ax] += drc

            locs.append(tuple(new))

        output = output.union(set(locs))

    return len(output)

if __name__ == '__main__':
    print(part_2())
