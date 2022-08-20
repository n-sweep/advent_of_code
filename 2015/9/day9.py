#!/usr/bin/env python3
# Advent of Code 2015 Day 9
# https://adventofcode.com/2015/day/9

import re
from collections import defaultdict
from itertools import permutations

class Graph:
    def __init__(self):
        self.graph = defaultdict(dict)
        self.nodes = set()

    def add_edge(self, n, c, w):
        self.nodes.add(n)
        self.nodes.add(c)
        self.graph[n][c] = int(w)
        self.graph[c][n] = int(w)

    def search(self, node, locs):
        locs.append(node)
        
        for nbr in self.graph[node]:
            if nbr not in locs:
                self.search(nbr, locs)

    def run(self):
        for node in list(self.graph.keys()):
            locs = []
            result = self.search(node, locs)
            if len(locs) == len(self.nodes):
                p = [self.graph[locs[i-1]][locs[i]] for i in range(1,len(locs))]
                print(p)
                return sum(p)

def build_graph():
    graph = Graph()
    pattern = r'(\w+) to (\w+) = (\d+)'
    
    with open('input.txt', 'r') as f:
        data = re.findall(pattern, f.read())

    for node, connection, weight in data:
        graph.add_edge(node, connection, weight)

    return graph

def part_1():
    graph = build_graph()
    perms = list(permutations(graph.nodes))
    output = {}
    for perm in perms:
        k = ' -> '.join(perm)
        v = sum([graph.graph[perm[i-1]][perm[i]] for i in range(1, len(perm))])
        output[k] = v
    return output

if __name__ == '__main__':
    p = part_1()
    # part 1
    print(min(p.values()))
    # part 2
    print(max(p.values()))

