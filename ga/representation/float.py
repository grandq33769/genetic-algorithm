# Standard Library
from dataclasses import dataclass
from random import uniform
from typing import List, Sequence, Union

# Third Party Library
from loguru import logger

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

    @property
    def length(self):
        return len(self.representations)

    def generate(self) -> tuple:
        gene = tuple(r.generate for r in self.representations)
        return gene

    def decode(self, gene: tuple) -> tuple:
        phenotype: List[Union[int, float]] = list()
        if gene_len := len(gene) != self.length:
            logger.warning(
                f'The length of gene is "{gene_len}" but the generator '
                f'only can decode the gene with "{self.length}" long.'
            )
            return tuple(phenotype)
        for r, g in zip(self.representations, gene):
            phenotype.append(r.decode(g))

        return tuple(phenotype)

    def valid_gene(self, gene: tuple) -> bool:
        phenotype = self.decode(gene)
        valids = [
            r.min_value <= p <= r.max_value
            for p, r in zip(phenotype, self.representations)
        ]
        return all(valids)

    def crossover(self, first: tuple, second: tuple, idx: int):
        cross_first = first[:idx] + tuple([second[idx]]) + first[idx + 1 :]
        cross_second = second[:idx] + tuple([first[idx]]) + second[idx + 1 :]

        return cross_first, cross_second

    def mutation(self, target: tuple, idx: int):
        repre = self.representations[idx]
        random_float = uniform(repre.min_value, repre.max_value)
        mutated_dna = tuple([round(random_float, repre.decimal)])
        mutated_target = target[:idx] + mutated_dna + target[idx + 1 :]
        return mutated_target
