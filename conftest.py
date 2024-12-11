""" This is a file that ensures that project directory is added to the PYTHONPATH and
all fixtures declared under "devsure/fixtures/" will be found by pytest.
Make sure to include this file in the parent directory containing tests.

"""
import pytest
import logging
import sys
import os
from pathlib import Path

# ----------------------------------------------------------------------------------------------------------------------
# Please, set the "DEVSURE_DIR" environment variable to the full path of the "Devsure" project directory
# (e.g. "/home/user/Projects/devsure") or replace the default parameter with it

project_dir = os.getenv(key="DEVSURE_DIR", default=".")
# ----------------------------------------------------------------------------------------------------------------------

sys.path.insert(0, project_dir)  # add the project directory to the PYTHONPATH
sys.path.append(str(Path(__file__).parent))  # add the parent directory to the PYTHONPATH

pytest_plugins = ["devsure.fixtures.conftest"]  # point to the directory with pytest fixtures

def pytest_configure(config):
    # Create a timestamped directory
    logging.basicConfig(
        level=logging.DEBUG,  # Capture all log levels
        format="%(asctime)s [%(levelname)s] %(message)s",
        handlers=[
            logging.StreamHandler()  # Output to console
        ]
    )

def pytest_runtest_call(item):
    logging.info(f"----- {item.location[-1]} -----")
    logging.info(f"Test location: {item.location[0]}")

@pytest.fixture(autouse=True)
def capture_print_logs(request, capsys):
    """ Fixture to capture print statements and log them """
    yield
    captured = capsys.readouterr()
    if captured.out.strip():
        logging.info(captured.out.strip())
    if captured.err.strip():
        logging.warning(captured.err.strip())

@pytest.hookimpl()
def pytest_assertion_pass(item, lineno, orig, expl):
    """ Hook to log information when an assertion passes """
    logging.debug(f"Assertion Passed in Test: {item}")
    logging.debug(f"Assertion Code Line: {lineno}")
    logging.debug(f"Expected: {orig}")
    logging.debug(f"Actual: {expl}")
