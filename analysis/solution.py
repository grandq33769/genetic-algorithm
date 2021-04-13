# Third Party Library
import pandas as pd
from loguru import logger as log


def find_solution(title):
    df = pd.read_csv(f'./performance/test_{title}/metric.csv', header=None)
    log.debug(df)
    target_idx = df[4].idxmax()
    log.debug(f'{target_idx=}')
    log.debug(f'{df.loc[target_idx, ]=}')


if __name__ == '__main__':
    # find_solution('ga_float_max')
    find_solution('ga_float_min')
    # find_solution('ga_binary_max')
    # find_solution('hillclimbing_float_min')
