# Standard Library
from operator import attrgetter
from random import randint, random
from typing import List

# Local Module
from ga.config import GAsetting


def pairwise(iterable):
    gen = iter(iterable)
    while True:
        a, b = next(gen, None), next(gen, None)
        if a is None or b is None:
            break
        yield a, b


def one_bit_crossover(population: List, setting: GAsetting):

    crossover_rate, operator = attrgetter('crossover_rate', 'gene_operator')(
        setting
    )
    new_population: List = []
    candidates: List = []
    for i in population:
        crossover_throw = random()
        if crossover_throw <= crossover_rate:
            # Add individual to candidates pool
            # if the throw smaller than the mutation rate
            candidates.append(i)
        else:
            # Add individual to new population if individual not crossover
            new_population.append(i)

    # Crossover must be even candidates, remove the remain candidate and
    # Add to new population
    if len_candidates := len(candidates) % 2 != 0:
        abandoned_idx: int = randint(0, len_candidates - 1)
        new_population.append(candidates.pop(abandoned_idx))

    for first, second in pairwise(candidates):
        crossover_idx = randint(0, operator.length - 1)
        new_first, new_second = operator.crossover(
            first, second, crossover_idx
        )
        new_population.extend([new_first, new_second])

    return new_population
