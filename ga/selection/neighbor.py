# Standard Library
from operator import attrgetter
from typing import Callable, List, Tuple

# Third Party Library
from loguru import logger as log

# Local Module
from ga.config import GAsetting, HillClimbingSetting
from ga.evaluation.basic import basic_evaluation


def get_strongest(
    population: Tuple, setting: GAsetting, obj_func: Callable
) -> Tuple[Tuple, int]:
    new_fit = basic_evaluation(population, setting, obj_func)
    new_max_value = max(new_fit)
    new_strongest = population[new_fit.index(new_max_value)]

    return new_strongest, new_max_value


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
        neighbors = operator.generate_neighbor(target, pop_size)
        strongest, max_value = get_strongest(neighbors, setting, obj_func)

        if max_value > setting.target_fitness:
            setting.target, setting.target_fitness = strongest, max_value
        else:
            local = True

    return [setting.target]
