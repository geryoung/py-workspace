import unittest
import os

def load_tests(loader):
    case_path = os.path.dirname(__file__)
    package_tests = loader.discover("tests")
    return package_tests


if __name__ == "__main__":
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(load_tests(unittest.defaultTestLoader))
