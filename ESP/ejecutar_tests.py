#######################################################
# NO MODIFICAR ESTE ARCHIVO A MENOS QUE SEA NECESARIO #
#######################################################

import unittest
import tests.tests_numeros as numeros
import tests.tests_strings as strings
import tests.tests_listas as listas
import tests.tests_diccionarios as diccionarios


loader = unittest.TestLoader()
suite = unittest.TestSuite()

# Comentar las líneas correspondiente a las áreas temáticas a excluir durante la ejecución.
suite.addTests(loader.loadTestsFromModule(numeros))
suite.addTests(loader.loadTestsFromModule(strings))
suite.addTests(loader.loadTestsFromModule(listas))
suite.addTests(loader.loadTestsFromModule(diccionarios))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
