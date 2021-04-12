# Standard Library
from operator import attrgetter
from random import randint
from typing import List

# Third Party Library
from loguru import logger as log

# Local Module
from ga.config import GAsetting
from ga.utils import separate_pop_by_chance


def one_bit_mutation(population: List, setting: GAsetting):
    mutation_rate, operator = attrgetter('mutation_rate', 'gene_operator')(
        setting
    )
    candidates, new_population = separate_pop_by_chance(
        population, mutation_rate
    )
    occurred: bool = bool(candidates)
    for candidate in candidates:
        valid = False
        while not valid:
            mutation_idx = randint(0, operator.length - 1)
            mutated = operator.mutation(candidate, mutation_idx)
            valid = operator.valid_gene(mutated)
        log.debug(f'{candidate=}, {mutated=}, {mutation_idx=}')
        new_population.append(mutated)
    return new_population, occurred
