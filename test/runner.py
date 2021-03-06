"""
Created on Jan 7, 2017

@author: meike.zehlike
"""
# tests/runner.py
import unittest

# initialize the test suite
loader = unittest.TestLoader()
suite = unittest.TestSuite()

# add tests to the test suite
suite.addTests(loader.discover('.', pattern="Test*.py"))

# initialize a runner, pass it your suite and run it
runner = unittest.TextTestRunner(verbosity=3)
result = runner.run(suite)
