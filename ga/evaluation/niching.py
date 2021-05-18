# Standard Library
from itertools import combinations
from math import dist
from operator import attrgetter
from typing import Callable, List, Tuple

# Third Party Library
from loguru import logger

# Local Module
from ga.config import NichingSetting


def cal_sharing_fitness(
    population: Tuple, setting: NichingSetting, all_pairs_idx: List
) -> List:
    operator = attrgetter("gene_operator")(setting)
    sharing_fitness = list()
    for first_idx, second_idx in all_pairs_idx:
        first_candidate = population[first_idx]
        second_candidate = population[second_idx]
        distance = dist(
            operator.decode(first_candidate), operator.decode(second_candidate)
        )
        if distance < setting.restrict_distance:
            sharing_value = 1 - (
                (distance / setting.restrict_distance) ** setting.power
            )
        else:
            sharing_value = 0
        sharing_fitness.append(sharing_value)
    return sharing_fitness


def niching_evaluation(
    population: Tuple, setting: NichingSetting, obj_func: Callable
) -> Tuple:
    operator = attrgetter("gene_operator")(setting)
    fitness = list()
    all_pairs_idx = list(combinations(range(setting.pop_size), 2))
    sharing_fitness = cal_sharing_fitness(population, setting, all_pairs_idx)

    for idx, p in enumerate(population):
        neighbors_idx = tuple(
            pairs_idx
            for pairs_idx, pairs in enumerate(all_pairs_idx)
            if idx in pairs
        )
        logger.debug(f'{idx=} {p=} {neighbors_idx=}')
        sharing_sum = sum([sharing_fitness[idx] for idx in neighbors_idx])
        if sharing_sum == 0:
            sharing_sum = 1
        fitness_value = obj_func(*operator.decode(p)) / sharing_sum
        fitness.append(fitness_value)

    return tuple(fitness)
