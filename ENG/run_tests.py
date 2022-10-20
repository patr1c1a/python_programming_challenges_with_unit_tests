#########################################
# DO NOT MODIFY THIS FILE UNLESS NEEDED #
#########################################

import unittest
import tests.tests_numbers as numbers
import tests.tests_strings as strings
import tests.tests_lists as lists
import tests.tests_dictionaries as dictionaries

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Comment out the lines related to topics you'd like to exclude from execution.
suite.addTests(loader.loadTestsFromModule(numbers))
suite.addTests(loader.loadTestsFromModule(strings))
suite.addTests(loader.loadTestsFromModule(lists))
suite.addTests(loader.loadTestsFromModule(dictionaries))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
