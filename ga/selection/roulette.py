# Standard Library
from itertools import accumulate
from math import exp
from random import random
from typing import List, Tuple

# Local Module
from ga.config import GAsetting


def float_to_range_idx(target: float, ranges: Tuple) -> int:
    start = 0
    for idx, end in enumerate(ranges):
        if start < target <= end:
            return idx
        start = end
    return 0


def roulette(population: Tuple, fitness: Tuple, setting: GAsetting) -> List:
    new_population: List = []
    # Pre-processing of fitness, exponential all fitness value
    # Normalization of fitness
    processed_fitness = tuple(exp(f) for f in fitness)

    # Percentage of all individuals by fitness
    sum_fitness: float = sum(processed_fitness)
    percentages: Tuple = tuple(f / sum_fitness for f in processed_fitness)

    # Accumulate percentage to 1
    accumulated: Tuple = tuple(accumulate(percentages, lambda a, b: a + b))

    for _ in range(setting.pop_size):
        # Random generate a number from 0..1
        fall = random()

        # Select a index from the accumulated percentage
        target_idx = float_to_range_idx(fall, accumulated)

        # Select candidate from previous populations
        selected = population[target_idx]
        new_population.append(selected)

    return new_population
