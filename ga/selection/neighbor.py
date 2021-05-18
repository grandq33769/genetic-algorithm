# Standard Library
from operator import attrgetter
from random import randint
from typing import Callable, List, Tuple

# Third Party Library
from loguru import logger as log

# Local Module
from ga.config import HillClimbingSetting
from ga.evaluation.basic import basic_evaluation


def select_neighbor_from_target(
    population: Tuple,
    fitness: Tuple,
    setting: HillClimbingSetting,
    obj_func: Callable,
) -> List:
    pop_size, operator, target = attrgetter(
        "pop_size", "gene_operator", "target"
    )(setting)
    log.debug(
        ' '.join(
            [
                f'{population=}',
                f'{fitness=}',
            ]
        )
    )
    local: bool = False
    while not local:
        new_population: List = []
        while len(new_population) != pop_size:
            neighbor_idx = randint(0, operator.length - 1)
            neighbor = operator.mutation(target, neighbor_idx)
            if operator.valid_gene(neighbor):
                new_population.append(neighbor)

        new_fit = basic_evaluation(tuple(new_population), setting, obj_func)
        new_max_value = max(new_fit)
        new_strongest = new_population[new_fit.index(new_max_value)]
        log.debug(f'{setting.target=} {new_strongest=}')
        if setting.target_fitness < new_max_value:
            log.debug(f'{new_max_value=} {setting.target_fitness=}')
            setting.target = new_strongest
            log.debug(f'{setting.target=} {new_strongest=}')
            setting.target_fitness = new_max_value
        else:
            local = True

    return [new_strongest]
