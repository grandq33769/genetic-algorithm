# Local Module
from ga.initialization.basic import basic_init, init_by_neighbors


def test_basic_init(ga_setting):
    subject = basic_init(ga_setting)
    assert isinstance(subject, list)
    assert len(subject) == 1

    population = subject[0]
    assert isinstance(population, tuple)
    assert len(population) == 100
    assert all((isinstance(i, str) for i in population))


def test_init_by_neighbors(ga_setting):
    subject = init_by_neighbors(ga_setting)
    assert isinstance(subject, list)
    assert len(subject) == 1

    population = subject[0]
    assert isinstance(population, tuple)
    assert len(population) == 100
    assert all((isinstance(i, str) for i in population))
