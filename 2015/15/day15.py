#!/usr/bin/env python3
# Advent of Code 2015 Day 15
# https://adventofcode.com/2015/day/15

import pandas as pd
from math import prod


def process_input(calories=True):
    with open('input.txt', 'r') as f:
        lines = f.read().strip().split('\n')

    ingredients = {}
    for line in lines:
        ingredient, prop_str = line.split(': ')
        properties = {}
        for prop in prop_str.split(', '):
            key, val = prop.split()
            if not calories and key == 'calories': continue
            properties[key] = int(val)

        ingredients[ingredient] = properties

    return ingredients


def get_combs():
    combs = []
    for a in range(101):
        for b in range(101 - a):
            for c in range(101 - a - b):
                d = 100 - a - b - c
                if d >= 0:
                    combs.append((a, b, c, d))

    return combs


def main():
    data = process_input(calories=False)

    keys = ['Sprinkles', 'PeanutButter', 'Frosting', 'Sugar']
    combs = get_combs()
    recipes = []

    for comb in combs:
        recipe = dict(zip(keys, comb))
        result = {k: 0 for k in data[keys[0]].keys()}
        for ing, mult in recipe.items():
            for p, v in data[ing].items():
                r = int(v) * mult
                result[p] += r if r > 0 else 0

        output = {'score': prod(result.values())}
        output.update(recipe)
        output.update(result)
        recipes.append(output)


    print(max([r['score'] for r in recipes]))
    df = pd.DataFrame(recipes)
    df.to_csv('recipes.csv', index=None)

if __name__ == '__main__':
    main()
