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


def test_max():
    assert obj_func(0.6887, 0.9866) == 2.1912616758946326


def test_min():
    assert obj_func(0.0001, 0.0002) == 0.015155696886441018
