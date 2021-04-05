# Standard Library
from math import sin

# Third Party Library
from loguru import logger as log


def obj_func(x1, x2):
    log.debug(f'{x1=} {x2=}')
    assert isinstance(x1, (int, float))
    assert isinstance(x2, (int, float))
    assert 0 <= x1 <= 1
    assert 0 <= x2 <= 1

    x1 = round(x1, 4)
    x2 = round(x2, 4)

    result = cal_term_1(x1, x2) * cal_term_2(x1, x2)

    log.debug(f'Objective {result=}')
    return result


def cal_term_1(x1, x2):
    return (x1 ** 2 + x2 ** 2) ** 0.25


def cal_term_2(x1, x2):
    def inner_term(x1, x2):
        return (x1 ** 2 + x2 ** 2) ** 0.1

    return sin(50 * inner_term(x1, x2)) ** 2 + 1


def main():
    obj_func(3, 4)


if __name__ == "__main__":
    main()
