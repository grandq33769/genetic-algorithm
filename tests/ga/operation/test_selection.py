# Standard Library
from operator import sub

# Third Party Library
from numpy import mean

# Local Module
from ga.selection.neighbor import select_neighbor_from_target
from ga.selection.roulette import float_to_range_idx, roulette


def test_float_to_range_idx():
    target = 0.3
    ranges = (0.001, 0.1, 0.2, 0.3, 0.4, 0.5, 1)
    subject = float_to_range_idx(target, ranges)

    assert subject == 3


def test_roulette(ga_setting, file_logger):
    population = (3, 8, 9, 20, 1, 5)
    fitness = (0.3, 0, -0.1, 0.15, 0.9, 1)

    subjects = [roulette(population, fitness, ga_setting) for _ in range(100)]
    file_logger.debug(subjects)

    type_result = [isinstance(p, list) for p in subjects]
    result = [isinstance(mean(p), float) for p in subjects]

    assert all(type_result)
    assert all(result)


def test_select_neighbor_from_target(hc_setting, file_logger):
    hc_setting.target = '0000000000000100000000000010'
    population = (
        '0000000000000100001111111010',
        '0000000111100100000000000010',
        '0000000000101000000000000010',
        '0000000000000100000000011110',
        '0000000111000100000000000010',
        '0000000001010100000000000010',
    )
    fitness = (0.3, 0, -0.1, 0.15, 0.9, 1)
    subject = select_neighbor_from_target(population, fitness, hc_setting)
    file_logger.info(f'{subject=}')

    individual_type_check = [isinstance(p, str) for p in subject]

    assert isinstance(subject, list)
    assert all(individual_type_check)
