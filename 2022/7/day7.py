#!/usr/bin/env python3
# Advent of Code 2022 Day 7
# https://adventofcode.com/2022/day/7

import pyperclip as pc

with open('./input.txt', 'r') as f:
    inp = f.read().strip()


class BaseAddable:
    def __add__(self, other):
        if isinstance(other, BaseAddable):
            return self.size + other.size
        else:
            return self.size + int(other)

    def __radd__(self, other):
        return self.__add__(other)


class File(BaseAddable):
    def __init__(self, size, name):
        self.size = size
        self.name = name


class Directory(BaseAddable):
    def __init__(self, name, parent=None):
        self.name = name
        self.parent = parent
        self.files = list()
        self.dirs = list()

    @property
    def size(self):
        if self.files or self.dirs:
            return sum(self.files) + sum(self.dirs)
        else:
            return 0


class Builder:
    def __init__(self, lines):
        self.lines = (ln.split(' ') for ln in lines)
        self.root = Directory('/')
        self.loc = self.root

    @property
    def next(self):
        return next(self.lines, None)

    def ls(self):
        ln = self.next

        while ln:
            if ln[0] == '$':
                self.process_command(ln[1:])
            elif ln[0] == 'dir':
                self.mkdir(ln[1])
            else:
                self.touch(ln)

            ln = self.next

    def cd(self, dir):
        if dir == '/':
            self.loc = self.root
        elif dir == '..':
            self.loc = self.loc.parent
        else:
            dirs = {d.name: d for d in self.loc.dirs}
            self.loc = dirs[dir]

    def touch(self, file):
        size, name = file
        f = File(int(size), name)
        self.loc.files.append(f)

    def mkdir(self, name):
        dir = Directory(name, self.loc)
        self.loc.dirs.append(dir)

    def process_command(self, cmd):
        if cmd[0] == 'cd':
            self.cd(cmd[1])
        else:
            self.ls()

    def build(self):
        self.ls()
        return self.root


def get_dirs(directory, log=[]):
    s = directory.size
    log.append(s)
    for dir in directory.dirs:
        get_dirs(dir, log)

    return log


def main():
    builder = Builder(inp.split('\n'))
    root = builder.build()
    log = get_dirs(root)

    # pt1
    # n = sum([l for l in log if l <= 100000])

    # pt2
    total = 70000000
    update = 30000000
    used = root.size
    avail = total - used
    need = update - avail
    candidates = [i for i in log if i >= need]
    n = min(candidates)

    print(n)
    pc.copy(n)


if __name__ == '__main__':
    main()
