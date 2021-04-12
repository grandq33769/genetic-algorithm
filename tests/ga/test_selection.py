# Local Module
from ga.selection.roulette import float_to_range_idx, roulette


def test_float_to_range_idx():
    target = 0.3
    ranges = (0.001, 0.1, 0.2, 0.3, 0.4, 0.5, 1)
    subject = float_to_range_idx(target, ranges)

    assert subject == 3


def test_roulette(ga_setting):
    population = (3, 8, 9, 20, 1, 5)
    fitness = (0.3, 0, -0.1, 0.15, 0.9, 1)

    subjects = [roulette(population, fitness, ga_setting) for _ in range(100)]

    type_result = [isinstance(p, list) for p in subjects]
    result = [9 not in p for p in subjects]

    assert all(type_result)
    assert all(result)
