# Local Module
from ga.main import basic_init
from ga.mutation.binary import one_bit_mutation


def test_one_bit_mutation(ga_setting, file_logger):
    population = list(basic_init(ga_setting)[0])

    occurred = False
    while not occurred:
        subject, occurred = one_bit_mutation(population, ga_setting)
    file_logger.debug(subject)
    assert isinstance(subject, list)
    assert len(subject) == ga_setting.pop_size
