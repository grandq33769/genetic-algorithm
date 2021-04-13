# Local Module
from ga.termination.basic import (
    is_strongest_diff_from_previous,
    is_terminated_by_generation,
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


def test_is_strongest_diff_from_previous(hc_setting):
    generation = 1
    populations = [('010', '001'), ('110', '100')]
    fitnesses_success = [(20, 10), (30, 5)]
    fitnesses_fail = [(10, 10), (8, 5)]
    hc_setting.target_fitness = 15

    success_args = (generation, populations, fitnesses_success, hc_setting)
    fail_args = (generation, populations, fitnesses_fail, hc_setting)

    assert is_strongest_diff_from_previous(*success_args) == True
    assert hc_setting.target_fitness == 30
    assert is_strongest_diff_from_previous(*fail_args) == False
    assert hc_setting.target_fitness == 30
