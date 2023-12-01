# Advent of Code 2022 Day 5
# https://adventofcode.com/2022/day/5

import re
import pyperclip as pc

with open('input.txt', 'r') as f:
    inp = f.read().strip()


def parse_starting_config(start):
    rows = start.split('\n')
    idx = rows[-1]
    rows = rows[:-1]

    output = {}
    for i, char in enumerate(idx):
        if char != ' ':
            output[char] = [c[i] for c in rows if c[i] != ' ']

    return output


def stack_crates(stacks, instructions, part=1):
    exp = r'move (\d+) from (\d) to (\d)'
    for line in instructions.split('\n'):
        qty, source, dest = re.match(exp, line).groups()
        qty = int(qty)

        if part == 1:
            # move crates one at a time
            for _ in range(qty):
                stacks[dest].insert(0, stacks[source].pop(0))
        elif part == 2:
            # move n=qty crates at once
            stacks[dest] = stacks[source][:qty] + stacks[dest]
            stacks[source] = stacks[source][qty:]

    return stacks


def get_message(part):
    start, instructions = inp.split('\n\n')
    stacks = parse_starting_config(start)
    final_config = stack_crates(stacks, instructions, part)
    output = ''.join([s[0] for s in final_config.values()])

    return output


def main():
    pt1 = get_message(part=1)
    pt2 = get_message(part=2)
    print(pt2)
    pc.copy(pt2)


if __name__ == '__main__':
    main()
