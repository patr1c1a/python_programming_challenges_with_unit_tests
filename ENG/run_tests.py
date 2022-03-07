###########################
# DO NOT MODIFY THIS FILE #
###########################

import unittest
import tests.tests_numbers
import tests.tests_strings
import tests.tests_lists
import tests.tests_dictionaries

loader = unittest.TestLoader()
suite = unittest.TestSuite()
suite.addTests(loader.loadTestsFromModule(tests.tests_numbers))
suite.addTests(loader.loadTestsFromModule(tests.tests_strings))
suite.addTests(loader.loadTestsFromModule(tests.tests_lists))
suite.addTests(loader.loadTestsFromModule(tests.tests_dictionaries))
runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
