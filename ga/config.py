# Standard Library
import os
from dataclasses import dataclass
from typing import Callable

POP_SIZE = int(os.environ.get('POP_SIZE', 10))
CROSSOVER_RATE = float(os.environ.get('CROSSOVER_RATE', 0.4))
MUTATION_RATE = float(os.environ.get('MUTATION_RATE', 0.01))


@dataclass
class GAsetting:
    pop_size: int
    crossover_rate: float
    mutation_rate: float


@dataclass
class GAconfig:
    setting: GAsetting
    initialize: Callable
    evaluation: Callable
    select: Callable
    is_terminated: Callable
    crossover: Callable
    mutation: Callable
