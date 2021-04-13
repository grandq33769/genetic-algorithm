# Local Module
from ga.config import HillClimbingConfig
from ga.crossover.binary import no_ops as crossover_no_ops
from ga.evaluation.basic import hc_evaluation
from ga.initialization.basic import init_by_neighbors
from ga.main import genetic_algorithm
from ga.mutation.binary import no_ops as mutation_no_ops
from ga.selection.neighbor import select_neighbor_from_target
from ga.termination.basic import is_strongest_diff_from_previous


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
    populations, fitnesses = genetic_algorithm(config)
    last_pop, last_fitness = populations[-1], fitnesses[-1]
    max_fitness = max(last_fitness)
    max_idx = last_fitness.index(max_fitness)
    strongest_individual = last_pop[max_idx]
    strongest_phenotype = hc_setting.gene_operator.decode(strongest_individual)
    file_logger.info(
        ' '.join(
            [
                f'{last_pop=}',
                f'{last_fitness=}',
                f'{strongest_individual=}',
                f'{strongest_phenotype=}',
                f'{max_fitness=}',
                f'{max_idx=}',
            ]
        )
    )
    assert isinstance(populations, list)
    assert isinstance(fitnesses, list)
