# Third Party Library
import pytest

# Local Module
from ga.config import GAsetting
from ga.representation.binary import BinaryGeneOperator, BinaryRepresentation

SETTING = GAsetting(
    pop_size=100,
    crossover_rate=0.3,
    mutation_rate=0.01,
    gene_operator=BinaryGeneOperator(
        [BinaryRepresentation(0, 1, 4), BinaryRepresentation(0, 1, 4)]
    ),
)


@pytest.fixture()
def ga_setting():
    yield SETTING
