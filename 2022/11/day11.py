#!/usr/bin/env python3
# Advent of Code 2022 Day 11
# https://adventofcode.com/2022/day/11

import logging
from math import prod

# logging.basicConfig(filename='monkeys.log', level=logging.INFO)

with open('./test.txt', 'r') as f:
    inp = f.read().strip()


class Monkey:

    inspections = 0

    def __init__(self, text, troop):
        self.troop = troop
        self.process_text(text)

    def process_text(self, text):
        lines = [line for line in text.split('\n')]
        self.id = int(lines.pop(0).split(' ')[1][0])

        lines = [line.split(': ')[1] for line in lines]
        self.items = [int(i) for i in lines[0].split(', ')]
        self.operation = lines[1].split(' ')[3:]
        self.test = [int(l.split(' ')[-1]) for l in lines[2:]]

    def inspect(self):
        self.inspections += 1

        item = self.items.pop(0)
        test, true, false = self.test
        op, val = self.operation
        val = item if val == 'old' else int(val)
        operation = f'({item} {op} {val})'# // 3'

        if op == '*':
            worry = prod((item, val))
        else:
            worry = sum((item, val))

        if worry % test == 0:
            return worry, true
        else:
            return worry, false

    def turn(self):
        for _ in range(len(self.items)):
            item, target = self.inspect()
            self.troop[target].items.append(item)

    def __str__(self):
        return f"Monkey {self.id}"

    def __repr__(self):
        return self.__str__()


def main():
    troop = []
    for text in inp.split('\n\n'):
        troop.append(Monkey(text, troop))

    for i in range(1000):
        for m in troop:
            m.turn()

    for m in troop:
        print(f"{m} inspected items {m.inspections} times")

    top2 = sorted(troop, key=lambda m: m.inspections, reverse=True)[:2]
    monkeybusiness = prod(m.inspections for m in top2)

    print(monkeybusiness)


if __name__ == '__main__':
    main()
