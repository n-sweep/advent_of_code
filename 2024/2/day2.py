# Advent of Code 2024 Day 2
# https://adventofcode.com/2024/day/2

with open('puzzle.txt', 'r') as f:
    reports = [list(map(int, r.strip().split())) for r in f.readlines()]


def safe(report):
    ln = len(report) - 1
    diffs = [report[i] - report[i+1] for i in range(ln)]

    inrange = sum(map(lambda x: abs(x) > 0 and abs(x) < 4, diffs))
    posneg = sum(map(lambda x: x < 0, diffs))

    return (inrange == ln) and (posneg in [0, ln])


def dampen(report):
    for i in range(len(report)):
        r = report[:i] + report[i+1:]
        if safe(r):
            return True
    return False


def main():
    # pt 1
    # print(sum([safe(r) for r in reports]))

    # pt 2
    print(sum([safe(r) or dampen(r) for r in reports]))


if __name__ == '__main__':
    main()
