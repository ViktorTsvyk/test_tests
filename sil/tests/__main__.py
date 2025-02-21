""" Test the devsure.rpc operation
Run all with
python -m devsure.rpc.test

Note1:  one can also use
            python -m unittest discover
        from the root folder to run all the tests in the project

Note2:  In PyCharm one can just right-click the file
        and choose "Run Python tests" or "Debug Python tests",
        to run/debug directly from IDE
"""

import unittest
from os import path

if __name__ == '__main__':
    my_dir_path = path.dirname(path.realpath(__file__))
    top_level_dir = path.normpath(
        path.join(path.dirname(path.realpath(__file__)), "../../..")
    )

    print(f"Loading all tests from {my_dir_path}\n\n")
    testsuite = unittest.TestLoader().discover(my_dir_path, top_level_dir=top_level_dir)
    unittest.TextTestRunner(verbosity=2).run(testsuite)
