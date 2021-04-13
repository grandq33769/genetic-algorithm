# Standard Library
from random import random
from typing import List


def separate_pop_by_chance(population: List, chance: float):
    candidates: List = []
    new_population: List = []
    for i in population:
        crossover_throw = random()
        if crossover_throw <= chance:
            # Add individual to candidates pool
            # if the throw smaller than the chance
            candidates.append(i)
        else:
            # Add individual to new population if individual not be chosen
            new_population.append(i)
    return candidates, new_population
