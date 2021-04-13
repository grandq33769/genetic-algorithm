# Standard Library
from collections import Counter
from math import exp
from random import random
from typing import List, Tuple

# Third Party Library
from loguru import logger as log

# Local Module
from ga.config import GAsetting, HillClimbingSetting, SAsetting


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


def smaller_than_previous(
    generation: int,
    populations: List[Tuple],
    fitnesses: List[Tuple],
    setting: HillClimbingSetting,
):
    new_pop = populations[-1]
    new_fit = fitnesses[-1]
    new_max_value = max(new_fit)
    new_strongest = new_pop[new_fit.index(new_max_value)]

    target = setting.target
    target_value = setting.target_fitness

    log.debug(
        ' '.join(
            [
                f'{generation}',
                f'{new_strongest=}',
                f'{new_max_value=}',
                f'{target=}',
                f'{target_value=}',
            ]
        )
    )
    larger_than: bool = new_max_value > target_value
    if larger_than:
        setting.target = new_strongest
        setting.target_fitness = new_max_value

    return not larger_than


def is_annealled(
    generation: int,
    populations: List[Tuple],
    fitnesses: List[Tuple],
    setting: SAsetting,
    /,
    terminated_gen: int,
    duplicated_time: int,
):
    setting.temperature = setting.temperature * setting.annealling_rate

    new_pop = populations[-1][0]
    new_fit = fitnesses[-1][0]

    target_value = setting.target_fitness

    if new_fit > target_value:
        setting.target = new_pop
        setting.target_fitness = new_fit
    else:
        throw = random()
        if throw < exp((new_fit - target_value) / setting.temperature):
            setting.target = new_pop
            setting.target_fitness = new_fit

    fitness, time = Counter(fitnesses).most_common(1)[0]
    log.debug(
        ' '.join(
            [
                f'{generation=}',
                f'{len(populations)=}',
                f'{len(fitness)=}',
                f'{terminated_gen=}',
                f'{duplicated_time=}',
            ]
        )
    )

    annealled: bool = time > duplicated_time
    exceeded: bool = generation > terminated_gen
    return annealled or exceeded
