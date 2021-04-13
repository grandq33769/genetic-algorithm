# Local Module
from ga.initialization.basic import basic_init, init_by_neighbors


def test_basic_init(ga_setting):
    subject = basic_init(ga_setting)
    assert isinstance(subject, list)
    assert len(subject) == 1

    population = subject[0]
    assert isinstance(population, tuple)
    assert len(population) == ga_setting.pop_size
    assert all((isinstance(i, str) for i in population))


def test_init_by_neighbors(hc_setting):
    operator = hc_setting.gene_operator
    subject = init_by_neighbors(hc_setting)
    assert isinstance(subject, list)
    assert len(subject) == 1

    population = subject[0]
    assert isinstance(population, tuple)
    assert len(population) == hc_setting.pop_size
    assert all((isinstance(i, str) for i in population))

    assert len(hc_setting.target) == operator.length
