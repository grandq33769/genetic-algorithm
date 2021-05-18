# Third Party Library
from loguru import logger as log

# Local Module
from ga.evaluation.basic import basic_evaluation, hc_evaluation
from ga.evaluation.niching import niching_evaluation
from ga.initialization.basic import basic_init, init_by_neighbors
from ga.main import obj_func
from ga.objective.hw2 import obj_func_q1


def test_basic_evaluation(ga_setting, file_logger):
    population = basic_init(ga_setting)[0]
    subject = basic_evaluation(population, ga_setting, obj_func)
    file_logger.debug(subject)

    assert isinstance(subject, tuple)
    assert len(subject) == ga_setting.pop_size
    assert all((isinstance(i, float) for i in subject))


def test_hc_evaluation(hc_setting):
    population = init_by_neighbors(hc_setting)[0]
    subject = hc_evaluation(population, hc_setting, obj_func)

    assert isinstance(subject, tuple)
    assert len(subject) == hc_setting.pop_size
    assert all((isinstance(i, float) for i in subject))
    assert isinstance(hc_setting.target_fitness, float)


def test_niching_evaluation(niching_float_setting, file_logger):
    population = basic_init(niching_float_setting)[0]
    subject = niching_evaluation(
        population, niching_float_setting, obj_func_q1
    )
    file_logger.debug(subject)

    assert isinstance(subject, tuple)
    assert len(subject) == niching_float_setting.pop_size
    assert all((isinstance(i, float) for i in subject))
