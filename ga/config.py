# Standard Library
import os
from dataclasses import dataclass
from typing import Callable

# Local Module
from ga.representation.base import GeneOperator

POP_SIZE = int(os.environ.get('POP_SIZE', 10))
CROSSOVER_RATE = float(os.environ.get('CROSSOVER_RATE', 0.4))
MUTATION_RATE = float(os.environ.get('MUTATION_RATE', 0.01))


@dataclass
class GAsetting:
    pop_size: int
    crossover_rate: float
    mutation_rate: float
    gene_operator: GeneOperator


@dataclass
class HillClimbingSetting(GAsetting):
    target: tuple = tuple()
    target_fitness: float = 0.0


@dataclass
class SAsetting(HillClimbingSetting):
    temperature: float = 100
    annealling_rate: float = 0.9


@dataclass
class GAconfig:
    setting: GAsetting
    initialize: Callable
    evaluation: Callable
    select: Callable
    is_terminated: Callable
    crossover: Callable
    mutation: Callable


@dataclass
class HillClimbingConfig(GAconfig):
    setting: HillClimbingSetting


@dataclass
class SAconfig(GAconfig):
    setting: SAsetting
