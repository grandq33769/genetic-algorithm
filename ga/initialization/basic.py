# Standard Library
from operator import attrgetter
from typing import List, Tuple

# Local Module
from ga.config import GAsetting


def basic_init(setting: GAsetting) -> List[Tuple]:
    pop_size, operator = attrgetter("pop_size", "gene_operator")(setting)
    populations: List[Tuple] = []
    population = tuple(operator.generate() for _ in range(pop_size))
    populations.append(population)
    return populations
