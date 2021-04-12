# Local Module
from ga.crossover.binary import one_bit_crossover
from ga.initialization.basic import basic_init


def test_one_bit_crossover(ga_setting, file_logger):
    population = list(basic_init(ga_setting)[0])

    subject = one_bit_crossover(population, ga_setting)
    file_logger.debug(subject)
    assert isinstance(subject, list)
    assert len(subject) == ga_setting.pop_size
