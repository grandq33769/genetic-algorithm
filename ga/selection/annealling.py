from operator import attrgetter
from loguru import logger as log
from math import exp
from typing import Tuple, Callable, List
from random import random
from ga.config import SAsetting
from ga.selection.neighbor import select_neighbor_from_target
from ga.evaluation.basic import basic_evaluation

def annealling(population: Tuple, fitness: Tuple, setting: SAsetting, obj_func: Callable) -> List:
    new_population = select_neighbor_from_target(population, fitness, setting)

    operator, target = attrgetter("gene_operator", "target")(setting)
    fitness = basic_evaluation(new_population, setting, obj_func)
    fitness_value = max(fitness)
    target_fitness = obj_func(*operator.decode(target))

    max_value = max(fitness)
    target_idx = fitness.index(max_value)
    if fitness_value > target_fitness:
        setting.target = new_population[target_idx]
        setting.count = 0
    else:
        throw = random()
        if throw < exp(
            (fitness_value - target_fitness) / setting.temperature
        ):
            setting.target = new_population[target_idx]
            setting.count = 0
        else:
            setting.count += 1

    return [setting.target]

