# Local Module
from ga.termination.basic import (
    is_annealled,
    is_terminated_by_generation,
    smaller_than_previous,
)


def test_is_terminated_by_generation(ga_setting):
    generation = 2
    populations = [('010'), ('110')]
    fitnesses = [(20), (30)]
    setting = ga_setting
    input_args = (generation, populations, fitnesses, setting)

    test_success_subject = lambda *args: is_terminated_by_generation(
        *args, terminated_gen=1
    )
    test_fail_subject = lambda *args: is_terminated_by_generation(
        *args, terminated_gen=3
    )

    assert test_success_subject(*input_args) == True
    assert test_fail_subject(*input_args) == False


def test_smaller_than_previous(hc_setting):
    generation = 1
    populations = [('010', '001'), ('110', '100')]
    fitnesses_success = [(20, 10), (30, 5)]
    fitnesses_fail = [(10, 10), (8, 5)]
    hc_setting.target_fitness = 15

    success_args = (generation, populations, fitnesses_success, hc_setting)
    fail_args = (generation, populations, fitnesses_fail, hc_setting)

    assert smaller_than_previous(*success_args) == False
    assert hc_setting.target_fitness == 30
    assert smaller_than_previous(*fail_args) == True
    assert hc_setting.target_fitness == 30


def test_is_annealled(sa_setting):
    generation = 3
    populations = [('010',), ('100',), ('000',), ('101',)]
    fitnesses = [(10,), (10,), (10,), (10,)]
    setting = sa_setting
    input_args = (generation, populations, fitnesses, setting)

    test_exceeded = lambda *args: is_annealled(
        *args, terminated_gen=1, duplicated_time=10
    )

    test_not_exceeded = lambda *args: is_annealled(
        *args, terminated_gen=5, duplicated_time=10
    )

    test_annealled = lambda *args: is_annealled(
        *args, terminated_gen=5, duplicated_time=3
    )

    test_both = lambda *args: is_annealled(
        *args, terminated_gen=1, duplicated_time=3
    )

    assert test_exceeded(*input_args) == True
    assert test_not_exceeded(*input_args) == False
    assert test_annealled(*input_args) == True
    assert test_both(*input_args) == True
