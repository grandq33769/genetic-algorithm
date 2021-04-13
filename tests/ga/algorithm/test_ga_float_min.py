# Local Module
from ga.config import GAconfig
from ga.crossover.binary import one_bit_crossover
from ga.evaluation.basic import basic_evaluation
from ga.initialization.basic import basic_init
from ga.main import obj_func
from ga.mutation.binary import one_bit_mutation
from ga.selection.roulette import roulette
from ga.termination.basic import is_terminated_by_generation

from .performance_utils import ga_testing


def test_ga_float_min(ga_float_setting, file_logger):
    is_terminated = lambda *args: is_terminated_by_generation(
        *args, terminated_gen=100
    )
    evaluation = lambda *args: basic_evaluation(
        *args, obj_func=lambda *x: -obj_func(*x)
    )
    config = GAconfig(
        ga_float_setting,
        basic_init,
        evaluation,
        roulette,
        is_terminated,
        one_bit_crossover,
        one_bit_mutation,
    )
    populations, fitnesses = ga_testing(
        config, file_logger, test_ga_float_min.__name__
    )

    assert isinstance(populations, list)
    assert isinstance(fitnesses, list)
