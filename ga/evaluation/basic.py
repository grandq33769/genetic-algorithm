# Standard Library
from math import exp
from operator import attrgetter
from random import randint, random
from typing import Callable, Tuple

# Third Party Library
from numpy import mean

# Local Module
from ga.config import GAsetting, HillClimbingSetting, SAsetting


def basic_evaluation(
    population: Tuple, setting: GAsetting, obj_func: Callable
) -> Tuple:
    operator = attrgetter("gene_operator")(setting)
    fitness = tuple(obj_func(*operator.decode(i)) for i in population)
    return fitness


def hc_evaluation(
    population: Tuple, setting: HillClimbingSetting, obj_func: Callable
) -> Tuple:
    operator, target = attrgetter("gene_operator", "target")(setting)
    setting.target_fitness = obj_func(*operator.decode(target))
    fitness = basic_evaluation(population, setting, obj_func)
    return fitness
