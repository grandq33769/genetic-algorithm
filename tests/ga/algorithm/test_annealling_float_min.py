# Local Module
from ga.config import SAconfig
from ga.crossover.binary import no_ops as crossover_no_ops
from ga.evaluation.basic import basic_evaluation
from ga.initialization.basic import annealling_init
from ga.main import obj_func
from ga.mutation.binary import no_ops as mutation_no_ops
from ga.selection.annealling import annealling
from ga.termination.basic import is_annealled

from .performance_utils import ga_testing


def test_annealling_float_min(sa_setting_float, file_logger):
    is_terminated = lambda *args: is_annealled(
        *args, terminated_gen=10000, duplicated_time=5
    )
    evaluation = lambda *args: basic_evaluation(
        *args, obj_func=lambda *x: -obj_func(*x)
    )
    selection = lambda *args: annealling(
        *args, obj_func=lambda *x: -obj_func(*x)
    )
    config = SAconfig(
        sa_setting_float,
        annealling_init,
        evaluation,
        selection,
        is_terminated,
        crossover_no_ops,
        mutation_no_ops,
    )

    populations, fitnesses = ga_testing(
        config, file_logger, test_annealling_float_min.__name__
    )
    file_logger.info(
        ' '.join(
            [
                f'{sa_setting_float.target=}',
                f'{sa_setting_float.target_fitness=}',
            ]
        )
    )

    assert isinstance(populations, list)
    assert isinstance(fitnesses, list)
