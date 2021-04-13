# Standard Library
from dataclasses import dataclass, field
from math import ceil, log
from random import randint
from typing import List, Sequence, Union

# Third Party Library
from loguru import logger

from .base import GeneOperator, Representation


@dataclass
class BinaryRepresentation(Representation):
    max: int = field(init=False)
    min: int = field(init=False)
    offset: int = field(init=False)
    num_of_bits: int = field(init=False)

    def __post_init__(self):
        self.max = int(self.max_value * (10 ** self.decimal))
        self.min = int(self.min_value * (10 ** self.decimal))
        self.offset = self.max - self.min
        self.num_of_bits = ceil(log(self.offset, 2))
        logger.debug(f'{self.__dict__}')

    def generate(self) -> str:
        random_offset = bin(randint(0, self.offset))
        chromosome = self.format(random_offset)
        return chromosome

    def encode(self, value: float) -> str:
        bin_string = bin(int(value * (10 ** self.decimal)) - self.min)
        chromosome = self.format(bin_string)
        return chromosome

    def decode(self, gene) -> float:
        return (self.min + int(gene, 2)) / (10 ** self.decimal)

    def format(self, bin_string: str) -> str:
        return str(bin_string)[2:].zfill(self.num_of_bits)


class BinaryGeneOperator(GeneOperator):
    representations: Sequence[BinaryRepresentation]

    @property
    def length(self):
        return sum([r.num_of_bits for r in self.representations])

    def generate(self) -> str:
        gene = ''.join([r.generate() for r in self.representations])
        return gene

    def encode(self, phenotype: Union[tuple, list]) -> str:
        gene = ''
        if phenotype_len := len(phenotype) != self.repre_len:
            logger.warning(
                f'The length of phenotype is "{phenotype_len}" ',
                'but the generator ',
                f'only can encode the phenotype with "{self.repre_len}" long.',
            )
            return gene

        gene = ''.join(
            [r.encode(p) for r, p in zip(self.representations, phenotype)]
        )
        return gene

    def decode(self, gene: str) -> tuple:
        phenotype: List[Union[int, float]] = list()
        un_decoded = gene
        if gene_len := len(gene) != self.length:
            logger.warning(
                f'The length of gene is "{gene_len}" but the generator '
                f'only can decode the gene with "{self.length}" long.'
            )
            return tuple(phenotype)
        for r in self.representations:
            target, un_decoded = (
                un_decoded[: r.num_of_bits],
                un_decoded[r.num_of_bits :],
            )
            phenotype.append(r.decode(target))

        return tuple(phenotype)

    def crossover(self, first: str, second: str, idx: int):

        cross_first = ''.join([first[:idx], second[idx], first[idx + 1 :]])
        cross_second = ''.join([second[:idx], first[idx], second[idx + 1 :]])
        return cross_first, cross_second

    def mutation(self, target: str, idx: int):
        mutated_bit = '1' if target[idx] == '0' else '0'
        mutated_target = target[:idx] + mutated_bit + target[idx + 1 :]
        return mutated_target
