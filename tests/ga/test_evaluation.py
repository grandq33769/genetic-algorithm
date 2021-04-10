# Local Module
from ga.main import basic_evaluation, basic_init


def test_basic_evaluation(ga_setting):
    population = basic_init(ga_setting)[0]
    subject = basic_evaluation(population, ga_setting)

    assert isinstance(subject, tuple)
    assert len(subject) == 100
    assert all((isinstance(i, float) for i in subject))
