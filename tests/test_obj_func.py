# Third Party Library
import pytest

# Local Module
from ga.main import cal_term_1, cal_term_2, obj_func


def test_obj_func_success():
    obj_func(0.1, 0.4)


def test_obj_func_fail():
    with pytest.raises(AssertionError):
        obj_func('a', 'string')


def test_obj_func_fail_out_of_range():
    with pytest.raises(AssertionError):
        obj_func(4.1, -0.8)


def test_cal_term_1():
    assert cal_term_1(0.1345, 0.4555) == 0.6891608144070406


def test_cal_term_2():
    assert cal_term_2(0.1345, 0.4555) == 1.6136606806223517
