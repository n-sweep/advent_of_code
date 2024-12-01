# Advent of Code 2024 Day 1
# https://adventofcode.com/2024/day/1

with open('input.txt', 'r') as f:
    lines = f.readlines()


def pt1():

    left = []
    right = []
    for line in lines:
        l, r = line.strip().split()
        left.append(int(l))
        right.append(int(r))

    result = sum([abs(l-r) for l, r in zip(sorted(left), sorted(right))])

    print(result)


def main():
    left = []
    right = []
    for line in lines:
        l, r = line.strip().split()
        left.append(int(l))
        right.append(int(r))

    counts = {}
    for i in right:
        counts[i] = counts.get(i, 0) + 1

    result = sum([i * counts.get(i, 0) for i in left])

    print(result)

if __name__ == '__main__':
    main()
