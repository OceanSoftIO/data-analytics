import pytest
from loguru import logger
import logging

@pytest.fixture(autouse=True)
def loguru_caplog(caplog):
    """Redirect loguru logs to pytest's logging system."""
    class PropagateHandler(logging.Handler):
        def emit(self, record):
            logging.getLogger(record.name).handle(record)

    logger.remove()
    logger.add(PropagateHandler(), format="{message}")


@pytest.fixture(scope="module")
def config():
    """Fixture for loading default configuration."""
    return {
        "precision": 2,
        "allow_negative": True,
        "debug": False,
    }
