# Standard Library
import sys
from itertools import product
from math import sin
from operator import attrgetter
from typing import List, Tuple

# Third Party Library
from loguru import logger as log
from numpy import mean

# Local Module
from ga.config import GAconfig, GAsetting


def obj_func(x1, x2):
    assert isinstance(x1, (int, float))
    assert isinstance(x2, (int, float))
    assert 0 <= x1 <= 1
    assert 0 <= x2 <= 1

    x1 = round(x1, 4)
    x2 = round(x2, 4)

    result = cal_term_1(x1, x2) * cal_term_2(x1, x2)
    return result


def cal_term_1(x1, x2):
    return (x1 ** 2 + x2 ** 2) ** 0.25


def cal_term_2(x1, x2):
    def inner_term(x1, x2):
        return (x1 ** 2 + x2 ** 2) ** 0.1

    return sin(50 * inner_term(x1, x2)) ** 2 + 1


def brute_force():
    range_list = [x / 10000 for x in range(10001)]
    candidates = list(product(range_list, repeat=2))
    max_value = ((), sys.maxsize * -1)
    min_value = ((), sys.maxsize)
    for c in candidates:
        result = obj_func(*c)
        if result > max_value[1]:
            max_value = (c, result)
        elif result < min_value[1]:
            min_value = (c, result)

    return max_value, min_value


def genetic_algorithm(config: GAconfig):
    setting: GAsetting = config.setting
    initialize, evaluation, select = attrgetter(
        "initialize", "evaluation", "select"
    )(config)
    is_terminated, crossover, mutation = attrgetter(
        "is_terminated", "crossover", "mutation"
    )(config)

    generation: int = 0
    fitnesses: List[Tuple] = []
    populations: List[Tuple] = initialize(setting)
    log.info(f'Populations Initialization: {populations}')
    fitness: Tuple = evaluation(populations[generation], setting)
    log.info(f'Fitness of First Generation: {fitness}')
    log.info(f'Average Fitness of First Generation: {mean(fitness)}')
    fitnesses.append(fitness)
    log.info('Evolution Start:')

    while not is_terminated(generation, populations, fitnesses, setting):
        generation += 1
        # Next Generation
        population: List = select(
            populations[generation - 1], fitness, setting
        )
        # Alter
        population = crossover(population, setting)
        population, _ = mutation(population, setting)
        # Add new generation
        populations.append(tuple(population))
        # Evaluation
        fitness = evaluation(population, setting)
        fitnesses.append(fitness)
        log.info((f'{generation=} {mean(fitness)=}'))
        log.debug((f'{population=} {fitness=}'))
    log.info('Evolution End')
    return populations, fitnesses


def basic_evaluation(population: Tuple, setting: GAsetting) -> Tuple:
    operator = attrgetter("gene_operator")(setting)
    fitness = tuple(obj_func(*operator.decode(i)) for i in population)
    return fitness
