# Third Party Library
from loguru import logger as log

# Local Module
from ga.evaluation.basic import basic_evaluation, hc_evaluation
from ga.initialization.basic import basic_init


def test_basic_evaluation(ga_setting, file_logger):
    population = basic_init(ga_setting)[0]
    subject = basic_evaluation(population, ga_setting)
    file_logger.debug(subject)

    assert isinstance(subject, tuple)
    assert len(subject) == 100
    assert all((isinstance(i, float) for i in subject))


def test_hc_evaluation(hc_setting):
    population = basic_init(hc_setting)[0]
    subject = basic_evaluation(population, hc_setting)

    assert isinstance(subject, tuple)
    assert len(subject) == 100
    assert all((isinstance(i, float) for i in subject))

    assert isinstance(hc_setting.target_fitness, float)
