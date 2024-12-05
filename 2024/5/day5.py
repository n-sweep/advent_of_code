# Advent of Code 2024 Day 5
# https://adventofcode.com/2024/day/5

with open('puzzle.txt', 'r') as f:
    order, page_sets = f.read().strip().split('\n\n')


# def reorder(rule, pages):


def safe(section):
    for rule in order.split('\n'):
        a, b = rule.split('|')
        if a in section and b in section:
            if section.index(a) > section.index(b):
                return -1

    return int(section[len(section) // 2])


def pt1():
    total = 0
    for ps in page_sets.split('\n'):
        ps = ps.split(',')
        if (m:=safe(ps)) > -1:
            total += m

    print(total)


def main():
    total = 0
    for ps in page_sets.split('\n'):
        ps = ps.split(',')

        if (m:=safe(ps)) > -1:
            continue

        while (m:=safe(ps)) < 0:
            for rule in order.split('\n'):
                a, b = rule.split('|')
                if a in ps and b in ps:
                    if (ia:=ps.index(a)) > (ib:=ps.index(b)):
                        ps.insert(ib, ps.pop(ia))

        total += int(ps[len(ps) // 2])
    print(total)


if __name__ == '__main__':
    main()
