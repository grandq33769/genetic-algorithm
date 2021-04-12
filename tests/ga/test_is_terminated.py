# Local Module
from ga.termination.basic import is_terminated_by_generation


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
