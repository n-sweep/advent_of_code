#!/usr/bin/env python3
# Advent of Code 2015 Day 1
# https://adventofcode.com/2015/day/1

with open('input.txt', 'r') as f:
    inp = f.read()

def part_1():

    up = len(inp.replace(')', ''))
    down = len(inp.replace('(', ''))
    
    return up-down


def part_2():
    
    floor = 0

    for i, char in enumerate(inp, 1):
        floor += 1 if char == '(' else -1
        if floor < 0:
            return i
            break

if __name__ == '__main__':
    print(part_1())
    print(part_2())
