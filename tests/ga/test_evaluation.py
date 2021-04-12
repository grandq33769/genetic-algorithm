# Third Party Library
from loguru import logger as log

# Local Module
from ga.initialization.basic import basic_init
from ga.main import basic_evaluation


def test_basic_evaluation(ga_setting, file_logger):
    population = basic_init(ga_setting)[0]
    subject = basic_evaluation(population, ga_setting)
    file_logger.debug(subject)

    assert isinstance(subject, tuple)
    assert len(subject) == 100
    assert all((isinstance(i, float) for i in subject))
