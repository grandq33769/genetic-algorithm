# Standard Library
from typing import List, Tuple

# Third Party Library
from loguru import logger as log

# Local Module
from ga.config import GAsetting, HillClimbingSetting


def is_terminated_by_generation(
    generation: int,
    populations: List[Tuple],
    fitnesses: List[Tuple],
    setting: GAsetting,
    /,
    terminated_gen: int,
) -> bool:
    log.debug(
        ' '.join(
            [
                f'{generation=}',
                f'{len(populations)=}',
                f'{len(fitnesses)=}',
                f'{setting=}',
                f'{terminated_gen=}',
            ]
        )
    )
    return generation > terminated_gen


def is_strongest_diff_from_previous(
    generation: int,
    populations: List[Tuple],
    fitnesses: List[Tuple],
    setting: HillClimbingSetting,
):
    # Can not compare if there is only one generation
    if generation < 1:
        return False

    new_pop = populations[-1]
    new_fit = fitnesses[-1]
    new_max_value = max(new_fit)
    new_strongest = new_pop[new_fit.index(new_max_value)]

    operator = setting.gene_operator
    target = setting.target
    target_value = setting.target_fitness

    log.debug(
        ' '.join(
            [
                f'{operator=}',
                f'{new_strongest=}',
                f'{new_max_value=}',
                f'{target=}',
                f'{target_value=}',
            ]
        )
    )
    replacement: bool = new_max_value > target_value
    if replacement:
        setting.target = new_strongest
        setting.target_fitness = new_max_value

    return replacement
