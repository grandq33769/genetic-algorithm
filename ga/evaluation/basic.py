# Standard Library
from operator import attrgetter
from typing import Tuple

# Local Module
from ga.config import GAsetting, HillClimbingSetting
from ga.main import obj_func


def basic_evaluation(population: Tuple, setting: GAsetting) -> Tuple:
    operator = attrgetter("gene_operator")(setting)
    fitness = tuple(obj_func(*operator.decode(i)) for i in population)
    return fitness


def hc_evaluation(population: Tuple, setting: HillClimbingSetting) -> Tuple:
    operator, target = attrgetter("gene_operator", "target")(setting)
    setting.target_fitness = obj_func(*operator.decode(target))
    fitness = basic_evaluation(population, setting)
    return fitness
