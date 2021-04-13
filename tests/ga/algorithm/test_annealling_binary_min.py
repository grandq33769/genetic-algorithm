# Local Module
from ga.config import SAconfig
from ga.crossover.binary import no_ops as crossover_no_ops
from ga.evaluation.basic import annealling
from ga.initialization.basic import init_by_neighbors
from ga.main import obj_func
from ga.mutation.binary import no_ops as mutation_no_ops
from ga.selection.neighbor import select_neighbor_from_target
from ga.termination.basic import is_annealled

from .performance_utils import ga_testing


def test_ga_binary_min(sa_setting, file_logger):
    is_terminated = lambda *args: is_annealled(
        *args, terminated_gen=5000, duplicated_time=5
    )
    evaluation = lambda *args: annealling(
        *args, obj_func=lambda *x: -obj_func(*x)
    )
    config = SAconfig(
        sa_setting,
        init_by_neighbors,
        evaluation,
        select_neighbor_from_target,
        is_terminated,
        crossover_no_ops,
        mutation_no_ops,
    )

    populations, fitnesses = ga_testing(config, file_logger)
    file_logger.info(
        ' '.join([f'{sa_setting.target=}', f'{sa_setting.target_fitness=}'])
    )

    assert isinstance(populations, list)
    assert isinstance(fitnesses, list)
