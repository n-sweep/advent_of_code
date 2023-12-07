#!/usr/bin/env python3
# Advent of Code 2022 Day 7
# https://adventofcode.com/2022/day/7

# ordered from lowest to highest value
HANDS = ['11111', '2111', '221', '311', '32', '41', '5']
CARDS = list('23456789TJQKA')
alpha = "abcdefghijklmnopqrstuvwxyz"


# with open('../data/test_1.txt', 'r') as f:
with open('../data/input.txt', 'r') as f:
    lines = f.read().strip().split('\n')


def evaluate_hand(hand):
    counts = {}
    for card in hand:
        if card in counts:
            counts[card] += 1
        else:
            counts[card] = 1

    sorted_counts = sorted(counts.values(), reverse=True)
    hand_type = ''.join([str(s) for s in sorted_counts])
    sort_str = ''.join(alpha[CARDS.index(c)] for c in hand)

    return sort_str, hand_type

def main():
    hands = []
    for line in lines:
        hand, bid = line.split()
        sort_str, hand_type = evaluate_hand(hand)
        hands.append((hand, int(bid), sort_str, hand_type))
        # print(hand, int(bid), sort_str, hand_type)

    # sort by first card
    csort = sorted(hands, key=lambda h: h[2])
    # sort by hand strength
    hsort = sorted(csort, key=lambda h: HANDS.index(h[3]))

    output = sum([(i + 1) * h[1] for i, h in enumerate(hsort)])

    print(output)


if __name__ == '__main__':
    main()
