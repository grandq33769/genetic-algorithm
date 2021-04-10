# Local Module
from ga.config import GAsetting
from ga.main import basic_init
from ga.representation.binary import BinaryGeneOperator, BinaryRepresentation

SETTING = GAsetting(
    pop_size=100,
    crossover_rate=0.3,
    mutation_rate=0.01,
    gene_operator=BinaryGeneOperator(
        [BinaryRepresentation(0, 1, 4), BinaryRepresentation(0, 1, 4)]
    ),
)


def test_basic_init():
    subject = basic_init(SETTING)
    assert isinstance(subject, list)
    assert len(subject) == 1

    population = subject[0]
    assert isinstance(population, tuple)
    assert len(population) == 100
    assert all((isinstance(i, str) for i in population))
