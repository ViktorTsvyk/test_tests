""" This is a file that ensures that project directory is added to the PYTHONPATH and
all fixtures declared under "devsure/fixtures/" will be found by pytest.
Make sure to include this file in the parent directory containing tests.

"""
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