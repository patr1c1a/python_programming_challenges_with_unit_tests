#######################################################
# NO MODIFICAR ESTE ARCHIVO A MENOS QUE SEA NECESARIO #
#######################################################

import unittest
import tests.tests_numeros
import tests.tests_strings
import tests.tests_listas
import tests.tests_diccionarios


loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Comentar las líneas correspondiente a las áreas temáticas a excluir durante la ejecución.
suite.addTests(loader.loadTestsFromModule(tests.tests_numeros))
suite.addTests(loader.loadTestsFromModule(tests.tests_strings))
suite.addTests(loader.loadTestsFromModule(tests.tests_listas))
suite.addTests(loader.loadTestsFromModule(tests.tests_diccionarios))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
