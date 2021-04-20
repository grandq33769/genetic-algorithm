# Standard Library
from dataclasses import dataclass, field
from random import randint
from typing import List, Sequence, Tuple, Union

# Third Party Library
from loguru import logger


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

    @property
    def length(self):
        return len(self.representations)

    def generate(self):
        pass

    def decode(self, gene) -> tuple:
        return tuple([gene, self.length])

    def format(self, gene: str) -> str:
        decoded = self.decode(gene)
        decoded_str = tuple(str(i) for i in decoded)
        return ','.join(decoded_str)

    def crossover(self, first, second, idx):
        pass

    def mutation(self, target, idx) -> Tuple:
        return (self, target, idx)

    def valid_gene(self, gene: Union[str, tuple]) -> bool:
        phenotype = self.decode(gene)
        valids = [
            r.min_value <= p <= r.max_value
            for p, r in zip(phenotype, self.representations)
        ]
        return all(valids)

    def is_valid_length(self, gene: tuple) -> bool:
        gene_len = len(gene)
        valid = gene_len == self.length
        if not valid:
            logger.warning(
                f'The length of gene is "{gene_len}" but the generator '
                f'only can decode the gene with "{self.length}" long.'
            )
        return valid

    def generate_neighbor(self, target, num_of_neighbors: int) -> List:
        neighbors: List = []
        while len(neighbors) != num_of_neighbors:
            neighbor_idx = randint(0, self.length - 1)
            neighbor = self.mutation(target, neighbor_idx)
            if self.valid_gene(neighbor):
                neighbors.append(neighbor)
        return neighbors
