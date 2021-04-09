# Standard Library
from datetime import datetime
from time import time

# Third Party Library
import pytest

# Local Module
from ga.main import brute_force


@pytest.mark.slow
def test_brute_force():

    start = time()
    max_v, min_v = brute_force()
    end = time()

    with open('./performance/brute_force.csv', 'a') as wf:
        wf.write(f'{datetime.now().isoformat()},{end-start}\n')

    assert isinstance(max_v, tuple)
    assert isinstance(min_v, tuple)
    # max (0.6887, 0.9866)
    assert max_v == ((0.6887, 0.9866), 2.1912616758946326)
    assert min_v == ((0.0001, 0.0002), 0.015155696886441018)
