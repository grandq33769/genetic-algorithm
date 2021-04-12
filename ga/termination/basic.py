# Standard Library
from typing import List, Tuple

# Third Party Library
from loguru import logger as log

# Local Module
from ga.config import GAsetting


def is_terminated_by_generation(
    generation: int,
    populations: List[Tuple],
    fitnesses: List[Tuple],
    setting: GAsetting,
    /,
    terminated_gen: int,
) -> bool:
    log.debug(
        ' '.join(
            [
                f'{generation=}',
                f'{len(populations)=}',
                f'{len(fitnesses)=}',
                f'{setting=}',
                f'{terminated_gen=}',
            ]
        )
    )
    return generation > terminated_gen
