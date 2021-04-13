# Standard Library
from operator import attrgetter
from random import randint
from typing import List, Tuple

# Third Party Library
from loguru import logger as log

# Local Module
from ga.config import HillClimbingSetting


def select_neighbor_from_target(
    population: Tuple, fitness: Tuple, setting: HillClimbingSetting
) -> List:
    pop_size, operator, target = attrgetter(
        "pop_size", "gene_operator", "target"
    )(setting)
    log.debug(
        ' '.join(
            [
                f'{population=}',
                f'{fitness=}',
                f'{population=}',
            ]
        )
    )
    new_population: List = []
    while len(new_population) != pop_size:
        neighbor_idx = randint(0, operator.length - 1)
        neighbor = operator.mutation(target, neighbor_idx)
        if operator.valid_gene(neighbor):
            new_population.append(neighbor)
    return new_population
