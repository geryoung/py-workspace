import unittest
import os

def load_tests(loader, pattern="test*.py"):
    # top level directory cached on loader instance
    this_dir = os.path.dirname(__file__)
    package_tests = loader.discover(start_dir=this_dir, pattern=pattern)
    return package_tests
    # standard_tests.addTests(package_tests)
    # return standard_tests


if __name__ == "__main__":
    runner = unittest.TextTestRunner()
    runner.run(load_tests(unittest.defaultTestLoader))
