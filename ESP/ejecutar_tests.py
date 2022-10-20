#######################################################
# NO MODIFICAR ESTE ARCHIVO A MENOS QUE SEA NECESARIO #
#######################################################

import unittest
from tests import tests_numeros
from tests import tests_strings
from tests import tests_listas
from tests import tests_diccionarios

loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Comentar las líneas correspondiente a las áreas temáticas a excluir durante la ejecución.
suite.addTests(loader.loadTestsFromModule(tests_numeros))
suite.addTests(loader.loadTestsFromModule(tests_strings))
suite.addTests(loader.loadTestsFromModule(tests_listas))
suite.addTests(loader.loadTestsFromModule(tests_diccionarios))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
