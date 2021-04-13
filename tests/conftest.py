# content of conftest.py

# Standard Library
import os
from datetime import datetime

# Third Party Library
import pytest
from loguru import logger


def pytest_addoption(parser):
    parser.addoption(
        "--runslow", action="store_true", default=False, help="run slow tests"
    )


def pytest_configure(config):
    config.addinivalue_line("markers", "slow: mark test as slow to run")


def pytest_collection_modifyitems(config, items):
    if config.getoption("--runslow"):
        # --runslow given in cli: do not skip slow tests
        return
    skip_slow = pytest.mark.skip(reason="need --runslow option to run")
    for item in items:
        if "slow" in item.keywords:
            item.add_marker(skip_slow)


@pytest.fixture
def file_logger(request):
    filename = os.path.basename(request.node.fspath).replace('.py', '')
    now_time = datetime.now().strftime('%Y-%m-%dT%H-%M-%S')
    handler_id = logger.add(
        f'logs/{filename}/{now_time}.log',
        # filter=lambda r: r["extra"]["task"] == filename,
    )
    yield logger
    logger.remove(handler_id)
