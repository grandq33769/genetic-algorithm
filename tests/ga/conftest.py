# Third Party Library
import pytest

# Local Module
from ga.config import GAsetting, HillClimbingSetting, NichingSetting, SAsetting
from ga.representation.binary import BinaryGeneOperator, BinaryRepresentation
from ga.representation.float import FloatGeneOperator, FloatRepresentation


@pytest.fixture()
def ga_setting():
    yield GAsetting(
        pop_size=30,
        crossover_rate=0.3,
        mutation_rate=0.01,
        gene_operator=BinaryGeneOperator(
            [BinaryRepresentation(0, 1, 4), BinaryRepresentation(0, 1, 4)]
        ),
    )


@pytest.fixture()
def ga_float_setting():
    yield GAsetting(
        pop_size=30,
        crossover_rate=0.3,
        mutation_rate=0.01,
        gene_operator=FloatGeneOperator(
            [FloatRepresentation(0, 1, 4), FloatRepresentation(0, 1, 4)]
        ),
    )


@pytest.fixture()
def hc_setting():
    yield HillClimbingSetting(
        pop_size=30,
        crossover_rate=0.3,
        mutation_rate=0.01,
        gene_operator=BinaryGeneOperator(
            [BinaryRepresentation(0, 1, 4), BinaryRepresentation(0, 1, 4)]
        ),
    )


@pytest.fixture()
def hc_setting_float():
    yield HillClimbingSetting(
        pop_size=30,
        crossover_rate=0.3,
        mutation_rate=0.01,
        gene_operator=FloatGeneOperator(
            [FloatRepresentation(0, 1, 4), FloatRepresentation(0, 1, 4)]
        ),
    )


@pytest.fixture()
def sa_setting():
    yield SAsetting(
        pop_size=30,
        crossover_rate=0.3,
        mutation_rate=0.01,
        gene_operator=BinaryGeneOperator(
            [BinaryRepresentation(0, 1, 4), BinaryRepresentation(0, 1, 4)]
        ),
        temperature=100000,
        annealling_rate=0.9,
    )


@pytest.fixture()
def sa_setting_float():
    yield SAsetting(
        pop_size=30,
        crossover_rate=0.3,
        mutation_rate=0.01,
        gene_operator=FloatGeneOperator(
            [FloatRepresentation(0, 1, 4), FloatRepresentation(0, 1, 4)]
        ),
        temperature=100000,
        annealling_rate=0.9,
    )


def niching_setting_float():
    yield NichingSetting(
        pop_size=30,
        crossover_rate=0.3,
        mutation_rate=0.01,
        gene_operator=(
            [
                FloatRepresentation(-0.5, 1.5, 3),
                FloatRepresentation(-0.5, 1.5, 3),
            ]
        ),
        restrict_distance=0.5,
        power=2,
    )
