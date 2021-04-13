# Local Module
from ga.config import GAconfig
from ga.main import genetic_algorithm


def ga_testing(config: GAconfig, file_logger):
    populations, fitnesses = genetic_algorithm(config)
    last_pop, last_fitness = populations[-1], fitnesses[-1]
    max_fitness = max(last_fitness)
    max_idx = last_fitness.index(max_fitness)
    strongest_individual = last_pop[max_idx]
    strongest_phenotype = config.setting.gene_operator.decode(
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
    return populations, fitnesses
