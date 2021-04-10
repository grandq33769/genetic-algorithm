# Local Module
from ga.main import basic_init


def test_basic_init(ga_setting):
    subject = basic_init(ga_setting)
    assert isinstance(subject, list)
    assert len(subject) == 1

    population = subject[0]
    assert isinstance(population, tuple)
    assert len(population) == 100
    assert all((isinstance(i, str) for i in population))
