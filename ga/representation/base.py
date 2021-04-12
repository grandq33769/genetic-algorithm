# Standard Library
from dataclasses import dataclass, field
from typing import Sequence


@dataclass
class Representation:
    min_value: float
    max_value: float
    decimal: int

    def generate(self):
        pass

    def decode(self, gene):
        pass

    def __post_init__(self):
        if self.min_value > self.max_value:
            raise ValueError('min_value must be smaller than max_value')


@dataclass
class GeneOperator:
    representations: Sequence[Representation]
    repre_len: int = field(init=False)

    def __post_init__(self):
        self.repre_len = len(self.representations)

    def generate(self):
        pass

    def decode(self, gene):
        pass

    def crossover(self, first, second, idx):
        pass

    def mutation(self, target, idx):
        pass
