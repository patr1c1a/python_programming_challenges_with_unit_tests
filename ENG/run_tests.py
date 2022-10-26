import unittest
from tests import tests_numbers
from tests import tests_strings
from tests import tests_lists
from tests import tests_dictionaries

suite = unittest.TestSuite()
loader = unittest.TestLoader()

# Comment out lines related to topics that will be excluded from execution.
suite.addTests(loader.loadTestsFromModule(tests_numbers))
suite.addTests(loader.loadTestsFromModule(tests_strings))
suite.addTests(loader.loadTestsFromModule(tests_lists))
suite.addTests(loader.loadTestsFromModule(tests_dictionaries))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
