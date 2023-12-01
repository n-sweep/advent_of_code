#!/usr/bin/env python3
# Advent of Code 2022 Day 10
# https://adventofcode.com/2022/day/10

from pyperclip import copy
import numpy as np

with open('./input.txt', 'r') as f:
    instructions = f.read().strip().split('\n')


def pt1():
    cycles = []
    x = 1
    for instruction in instructions:
        cycles.append(x)
        if instruction != 'noop':
            cycles.append(x)
            v = int(instruction.split()[1])
            x += v

    cycles.append(x)
    strengths = [(i + 1) * c for i, c in enumerate(cycles)]

    return sum([strengths[i-1] for i in [20, 60, 100, 140, 180, 220]])


class CRT:
    pos = 1
    cycles = 0
    pending = []
    display = np.zeros((6, 40))

    def __init__(self, instructions):
        self.inst = instructions

    @property
    def x(self):
        return self.cycles % 40

    @property
    def y(self):
        return self.cycles // 40

    @property
    def sprite(self):
        s = np.zeros(40)
        l = self.pos-1 if self.pos-1 > 0 else 0
        r = self.pos+2
        s[l:r] = 1
        return s.astype(bool)

    def get_move(self):
        if self.pending:
            return self.pending.pop()
        elif len(self.inst) > 0:
            i = self.inst.pop(0)
            if i != 'noop':
                v = int(i.split()[1])
                self.pending.append(v)

        return 0

    def cycle(self):
        # draw pixel
        if self.sprite[self.x]:
            self.display[self.y][self.x] = True

        move = self.get_move()
        self.pos += move
        self.cycles += 1

    def run(self):
        while len(self.inst) > 0:
            self.cycle()

    def print(self):
        db = self.display.astype(bool)
        starr = np.where(db, '#', '.')
        print('\n'.join(''.join(r) for r in starr))


def main():
    c = CRT(instructions)
    c.run()
    c.print()
    # copy(str(result))


if __name__ == '__main__':
    main()
