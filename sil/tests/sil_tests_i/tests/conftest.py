import pytest
from devsure.time_simulator import SimulatedTimeScope, time_runner
from tests.Core.context.context import Context

pytest_plugins = ["devsure.fixtures.conftest"]

@pytest.fixture(scope="function")
def context():
    time_runner.reset_to_initial_state()
    with SimulatedTimeScope("test"):
        yield Context()
