""" This is a file that ensures that project directory is added to the PYTHONPATH and
all fixtures declared under "devsure/fixtures/" will be found by pytest.
Make sure to include this file in the parent directory containing tests.

"""

pytest_plugins = ["devsure.fixtures.conftest"]  # point to the directory with pytest fixtures
