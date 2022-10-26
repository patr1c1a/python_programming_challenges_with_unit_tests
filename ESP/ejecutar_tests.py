import unittest
from tests import tests_numeros
from tests import tests_strings
from tests import tests_listas
from tests import tests_diccionarios

suite = unittest.TestSuite()
loader = unittest.TestLoader()

# Comentar las líneas relacionadas a los temas que se excluirán de la ejecución.
suite.addTests(loader.loadTestsFromModule(tests_numeros))
suite.addTests(loader.loadTestsFromModule(tests_strings))
suite.addTests(loader.loadTestsFromModule(tests_listas))
suite.addTests(loader.loadTestsFromModule(tests_diccionarios))

runner = unittest.TextTestRunner(verbosity=2)
result = runner.run(suite)
