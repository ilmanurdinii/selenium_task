import unittest
from unittest.suite import TestSuite
import Login, Register, Checkout

if __name__ == "__main__":
    # create test suite from classes
    suite = TestSuite()

    # call test
    tests = unittest.TestLoader()

    # add test to suite
    suite.addTest(tests.loadTestsFromModule(Login))
    suite.addTest(tests.loadTestsFromModule(Register))
    suite.addTest(tests.loadTestsFromModule(Checkout))

    # run the test suite
    runner = unittest.TextTestRunner()
    runner.run(suite)