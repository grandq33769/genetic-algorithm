# Local Module
from ga.main import brute_force


def test_brute_force():
    max_v, min_v = brute_force()
    assert isinstance(max_v, tuple)
    assert isinstance(min_v, tuple)
    assert max_v == ((1, 1), 3)
    assert min_v == ((1, 1), 3)
