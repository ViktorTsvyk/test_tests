import pytest
from tests.Core.context.context import Context

pytest_plugins = ["devsure.fixtures.conftest"]

from tests.steps import *

@pytest.fixture(scope="function")
def context():
    return Context()
