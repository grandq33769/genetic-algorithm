# Third Party Library
from loguru import logger as log

# Local Module
from ga.evaluation.basic import basic_evaluation, hc_evaluation
from ga.initialization.basic import basic_init
from ga.main import obj_func


def test_basic_evaluation(ga_setting, file_logger):
    population = basic_init(ga_setting)[0]
    subject = basic_evaluation(population, ga_setting, obj_func)
    file_logger.debug(subject)

    assert isinstance(subject, tuple)
    assert len(subject) == ga_setting.pop_size
    assert all((isinstance(i, float) for i in subject))


def test_hc_evaluation(hc_setting):
    population = basic_init(hc_setting)[0]
    subject = hc_evaluation(population, hc_setting, obj_func)

    assert isinstance(subject, tuple)
    assert len(subject) == hc_setting.pop_size
    assert all((isinstance(i, float) for i in subject))

    assert isinstance(hc_setting.target_fitness, float)
