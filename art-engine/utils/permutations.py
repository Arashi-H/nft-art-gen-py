""" Calculates the number of combinations that can be made from provided trait layers """

import math

from pathlib import Path

from parse_yaml import read_yaml


def calculate_permutations() -> int:
    config = read_yaml()
    layer_counts = list()

    for layer in config['layers']:
        path = Path.cwd() / 'art-engine' / 'assets' / layer['name']
        trait_count = len([value for value in path.iterdir()])

        if not layer['required']:
            trait_count += 1

        layer_counts.append(trait_count)

    return math.prod(layer_counts)


print(calculate_permutations())
