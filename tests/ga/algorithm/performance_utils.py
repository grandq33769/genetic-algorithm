# Standard Library
from datetime import datetime
from os import listdir
from os.path import isfile, join
from pathlib import Path
from time import time
from typing import List, Tuple

# Local Module
from ga.config import GAconfig
from ga.main import genetic_algorithm
from ga.representation.base import GeneOperator


def ga_testing(
    config: GAconfig, file_logger, func_name: str, need_record=True
):
    start = time()
    populations, fitnesses = genetic_algorithm(config)
    end = time()
    now = datetime.now().strftime('%Y-%m-%dT%H:%M:%S')
    execution_sec = end - start

    last_pop, last_fitness = populations[-1], fitnesses[-1]
    max_fitness = max(last_fitness)
    max_idx = last_fitness.index(max_fitness)
    strongest_individual = last_pop[max_idx]
    strongest_phenotype = config.setting.gene_operator.decode(
        strongest_individual
    )
    aggregated_metric: Tuple = (
        now,
        execution_sec,
        strongest_individual,
        *strongest_phenotype,
        max_fitness,
    )
    metric: Tuple = tuple(str(i) for i in aggregated_metric)

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
    if need_record:
        write_metric(func_name, metric, populations, fitnesses, config)

    return populations, fitnesses


def write_metric(
    func_name: str,
    metric: Tuple,
    populations: List,
    fitnesses: List,
    config: GAconfig,
):
    operator: GeneOperator = config.setting.gene_operator
    pop_path = f'./performance/{func_name}/populations'
    fitness_path = f'./performance/{func_name}/fitnesses'
    Path(pop_path).mkdir(parents=True, exist_ok=True)
    Path(fitness_path).mkdir(parents=True, exist_ok=True)

    pop_filename = [f for f in listdir(pop_path) if isfile(join(pop_path, f))]
    fitness_filename = [
        f for f in listdir(fitness_path) if isfile(join(fitness_path, f))
    ]

    if pop_filename == []:
        pop_filename = ['0.csv']

    if fitness_filename == []:
        fitness_filename = ['0.csv']

    max_name: str = max([max(pop_filename), max(fitness_filename)]).replace(
        '.csv', ''
    )
    now_idx = int(max_name) + 1

    with open(f'./performance/{func_name}/metric.csv', 'a') as wf:
        wf.write(','.join(metric))
        wf.write('\n')

    with open(f'{pop_path}/{now_idx}.csv', 'w') as wf:
        for p in populations:
            individuals = [operator.format(i) for i in p]
            line = ','.join(individuals)
            wf.write(line)
            wf.write('\n')

    with open(f'{fitness_path}/{now_idx}.csv', 'w') as wf:
        for f in fitnesses:
            line = ','.join(str(i) for i in f)
            wf.write(line)
            wf.write('\n')
