#############################
# NO MODIFICAR ESTE ARCHIVO #
#############################

import unittest
from ESP.src.listas import *


class TestsFuncionesListas(unittest.TestCase):

    def test_productoria_numeros(self):
        pruebas = {
            'Argumento usado: [1, 2, 3, 4]': [
                productoria_numeros([1, 2, 3, 4]),
                24
            ],
            'Argumento usado: [0, 3, 7, 9]': [
                productoria_numeros([0, 3, 7, 9]),
                0
            ],
            'Argumento usado: []': [
                productoria_numeros([]),
                None
            ],
            'Argumento usado: [1, 1, 1]': [
                productoria_numeros([1, 1, 1]),
                1
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_mayor_elemento(self):
        pruebas = {
            'Argumento usado: ["x", "y", "z"]': [
                mayor_elemento(["x", "y", "z"]),
                "z"
            ],
            'Argumento usado: ["z", "y", "x"]': [
                mayor_elemento(["z", "y", "z"]),
                "z"
            ],
            'Argumento usado: ["abc", "cba", "cab", "bca"]': [
                mayor_elemento(["abc", "cba", "cab", "bca"]),
                "cba"
            ],
            'Argumento usado: ["abc", "abc", "abc"]': [
                mayor_elemento(["abc", "abc", "abc"]),
                "abc"
            ],
            'Argumento usado: []': [
                mayor_elemento([]),
                None
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_mayor_ganancia(self):
        pruebas = {
            'Argumento usado: [70, 53, 15, 23, 41, 30]': [
                mayor_ganancia([70, 53, 15, 23, 41, 30]),
                55
            ],
            'Argumento usado: [5, 5, 5, 5, 5]': [
                mayor_ganancia([5, 5, 5, 5, 5]),
                0
            ],
            'Argumento usado: [15.6, 12.8, 4, 2.5, 19]': [
                mayor_ganancia([15.6, 12.8, 4, 2.5, 19]),
                16.5
            ],
            'Argumento usado: [12, 21]': [
                mayor_ganancia([12, 21]),
                9
            ],
            'Argumento usado: [21, 12]': [
                mayor_ganancia([21, 12]),
                9
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_elementos_unicos(self):
        pruebas = {
            'Argumento usado: [3, False, "a", 1, 1, 2, 2, False, 4]': [
                elementos_unicos([3, False, "a", 1, 1, 2, 4, False, 4]),
                [3, "a", 2]
            ],
            'Argumento usado: [1, 1, 1]': [
                elementos_unicos([1, 1, 1]),
                []
            ],
            'Argumento usado: ["hola", True, 5.1]': [
                elementos_unicos(["hola", True, 5.1]),
                ["hola", True, 5.1]
            ],
            'Argumento usado: []':
                [elementos_unicos([]),
                 []
                 ],
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_porcentaje_pares_impares(self):
        pruebas = {
            'Argumento usado: [-5, 3, 2, -4, 7]': [
                porcentaje_pares_impares([-5, 3, 2, -4, 7]),
                (40.0, 60.0)
            ],
            'Argumento usado: [1, 1, 1, 1]': [
                porcentaje_pares_impares([1, 1, 1, 1]),
                (0.0, 100.0)
            ],
            'Argumento usado: [1, 5]': [
                porcentaje_pares_impares([1, 5]),
                (0.0, 100.0)
            ],
            'Argumento usado: [2, 4]': [
                porcentaje_pares_impares([2, 4]),
                (100.0, 0.0)
            ],
            'Argumento usado: [1, 2, 3, 4]': [
                porcentaje_pares_impares([1, 2, 3, 4]),
                (50.0, 50.0)
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_sumar_indice(self):
        pruebas = {
            'Argumento usado: [1, 2, 3, 4, 5, 6]': [
                sumar_indice([1, 2, 3, 4, 5, 6]),
                [1, 3, 5, 7, 9, 11]
            ],
            'Argumento usado: [0, 0, 0]': [
                sumar_indice([0, 0, 0]),
                [0, 1, 2]
            ],
            'Argumento usado: []': [
                sumar_indice([]),
                []
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_sumas_parciales(self):
        pruebas = {
            'Argumento usado: [4, 6, 10, 7]': [
                sumas_parciales([4, 6, 10, 7]),
                [4, 10, 20, 27]
            ],
            'Argumento usado: [1, 1, 1, 1, 1]': [
                sumas_parciales([1, 1, 1, 1, 1]),
                [1, 2, 3, 4, 5]
            ],
            'Argumento usado: [1, 2, 3, 4]': [
                sumas_parciales([1, 2, 3, 4]),
                [1, 3, 6, 10]
            ],
            'Argumento usado: []': [
                sumas_parciales([]),
                []
            ],
            'Argumento usado: [5, 0, 0, 0, 0]': [
                sumas_parciales([5, 0, 0, 0, 0]),
                [5, 5, 5, 5, 5]
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_numeros_faltantes(self):
        pruebas = {
            'Argumento usado: [5, 0, 2, 9, 8, 12, 9]': [
                numeros_faltantes([5, 0, 2, 9, 8, 12, 9]),
                [1, 3, 4, 6]
            ],
            'Argumento usado: [3, 7, 15, 3, 9]': [
                numeros_faltantes([3, 7, 15, 3, 9]),
                [0, 1, 2, 4]
            ],
            'Argumento usado: [1, 2, 3, 4]': [
                numeros_faltantes([1, 2, 3, 4]),
                [0]
            ],
            'Argumento usado: [0, 1, 2, 3]': [
                numeros_faltantes([0, 1, 2, 3]),
                []
            ],
            'Argumento usado: [5]': [
                numeros_faltantes([5]),
                [0]
            ],
            'Argumento usado: []': [
                numeros_faltantes([]),
                []
            ],
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_cuantos_numeros_menores(self):
        pruebas = {
            'Argumento usado: [6, 3, 3, 4, 2]': [
                cuantos_numeros_menores([6, 3, 3, 4, 2]),
                [4, 1, 1, 3, 0]
            ],
            'Argumento usado: [3, 3, 3, 3]': [
                cuantos_numeros_menores([3, 3, 3, 3]),
                [0, 0, 0, 0]
            ],
            'Argumento usado: []': [
                cuantos_numeros_menores([]),
                []
            ],
            'Argumento usado: [1]': [
                cuantos_numeros_menores([1]),
                [0]
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_dos_maximos(self):
        pruebas = {
            'Argumento usado: [5, 3, 6, 2, 8]': [
                dos_maximos([5, 3, 6, 2, 8]),
                (8, 6)
            ],
            'Argumento usado: [6, 8, 3, 5, 2]': [
                dos_maximos([6, 8, 3, 5, 2]),
                (8, 6)
            ],
            'Argumento usado: [5, 3, 2, 8, 6]': [
                dos_maximos([5, 3, 2, 8, 6]),
                (8, 6)
            ],
            'Argumento usado: [5, 5, 5, 5]': [
                dos_maximos([5, 5, 5, 5]),
                (5, 5)
            ],
            'Argumento usado: [1.3, -4, 2.5, 7, -2.2]': [
                dos_maximos([1.3, -4, 2.5, 7, -2.2]),
                (7, 2.5)
            ],
            'Argumento usado: [1, 2]': [
                dos_maximos([1, 2]),
                (2, 1)
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_jugada_uno(self):
        pruebas = {
            'Argumentos usados: ["rojo 2", "azul 5", "verde 1"], "rojo 3': [
                jugada_uno(["rojo 2", "azul 5", "verde 1"], "rojo 3"),
                True
            ],
            'Argumentos usados: ["rojo 2", "azul 5", "verde 1"], "amarillo 3': [
                jugada_uno(["rojo 2", "azul 5", "verde 1"], "amarillo 3"),
                False
            ],
            'Argumentos usados: ["verde 4"], "amarillo 4': [
                jugada_uno(["verde 4"], "amarillo 4"),
                True
            ],
            'Argumentos usados: ["verde 1"], "verde 6': [
                jugada_uno(["verde 1"], "verde 6"),
                True
            ],
            'Argumentos usados: ["verde 1"], "azul 5"': [
                jugada_uno(["verde 1"], "azul 5"),
                False
            ],
            'Argumentos usados: [], "azul 5"': [
                jugada_uno([], "azul 5"),
                False
            ],
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_eliminar_ocurrencias_extra(self):
        pruebas = {
            'Argumentos usados: [1, 2, 3, 2, 3, 3], 1': [
                descartar_ocurrencias_extra([1, 2, 3, 2, 3, 3], 1),
                [1, 2, 3]
            ],
            'Argumentos usados: [1, 2, 3, 2, 3, 3], 3': [
                descartar_ocurrencias_extra([1, 2, 3, 2, 3, 3], 3),
                [1, 2, 3, 2, 3, 3]
            ],
            'Argumentos usados: [7, 4, 5, 4, 4, 7, 8, 4, 5], 2': [
                descartar_ocurrencias_extra([7, 4, 5, 4, 4, 7, 8, 4, 5], 2),
                [7, 4, 5, 4, 7, 8, 5]
            ],
            'Argumentos usados: [1, 1, 1, 1, 1, 1], 0': [
                descartar_ocurrencias_extra([1, 1, 1, 1, 1, 1], 0),
                []
            ],
            'Argumentos usados: ["a", "a", "a"], 1': [
                descartar_ocurrencias_extra(["a", "a", "a"], 1),
                ["a"]
            ],
            'Argumentos usados: [], 1': [
                descartar_ocurrencias_extra([], 1),
                []
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_es_desplazamiento(self):
        pruebas = {
            'Argumentos usados: [1, 2, 3, 4], [3, 4, 1, 2], 2': [
                es_desplazamiento([1, 2, 3, 4], [3, 4, 1, 2], 2),
                True
            ],
            'Argumentos usados: [1, 2], [3, 4], 1': [
                es_desplazamiento([1, 2], [3, 4], 1),
                False
            ],
            'Argumentos usados: [1, 2, 3, 4], [1, 2, 3, 4], 0': [
                es_desplazamiento([1, 2, 3, 4], [1, 2, 3, 4], 0),
                True
            ],
            'Argumentos usados: [6.2, 8, -3, 1, 2.4], [1, 2.4, -3, 8, 6.2], 5': [
                es_desplazamiento([6.2, 8, -3, 1, 2.4], [1, 2.4, -3, 8, 6.2], 5),
                False
            ],
            'Argumentos usados: [6.2, 8, -3, 1, 2.4], [6.2, 8, -3, 1, 2.4], 5': [
                es_desplazamiento([6.2, 8, -3, 1, 2.4], [6.2, 8, -3, 1, 2.4], 5),
                True
            ],
            'Argumentos usados: [4, 4], [4, 4], 3': [
                es_desplazamiento([4, 4], [4, 4], 3),
                True
            ],
            'Argumentos usados: [7, 1.1, 0, -8, 9.15], [9.15, 7, 1.1, 0, 3], 1': [
                es_desplazamiento([7, 1.1, 0, -8, 9.15], [9.15, 7, 1.1, 0, 3], 1),
                False
            ],
            'Argumentos usados: [-2], [-2], 6': [
                es_desplazamiento([-2], [-2], 6),
                True
            ],
            'Argumentos usados: [], [], 2': [
                es_desplazamiento([], [], 2),
                True
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_suma_cada_n(self):
        pruebas = {
            'Argumentos usados: [5, 2, 1, 6, 4, 9, 3, 7, 8], 3': [
                suma_cada_n([5, 2, 1, 6, 4, 9, 3, 7, 8], 3),
                18
            ],
            'Argumentos usados: [1.5, 2, -3, 4], 5': [
                suma_cada_n([1.5, 2, -3, 4], 5),
                0
            ],
            'Argumentos usados: [1, 2, 3, -4], 1': [
                suma_cada_n([1, 2, 3, -4], 1),
                2
            ],
            'Argumentos usados: [6, 1, 2, 3, 7, 9, 4, 8], 6': [
                suma_cada_n([6, 1, 2, 3, 7, 9, 4, 8], 6),
                9
            ],
            'Argumentos usados: [9, -2, 3.5, -6.2, 1], 2': [
                suma_cada_n([9, -2, 3.5, -6.2, 1], 2),
                -8.2
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_desplazar_ceros(self):
        pruebas = {
            'Argumento usado: [5, 8, 0, 3, 0, 0, 4]': [
                desplazar_ceros([5, 8, 0, 3, 0, 0, 4]),
                [5, 8, 3, 4, 0, 0, 0]
            ],
            'Argumento usado: [1, 2, 3, 0, 0, 0]': [
                desplazar_ceros([1, 2, 3, 0, 0, 0]),
                [1, 2, 3, 0, 0, 0]
            ],
            'Argumento usado: [0, 0, 0, 0]': [
                desplazar_ceros([0, 0, 0, 0]),
                [0, 0, 0, 0]
            ],
            'Argumento usado: [1, 2, 3, 4]': [
                desplazar_ceros([1, 2, 3, 4]),
                [1, 2, 3, 4]
            ],
            'Argumento usado: [0, 0, 0, 1, 2, 3]': [
                desplazar_ceros([0, 0, 0, 1, 2, 3]),
                [1, 2, 3, 0, 0, 0]
            ],
            'Argumento usado: []': [
                desplazar_ceros([]),
                []
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_desanidar(self):
        pruebas = {
            'Argumento usado: [[1, 0, 4], ["a", "b"], [True, False, True, True]]': [
                desanidar([[1, 0, 4], ["a", "b"], [True, False, True, True]]),
                [1, 0, 4, "a", "b", True, False, True, True]
            ],
            'Argumento usado: [[], ["a", "b"]]': [
                desanidar([[], ["a", "b"]]),
                ["a", "b"]
            ],
            'Argumento usado: [["a", "b"], []]': [
                desanidar([["a", "b"], []]),
                ["a", "b"]
            ],
            'Argumento usado: [[1], [2], [3]]': [
                desanidar([[1], [2], [3]]),
                [1, 2, 3]
            ],
            'Argumento usado: [[], [], []]': [
                desanidar([[], [], []]),
                []
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_cantidad_aprobados(self):
        pruebas = {
            'Argumento usado: [["Mario Perez", 331, 6], ["Luisa Rey", 112, 3], ["Fernanda Torres", 256, 8], ["Martín '
            'Sotomayor", 209, 7]]': [
                cantidad_aprobados([["Mario Perez", 331, 6],
                                    ["Luisa Rey", 112, 3],
                                    ["Fernanda Torres", 256, 8],
                                    ["Martín Sotomayor", 209, 7]]),
                3
            ],
            'Argumento usado: [["Mario Perez", 331, 6], ["Luisa Rey", 112, 6], ["Fernanda Torres", 256, 6]]': [
                cantidad_aprobados([["Mario Perez", 331, 6],
                                    ["Luisa Rey", 112, 6],
                                    ["Fernanda Torres", 256, 6]]),
                3
            ],
            'Argumento usado: [["Mario Perez", 331, 1], ["Luisa Rey", 112, 5], ["Fernanda Torres", 256, 2], ["Martín '
            'Sotomayor", 209, 4]]': [
                cantidad_aprobados([["Mario Perez", 331, 1],
                                    ["Luisa Rey", 112, 5],
                                    ["Fernanda Torres", 256, 2],
                                    ["Martín Sotomayor", 209, 4]]),
                0
            ],
            'Argumento usado: [["Mario Perez", 331, 6]]': [
                cantidad_aprobados([["Mario Perez", 331, 6]]),
                1
            ],
            'Argumento usado: []': [
                cantidad_aprobados([]),
                0
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_suma_diagonal(self):
        pruebas = {
            'Argumento usado: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]': [
                suma_diagonal([[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                15
            ],
            'Argumento usado: [[5, 3], [8, 0]]': [
                suma_diagonal([[5, 3], [8, 0]]),
                5
            ],
            'Argumento usado: []': [
                suma_diagonal([]),
                0
            ],
            'Argumento usado: [[4]]': [
                suma_diagonal([[4]]),
                4
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_buscar_pais(self):
        pruebas = {
            'Argumentos usados: [("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), ("Liverpool", "Inglaterra"), '
            '("Madrid", "España")], "Glasgow"': [
                buscar_pais([("Buenos Aires", "Argentina"),
                             ("Glasgow", "Escocia"),
                             ("Liverpool", "Inglaterra"),
                             ("Madrid", "España")
                             ],
                            "Glasgow"),
                "Escocia"
            ],
            'Argumentos usados: [("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), ("Liverpool", "Inglaterra"), '
            '("Madrid", "España")], "Montevideo"': [
                buscar_pais([("Buenos Aires", "Argentina"),
                             ("Glasgow", "Escocia"),
                             ("Liverpool", "Inglaterra"),
                             ("Madrid", "España")
                             ],
                            "Montevideo"),
                None
            ],
            'Argumentos usados: [], "Glasgow"': [
                buscar_pais([], "Glasgow"),
                None
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_buscar_destino(self):
        pruebas = {
            'Argumentos usados: [(100, "Buenos Aires"), (110, "Madrid"), (120, "Glasgow")], '
            '[("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), ("Liverpool", "Inglaterra"), ("Madrid", "España")],'
            ' 100': [
                buscar_destino(
                    [(100, "Buenos Aires"),
                     (110, "Madrid"),
                     (120, "Glasgow")
                     ],
                    [("Buenos Aires", "Argentina"),
                     ("Glasgow", "Escocia"),
                     ("Liverpool", "Inglaterra"),
                     ("Madrid", "España")
                     ],
                    100),
                "Argentina"
            ],
            'Argumentos usados: [(100, "Buenos Aires"), (110, "Madrid"), (120, "Glasgow"), (130, "Madrid")], [("Buenos'
            ' Aires", "Argentina"), ("Glasgow", "Escocia"), ("Liverpool", "Inglaterra"), ("Madrid", "España")], 130': [
                buscar_destino(
                    [(100, "Buenos Aires"),
                     (110, "Madrid"),
                     (120, "Glasgow"),
                     (130, "Madrid")
                     ],
                    [("Buenos Aires", "Argentina"),
                     ("Glasgow", "Escocia"),
                     ("Liverpool", "Inglaterra"),
                     ("Madrid", "España")
                     ],
                    130),
                "España"
            ],
            'Argumentos usados: [("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), ("Liverpool", "Inglaterra"), '
            '("Madrid", "España")], [(100, "Buenos Aires"), (110, "Madrid"), (120, "Glasgow")], 140': [
                buscar_destino(
                    [("Buenos Aires", "Argentina"),
                     ("Glasgow", "Escocia"),
                     ("Liverpool", "Inglaterra"),
                     ("Madrid", "España")
                     ],
                    [(100, "Buenos Aires"),
                     (110, "Madrid"),
                     (120, "Glasgow")
                     ],
                    140),
                None
            ],
            'Argumentos usados: [("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), ("Liverpool", "Inglaterra"), '
            '("Madrid", "España")], [(100, "Montevideo"), (110, "Madrid"), (120, "Glasgow")], 100': [
                buscar_destino(
                    [("Buenos Aires", "Argentina"),
                     ("Glasgow", "Escocia"),
                     ("Liverpool", "Inglaterra"),
                     ("Madrid", "España")
                     ],
                    [(100, "Montevideo"),
                     (110, "Madrid"),
                     (120, "Glasgow")],
                    100),
                None
            ],
            'Argumentos usados: [("Buenos Aires", "Argentina"), ("Glasgow", "Escocia")], [], 100': [
                buscar_destino([
                    ("Buenos Aires", "Argentina"),
                    ("Glasgow", "Escocia")
                ],
                    [],
                    100),
                None
            ],
            'Argumentos usados: [], [(100, "Buenos Aires"), (110, "Madrid"), (120, "Glasgow")], 100': [
                buscar_destino([],
                               [(100, "Buenos Aires"),
                                (110, "Madrid"),
                                (120, "Glasgow")
                                ],
                               100),
                None
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)
