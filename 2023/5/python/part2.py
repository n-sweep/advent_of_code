#!/usr/bin/env python3
# Advent of Code 2022 Day 5
# https://adventofcode.com/2022/day/5

with open('../data/input.txt', 'r') as f:
    data = f.read().strip().split('\n\n')


def parse_maps(text):
    maps = {}

    for map_str in text:
        map = []
        split_map = map_str.split('\n')
        key = split_map[0].split()[0].replace('to-', '')

        for dest, src, n in [s.split() for s in split_map[1:]]:
            src, dest, n = int(src), int(dest), int(n),
            map.append(((src, src + n), (dest, dest + n)))

        maps[key] = map

    return maps


def main():
    seeds = [int(s) for s in data[0].split()[1:]]
    maps = parse_maps(data[1:])

    seq = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
    locs = []

    for i in range(0, len(seeds) - 1, 2):
        for seed in range(start:=seeds[i], start + seeds[i + 1]):
            val = seed
            for j in range(len(seq) - 1):
                map = maps[f"{seq[j]}-{seq[j + 1]}"]

                # get each mapped range
                for (src_lo, src_hi), (dest_lo, dest_hi) in map:
                    if val >= src_lo and val < src_hi:
                        diff = val - src_lo
                        val = dest_lo + diff
                        break

            locs.append(val)

    print(min(locs))


if __name__ == '__main__':
    main()
