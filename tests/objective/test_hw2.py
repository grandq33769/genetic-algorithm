# Third Party Library
import pytest

# Local Module
from ga.objective.hw2 import obj_func_q1


def test_obj_func_success():
    obj_func_q1(0.1, 0.4)


def test_obj_func_fail():
    with pytest.raises(AssertionError):
        obj_func_q1('a', 'string')


def test_obj_func_fail_out_of_range():
    with pytest.raises(AssertionError):
        obj_func_q1(-2.3, 2.3)
