# Local Module
from ga.config import HillClimbingConfig
from ga.crossover.binary import no_ops as crossover_no_ops
from ga.evaluation.basic import hc_evaluation
from ga.initialization.basic import init_by_neighbors
from ga.main import obj_func
from ga.mutation.binary import no_ops as mutation_no_ops
from ga.selection.neighbor import select_neighbor_from_target
from ga.termination.basic import is_terminated_by_generation

from .performance_utils import ga_testing


def test_hillclimbing_float_min(hc_setting_float, file_logger):
    is_terminated = lambda *args: is_terminated_by_generation(
        *args, terminated_gen=100
    )
    evaluation = lambda *args: hc_evaluation(
        *args, obj_func=lambda *x: -obj_func(*x)
    )
    selection = lambda *args: select_neighbor_from_target(
        *args, obj_func=lambda *x: -obj_func(*x)
    )
    config = HillClimbingConfig(
        hc_setting_float,
        init_by_neighbors,
        evaluation,
        selection,
        is_terminated,
        crossover_no_ops,
        mutation_no_ops,
    )
    populations, fitnesses = ga_testing(
        config, file_logger, test_hillclimbing_float_min.__name__
    )
    assert isinstance(populations, list)
    assert isinstance(fitnesses, list)
