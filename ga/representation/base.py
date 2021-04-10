# Standard Library
from dataclasses import dataclass


@dataclass
class GeneGenerator:
    def generate(self):
        pass

    def decode(self, gene):
        pass


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
