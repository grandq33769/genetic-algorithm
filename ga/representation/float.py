# Standard Library
from dataclasses import dataclass
from random import uniform
from typing import List, Sequence, Union

from .base import GeneOperator, Representation


@dataclass
class FloatRepresentation(Representation):
    def generate(self) -> float:
        random_value = uniform(self.min_value, self.max_value)
        return round(random_value, self.decimal)

    def encode(self, value: float) -> float:
        return round(value, self.decimal)

    def decode(self, gene: float) -> float:
        return round(gene, self.decimal)


class FloatGeneOperator(GeneOperator):
    representations: Sequence[FloatRepresentation]

    def generate(self) -> tuple:
        gene = tuple(r.generate() for r in self.representations)
        return gene

    def decode(self, gene: tuple) -> tuple:
        phenotype: List[Union[int, float]] = list()
        if not self.is_valid_length(gene):
            return tuple(phenotype)
        for r, g in zip(self.representations, gene):
            phenotype.append(r.decode(g))

        return tuple(phenotype)

    def crossover(self, first: tuple, second: tuple, idx: int):
        cross_first = first[:idx] + tuple([second[idx]]) + first[idx + 1 :]
        cross_second = second[:idx] + tuple([first[idx]]) + second[idx + 1 :]

        return cross_first, cross_second

    def _mutation(self, target: tuple, idx: int):
        repre = self.representations[idx]
        target_value = target[idx]
        step = (repre.max_value - repre.min_value) / 10
        random_float = uniform(target_value - step, target_value + step)
        mutated_dna = tuple([round(random_float, repre.decimal)])
        mutated_target = target[:idx] + mutated_dna + target[idx + 1 :]
        return mutated_target

    def mutation(self, target: tuple, idx: int):

        mutated_target = target
        for i, _ in enumerate(target):
            mutated_target = self._mutation(target, i)
        return mutated_target
