# Standard Library
from operator import attrgetter
from typing import List, Tuple

# Local Module
from ga.config import GAsetting, HillClimbingSetting, SAsetting


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

    population = operator.generate_neighbor(target, pop_size)
    populations.append(tuple(population))
    return populations


def annealling_init(setting: SAsetting) -> List[Tuple]:
    operator = attrgetter("gene_operator")(setting)
    populations: List[Tuple] = []
    target = operator.generate()
    setting.target = target
    populations.append(tuple([target]))
    return populations
