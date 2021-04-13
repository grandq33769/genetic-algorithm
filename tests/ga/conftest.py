# Third Party Library
import pytest

# Local Module
from ga.config import GAsetting, HillClimbingSetting, SAsetting
from ga.representation.binary import BinaryGeneOperator, BinaryRepresentation
from ga.representation.float import FloatGeneOperator, FloatRepresentation

SETTING = GAsetting(
    pop_size=100,
    crossover_rate=0.3,
    mutation_rate=0.01,
    gene_operator=BinaryGeneOperator(
        [BinaryRepresentation(0, 1, 4), BinaryRepresentation(0, 1, 4)]
    ),
)

FLOAT_SETTING = GAsetting(
    pop_size=100,
    crossover_rate=0.3,
    mutation_rate=0.01,
    gene_operator=FloatGeneOperator(
        [FloatRepresentation(0, 1, 4), FloatRepresentation(0, 1, 4)]
    ),
)

HC_SETTING = HillClimbingSetting(
    pop_size=10,
    crossover_rate=0.3,
    mutation_rate=0.01,
    gene_operator=BinaryGeneOperator(
        [BinaryRepresentation(0, 1, 4), BinaryRepresentation(0, 1, 4)]
    ),
)

SA_SETTING = SAsetting(
    pop_size=1,
    crossover_rate=0.3,
    mutation_rate=0.01,
    gene_operator=BinaryGeneOperator(
        [BinaryRepresentation(0, 1, 4), BinaryRepresentation(0, 1, 4)]
    ),
    temperature=10000,
)


@pytest.fixture()
def ga_setting():
    yield SETTING


@pytest.fixture()
def ga_float_setting():
    yield FLOAT_SETTING


@pytest.fixture()
def hc_setting():
    yield HC_SETTING


@pytest.fixture()
def sa_setting():
    yield SA_SETTING
