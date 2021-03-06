# Standard Library
from operator import attrgetter
from random import randint
from typing import List

# Third Party Library
from loguru import logger as log

# Local Module
from ga.config import GAsetting
from ga.utils import separate_pop_by_chance


def pairwise(iterable):
    gen = iter(iterable)
    while True:
        a, b = next(gen, None), next(gen, None)
        if a is None or b is None:
            break
        yield a, b


def one_bit_crossover(population: List, setting: GAsetting):

    crossover_rate, operator = attrgetter('crossover_rate', 'gene_operator')(
        setting
    )
    candidates, new_population = separate_pop_by_chance(
        population, crossover_rate
    )
    # Crossover must be even candidates, remove the remain candidate and
    # Add to new population
    if len_candidates := len(candidates) % 2 != 0:
        abandoned_idx: int = randint(0, len_candidates - 1)
        new_population.append(candidates.pop(abandoned_idx))

    for first, second in pairwise(candidates):
        valid_first, valid_second = False, False
        while not all([valid_first, valid_second]):
            crossover_idx = randint(0, operator.length - 1)
            new_first, new_second = operator.crossover(
                first, second, crossover_idx
            )
            valid_first, valid_second = (
                operator.valid_gene(new_first),
                operator.valid_gene(new_second),
            )
        new_population.extend([new_first, new_second])

    return new_population


def no_ops(population: List, setting: GAsetting) -> List:
    log.debug(f'Mutation No Operations : {setting.pop_size=}')
    return population
