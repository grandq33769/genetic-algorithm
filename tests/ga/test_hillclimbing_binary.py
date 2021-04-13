# Local Module
from ga.config import HillClimbingConfig
from ga.crossover.binary import no_ops as crossover_no_ops
from ga.evaluation.basic import hc_evaluation
from ga.initialization.basic import init_by_neighbors
from ga.main import genetic_algorithm
from ga.mutation.binary import no_ops as mutation_no_ops
from ga.selection.neighbor import select_neighbor_from_target
from ga.termination.basic import is_strongest_diff_from_previous

from .performance_utils import ga_testing


def test_ga_binary(hc_setting, file_logger):
    config = HillClimbingConfig(
        hc_setting,
        init_by_neighbors,
        hc_evaluation,
        select_neighbor_from_target,
        is_strongest_diff_from_previous,
        crossover_no_ops,
        mutation_no_ops,
    )
    populations, fitnesses = ga_testing(config, file_logger)
    assert isinstance(populations, list)
    assert isinstance(fitnesses, list)
