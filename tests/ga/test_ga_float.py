# Local Module
from ga.config import GAconfig
from ga.crossover.binary import one_bit_crossover
from ga.initialization.basic import basic_init
from ga.main import (
    basic_evaluation,
    genetic_algorithm,
    is_terminated_by_generation,
)
from ga.mutation.binary import one_bit_mutation
from ga.selection.roulette import roulette


def test_ga_binary(ga_float_setting, file_logger):
    is_terminated = lambda *args: is_terminated_by_generation(
        *args, terminated_gen=100
    )
    config = GAconfig(
        ga_float_setting,
        basic_init,
        basic_evaluation,
        roulette,
        is_terminated,
        one_bit_crossover,
        one_bit_mutation,
    )
    populations, fitnesses = genetic_algorithm(config)
    last_pop, last_fitness = populations[-1], fitnesses[-1]
    max_fitness = max(last_fitness)
    max_idx = last_fitness.index(max_fitness)
    strongest_individual = last_pop[max_idx]
    strongest_phenotype = ga_float_setting.gene_operator.decode(
        strongest_individual
    )
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
