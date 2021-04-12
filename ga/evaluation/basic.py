# Standard Library
from operator import attrgetter
from typing import Tuple

# Local Module
from ga.config import GAsetting
from ga.main import obj_func


def basic_evaluation(population: Tuple, setting: GAsetting) -> Tuple:
    operator = attrgetter("gene_operator")(setting)
    fitness = tuple(obj_func(*operator.decode(i)) for i in population)
    return fitness
