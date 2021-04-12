# Standard Library
from operator import attrgetter
from random import randint
from typing import List, Tuple

# Local Module
from ga.config import GAsetting, HillClimbingSetting


def basic_init(setting: GAsetting) -> List[Tuple]:
    pop_size, operator = attrgetter("pop_size", "gene_operator")(setting)
    populations: List[Tuple] = []
    population = tuple(operator.generate() for _ in range(pop_size))
    populations.append(population)
    return populations


def init_by_neighbors(setting: HillClimbingSetting) -> List[Tuple]:
    pop_size, operator = attrgetter("pop_size", "gene_operator")(setting)
    populations: List[Tuple] = []
    population: List = []
    target = operator.generate()
    setting.target = target
    while len(population) != pop_size:
        neighbor_idx = randint(0, operator.length - 1)
        neighbor = operator.mutation(target, neighbor_idx)
        if operator.valid_gene(neighbor):
            population.append(neighbor)
    populations.append(tuple(population))
    return populations
