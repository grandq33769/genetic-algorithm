# Local Module
from ga.config import SAconfig
from ga.crossover.binary import no_ops as crossover_no_ops
from ga.evaluation.basic import basic_evaluation
from ga.initialization.basic import init_by_neighbors
from ga.mutation.binary import no_ops as mutation_no_ops
from ga.selection.neighbor import select_neighbor_from_target
from ga.termination.basic import is_annealled

from .performance_utils import ga_testing


def test_ga_binary(sa_setting, file_logger):
    is_terminated = lambda *args: is_annealled(
        *args, terminated_gen=1000, duplicated_time=5
    )
    config = SAconfig(
        sa_setting,
        init_by_neighbors,
        basic_evaluation,
        select_neighbor_from_target,
        is_terminated,
        crossover_no_ops,
        mutation_no_ops,
    )

    populations, fitnesses = ga_testing(config, file_logger)

    assert isinstance(populations, list)
    assert isinstance(fitnesses, list)
