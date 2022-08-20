#!/usr/bin/env python3
# Advent of Code 2015 Day 7
# https://adventofcode.com/2015

import re

operators = {
        '':         lambda x: x[1],
        'NOT':      lambda x: ~ x[1],
        'AND':      lambda x: x[0] & x[1],
        'OR':       lambda x: x[0] | x[1],
        'LSHIFT':   lambda x: x[0] << x[1],
        'RSHIFT':   lambda x: x[0] >> x[1]
        }

def build_tree():
    pattern = r'(?:([a-z\d]*) )?(?:([A-Z]*) )?([a-z\d]*) -> ([a-z\d]*)'
    with open('input.txt', 'r') as f:
        data = re.findall(pattern, f.read())

    tree = {i[3]: list(i[:-1]) for i in data}
    # part 2
    tree['b'] = ('', '', 3176)

    return tree

def remember(f):
    mem = {}
    def wrapper(graph, key):
        if key not in mem:
            mem[key] = f(graph, key)
        return mem[key]
    return wrapper

@remember
def get_key(graph, key):
    try:
        return int(key) if key else key
    except ValueError:
        g = graph[key] 
        op = g[1]
        args = [get_key(graph, g[i]) for i in [0,2]]

        return operators[op](args)

def main():
    tree = build_tree()
    return get_key(tree, 'a')

if __name__ == '__main__':
    p = main()
    print(p)
