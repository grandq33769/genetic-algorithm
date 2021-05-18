# Standard Library
from math import exp
from operator import attrgetter
from random import random
from typing import Callable, List, Tuple

# Third Party Library
from loguru import logger as log

# Local Module
from ga.config import SAsetting
from ga.selection.neighbor import get_strongest


def annealling(
    population: Tuple, fitness: Tuple, setting: SAsetting, obj_func: Callable
) -> List:
    operator, target, pop_size = attrgetter(
        "gene_operator", "target", "pop_size"
    )(setting)
    log.debug(
        ' '.join(
            [
                f'{population=}',
                f'{fitness=}',
            ]
        )
    )
    neighbors = operator.generate_neighbor(target, pop_size)
    strongest, max_value = get_strongest(neighbors, setting, obj_func)

    if max_value > setting.target_fitness:
        setting.target, setting.target_fitness = strongest, max_value
        setting.count = 0
    else:
        throw = random()
        if throw < exp(
            (max_value - setting.target_fitness) / setting.temperature
        ):
            setting.target, setting.target_fitness = strongest, max_value
            setting.count = 0
        else:
            setting.count += 1

    return [setting.target]
