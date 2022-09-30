#############################
# NO MODIFICAR ESTE ARCHIVO #
#############################

import unittest
from ESP.src.listas import *


class TestsFuncionesListas(unittest.TestCase):

    def test_productoria_numeros(self):
        pruebas = {
            'Argumento usado: numeros=[1, 2, 3, 4]': [
                productoria_numeros(numeros=[1, 2, 3, 4]),
                24
            ],
            'Argumento usado: numeros=[0, 3, 7, 9]': [
                productoria_numeros(numeros=[0, 3, 7, 9]),
                0
            ],
            'Argumento usado: numeros=[]': [
                productoria_numeros(numeros=[]),
                None
            ],
            'Argumento usado: numeros=[1, 1, 1]': [
                productoria_numeros(numeros=[1, 1, 1]),
                1
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_mayor_elemento(self):
        pruebas = {
            'Argumento usado: strings=["x", "y", "z"]': [
                mayor_elemento(strings=["x", "y", "z"]),
                "z"
            ],
            'Argumento usado: strings=["z", "y", "x"]': [
                mayor_elemento(strings=["z", "y", "z"]),
                "z"
            ],
            'Argumento usado: strings=["abc", "cba", "cab", "bca"]': [
                mayor_elemento(strings=["abc", "cba", "cab", "bca"]),
                "cba"
            ],
            'Argumento usado: strings=["abc", "abc", "abc"]': [
                mayor_elemento(strings=["abc", "abc", "abc"]),
                "abc"
            ],
            'Argumento usado: strings=[]': [
                mayor_elemento(strings=[]),
                None
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_mayor_ganancia(self):
        pruebas = {
            'Argumento usado: precios=[70, 53, 15, 23, 41, 30]': [
                mayor_ganancia(precios=[70, 53, 15, 23, 41, 30]),
                55
            ],
            'Argumento usado: precios=[5, 5, 5, 5, 5]': [
                mayor_ganancia(precios=[5, 5, 5, 5, 5]),
                0
            ],
            'Argumento usado: precios=[15.6, 12.8, 4, 2.5, 19]': [
                mayor_ganancia(precios=[15.6, 12.8, 4, 2.5, 19]),
                16.5
            ],
            'Argumento usado: precios=[12, 21]': [
                mayor_ganancia(precios=[12, 21]),
                9
            ],
            'Argumento usado: precios=[21, 12]': [
                mayor_ganancia(precios=[21, 12]),
                9
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_elementos_unicos(self):
        pruebas = {
            'Argumento usado: puede_tener_duplicados=[3, False, "a", 1, 1, 2, 2, False, 4]': [
                elementos_unicos(puede_tener_duplicados=[3, False, "a", 1, 1, 2, 4, False, 4]),
                [3, "a", 2]
            ],
            'Argumento usado: puede_tener_duplicados=[1, 1, 1]': [
                elementos_unicos(puede_tener_duplicados=[1, 1, 1]),
                []
            ],
            'Argumento usado: puede_tener_duplicados=["hola", True, 5.1]': [
                elementos_unicos(puede_tener_duplicados=["hola", True, 5.1]),
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
            'Argumento usado: numeros=[-5, 3, 2, -4, 7]': [
                porcentaje_pares_impares(numeros=[-5, 3, 2, -4, 7]),
                (40.0, 60.0)
            ],
            'Argumento usado: numeros=[1, 1, 1, 1]': [
                porcentaje_pares_impares(numeros=[1, 1, 1, 1]),
                (0.0, 100.0)
            ],
            'Argumento usado: numeros=[1, 5]': [
                porcentaje_pares_impares(numeros=[1, 5]),
                (0.0, 100.0)
            ],
            'Argumento usado: numeros=[2, 4]': [
                porcentaje_pares_impares(numeros=[2, 4]),
                (100.0, 0.0)
            ],
            'Argumento usado: numeros=[1, 2, 3, 4]': [
                porcentaje_pares_impares(numeros=[1, 2, 3, 4]),
                (50.0, 50.0)
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_sumar_indice(self):
        pruebas = {
            'Argumento usado: numeros=[1, 2, 3, 4, 5, 6]': [
                sumar_indice(numeros=[1, 2, 3, 4, 5, 6]),
                [1, 3, 5, 7, 9, 11]
            ],
            'Argumento usado: numeros=[0, 0, 0]': [
                sumar_indice(numeros=[0, 0, 0]),
                [0, 1, 2]
            ],
            'Argumento usado: numeros=[]': [
                sumar_indice(numeros=[]),
                []
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_sumas_parciales(self):
        pruebas = {
            'Argumento usado: numeros=[4, 6, 10, 7]': [
                sumas_parciales(numeros=[4, 6, 10, 7]),
                [4, 10, 20, 27]
            ],
            'Argumento usado: numeros=[1, 1, 1, 1, 1]': [
                sumas_parciales(numeros=[1, 1, 1, 1, 1]),
                [1, 2, 3, 4, 5]
            ],
            'Argumento usado: numeros=[1, 2, 3, 4]': [
                sumas_parciales(numeros=[1, 2, 3, 4]),
                [1, 3, 6, 10]
            ],
            'Argumento usado: numeros=[]': [
                sumas_parciales(numeros=[]),
                []
            ],
            'Argumento usado: numeros=[5, 0, 0, 0, 0]': [
                sumas_parciales(numeros=[5, 0, 0, 0, 0]),
                [5, 5, 5, 5, 5]
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_numeros_faltantes(self):
        pruebas = {
            'Argumento usado: numeros=[5, 0, 2, 9, 8, 12, 9]': [
                numeros_faltantes(numeros=[5, 0, 2, 9, 8, 12, 9]),
                [1, 3, 4, 6]
            ],
            'Argumento usado: numeros=[3, 7, 15, 3, 9]': [
                numeros_faltantes(numeros=[3, 7, 15, 3, 9]),
                [0, 1, 2, 4]
            ],
            'Argumento usado: numeros=[1, 2, 3, 4]': [
                numeros_faltantes(numeros=[1, 2, 3, 4]),
                [0]
            ],
            'Argumento usado: numeros=[0, 1, 2, 3]': [
                numeros_faltantes(numeros=[0, 1, 2, 3]),
                []
            ],
            'Argumento usado: numeros=[5]': [
                numeros_faltantes(numeros=[5]),
                [0]
            ],
            'Argumento usado: numeros=[]': [
                numeros_faltantes(numeros=[]),
                []
            ],
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_cuantos_numeros_menores(self):
        pruebas = {
            'Argumento usado: numeros=[6, 3, 3, 4, 2]': [
                cuantos_numeros_menores(numeros=[6, 3, 3, 4, 2]),
                [4, 1, 1, 3, 0]
            ],
            'Argumento usado: numeros=[3, 3, 3, 3]': [
                cuantos_numeros_menores(numeros=[3, 3, 3, 3]),
                [0, 0, 0, 0]
            ],
            'Argumento usado: numeros=[]': [
                cuantos_numeros_menores(numeros=[]),
                []
            ],
            'Argumento usado: numeros=[1]': [
                cuantos_numeros_menores(numeros=[1]),
                [0]
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_dos_maximos(self):
        pruebas = {
            'Argumento usado: numeros=[5, 3, 6, 2, 8]': [
                dos_maximos(numeros=[5, 3, 6, 2, 8]),
                (8, 6)
            ],
            'Argumento usado: numeros=[6, 8, 3, 5, 2]': [
                dos_maximos(numeros=[6, 8, 3, 5, 2]),
                (8, 6)
            ],
            'Argumento usado: numeros=[5, 3, 2, 8, 6]': [
                dos_maximos(numeros=[5, 3, 2, 8, 6]),
                (8, 6)
            ],
            'Argumento usado: numeros=[5, 5, 5, 5]': [
                dos_maximos(numeros=[5, 5, 5, 5]),
                (5, 5)
            ],
            'Argumento usado: numeros=[1.3, -4, 2.5, 7, -2.2]': [
                dos_maximos(numeros=[1.3, -4, 2.5, 7, -2.2]),
                (7, 2.5)
            ],
            'Argumento usado: numeros=[1, 2]': [
                dos_maximos(numeros=[1, 2]),
                (2, 1)
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_jugada_uno(self):
        pruebas = {
            'Argumentos usados: mano=["rojo 2", "azul 5", "verde 1"], carta_descubierta="rojo 3': [
                jugada_uno(mano=["rojo 2", "azul 5", "verde 1"], carta_descubierta="rojo 3"),
                True
            ],
            'Argumentos usados: mano=["rojo 2", "azul 5", "verde 1"], carta_descubierta="amarillo 3': [
                jugada_uno(mano=["rojo 2", "azul 5", "verde 1"], carta_descubierta="amarillo 3"),
                False
            ],
            'Argumentos usados: mano=["verde 4"], carta_descubierta="amarillo 4': [
                jugada_uno(mano=["verde 4"], carta_descubierta="amarillo 4"),
                True
            ],
            'Argumentos usados: mano=["verde 1"], carta_descubierta="verde 6': [
                jugada_uno(mano=["verde 1"], carta_descubierta="verde 6"),
                True
            ],
            'Argumentos usados: mano=["verde 1"], carta_descubierta="azul 5"': [
                jugada_uno(mano=["verde 1"], carta_descubierta="azul 5"),
                False
            ],
            'Argumentos usados: mano=[], carta_descubierta="azul 5"': [
                jugada_uno(mano=[], carta_descubierta="azul 5"),
                False
            ],
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_eliminar_ocurrencias_extra(self):
        pruebas = {
            'Argumentos usados: numeros=[1, 2, 3, 2, 3, 3], n=1': [
                descartar_ocurrencias_extra(numeros=[1, 2, 3, 2, 3, 3], n=1),
                [1, 2, 3]
            ],
            'Argumentos usados: numeros=[1, 2, 3, 2, 3, 3], n=3': [
                descartar_ocurrencias_extra(numeros=[1, 2, 3, 2, 3, 3], n=3),
                [1, 2, 3, 2, 3, 3]
            ],
            'Argumentos usados: numeros=[7, 4, 5, 4, 4, 7, 8, 4, 5], n=2': [
                descartar_ocurrencias_extra(numeros=[7, 4, 5, 4, 4, 7, 8, 4, 5], n=2),
                [7, 4, 5, 4, 7, 8, 5]
            ],
            'Argumentos usados: numeros=[1, 1, 1, 1, 1, 1], n=0': [
                descartar_ocurrencias_extra(numeros=[1, 1, 1, 1, 1, 1], n=0),
                []
            ],
            'Argumentos usados: numeros=["a", "a", "a"], n=1': [
                descartar_ocurrencias_extra(numeros=["a", "a", "a"], n=1),
                ["a"]
            ],
            'Argumentos usados: numeros=[], n=1': [
                descartar_ocurrencias_extra(numeros=[], n=1),
                []
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_es_desplazamiento(self):
        pruebas = {
            'Argumentos usados: numeros1=[1, 2, 3, 4], numeros2=[3, 4, 1, 2], n=2': [
                es_desplazamiento(numeros1=[1, 2, 3, 4], numeros2=[3, 4, 1, 2], n=2),
                True
            ],
            'Argumentos usados: numeros1=[1, 2], numeros2=[3, 4], n=1': [
                es_desplazamiento(numeros1=[1, 2], numeros2=[3, 4], n=1),
                False
            ],
            'Argumentos usados: numeros1=[1, 2, 3, 4], numeros2=[1, 2, 3, 4], n=0': [
                es_desplazamiento(numeros1=[1, 2, 3, 4], numeros2=[1, 2, 3, 4], n=0),
                True
            ],
            'Argumentos usados: numeros1=[6.2, 8, -3, 1, 2.4], numeros2=[1, 2.4, -3, 8, 6.2], n=5': [
                es_desplazamiento(numeros1=[6.2, 8, -3, 1, 2.4], numeros2=[1, 2.4, -3, 8, 6.2], n=5),
                False
            ],
            'Argumentos usados: numeros1=[6.2, 8, -3, 1, 2.4], numeros2=[6.2, 8, -3, 1, 2.4], n=5': [
                es_desplazamiento(numeros1=[6.2, 8, -3, 1, 2.4], numeros2=[6.2, 8, -3, 1, 2.4], n=5),
                True
            ],
            'Argumentos usados: numeros1=[4, 4], numeros2=[4, 4], n=3': [
                es_desplazamiento(numeros1=[4, 4], numeros2=[4, 4], n=3),
                True
            ],
            'Argumentos usados: numeros1=[7, 1.1, 0, -8, 9.15], numeros2=[9.15, 7, 1.1, 0, 3], n=1': [
                es_desplazamiento(numeros1=[7, 1.1, 0, -8, 9.15], numeros2=[9.15, 7, 1.1, 0, 3], n=1),
                False
            ],
            'Argumentos usados: numeros1=[-2], numeros2=[-2], n=6': [
                es_desplazamiento(numeros1=[-2], numeros2=[-2], n=6),
                True
            ],
            'Argumentos usados: numeros1=[], numeros2=[], n=2': [
                es_desplazamiento(numeros1=[], numeros2=[], n=2),
                True
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_suma_cada_n(self):
        pruebas = {
            'Argumentos usados: numeros=[5, 2, 1, 6, 4, 9, 3, 7, 8], n=3': [
                suma_cada_n(numeros=[5, 2, 1, 6, 4, 9, 3, 7, 8], n=3),
                18
            ],
            'Argumentos usados: numeros=[1.5, 2, -3, 4], n=5': [
                suma_cada_n(numeros=[1.5, 2, -3, 4], n=5),
                0
            ],
            'Argumentos usados: numeros=[1, 2, 3, -4], n=1': [
                suma_cada_n(numeros=[1, 2, 3, -4], n=1),
                2
            ],
            'Argumentos usados: numeros=[6, 1, 2, 3, 7, 9, 4, 8], n=6': [
                suma_cada_n(numeros=[6, 1, 2, 3, 7, 9, 4, 8], n=6),
                9
            ],
            'Argumentos usados: numeros=[9, -2, 3.5, -6.2, 1], n=2': [
                suma_cada_n(numeros=[9, -2, 3.5, -6.2, 1], n=2),
                -8.2
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_desplazar_ceros(self):
        pruebas = {
            'Argumento usado: numeros=[5, 8, 0, 3, 0, 0, 4]': [
                desplazar_ceros(numeros=[5, 8, 0, 3, 0, 0, 4]),
                [5, 8, 3, 4, 0, 0, 0]
            ],
            'Argumento usado: numeros=[1, 2, 3, 0, 0, 0]': [
                desplazar_ceros(numeros=[1, 2, 3, 0, 0, 0]),
                [1, 2, 3, 0, 0, 0]
            ],
            'Argumento usado: numeros=[0, 0, 0, 0]': [
                desplazar_ceros(numeros=[0, 0, 0, 0]),
                [0, 0, 0, 0]
            ],
            'Argumento usado: numeros=[1, 2, 3, 4]': [
                desplazar_ceros(numeros=[1, 2, 3, 4]),
                [1, 2, 3, 4]
            ],
            'Argumento usado: numeros=[0, 0, 0, 1, 2, 3]': [
                desplazar_ceros(numeros=[0, 0, 0, 1, 2, 3]),
                [1, 2, 3, 0, 0, 0]
            ],
            'Argumento usado: numeros=[]': [
                desplazar_ceros(numeros=[]),
                []
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_desanidar(self):
        pruebas = {
            'Argumento usado: listas=[[1, 0, 4], ["a", "b"], [True, False, True, True]]': [
                desanidar(listas=[[1, 0, 4], ["a", "b"], [True, False, True, True]]),
                [1, 0, 4, "a", "b", True, False, True, True]
            ],
            'Argumento usado: listas=[[], ["a", "b"]]': [
                desanidar(listas=[[], ["a", "b"]]),
                ["a", "b"]
            ],
            'Argumento usado: listas=[["a", "b"], []]': [
                desanidar(listas=[["a", "b"], []]),
                ["a", "b"]
            ],
            'Argumento usado: listas=[[1], [2], [3]]': [
                desanidar(listas=[[1], [2], [3]]),
                [1, 2, 3]
            ],
            'Argumento usado: listas=[[], [], []]': [
                desanidar(listas=[[], [], []]),
                []
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_cantidad_aprobados(self):
        pruebas = {
            'Argumento usado: resultados_examen=[["Mario Perez", 331, 6], ["Luisa Rey", 112, 3], ["Fernanda Torres", '
            '256, 8], ["Martín Sotomayor", 209, 7]]': [
                cantidad_aprobados(resultados_examen=[["Mario Perez", 331, 6],
                                                      ["Luisa Rey", 112, 3],
                                                      ["Fernanda Torres", 256, 8],
                                                      ["Martín Sotomayor", 209, 7]]),
                3
            ],
            'Argumento usado: resultados_examen=[["Mario Perez", 331, 6], ["Luisa Rey", 112, 6], '
            '["Fernanda Torres", 256, 6]]': [
                cantidad_aprobados(resultados_examen=[["Mario Perez", 331, 6],
                                                      ["Luisa Rey", 112, 6],
                                                      ["Fernanda Torres", 256, 6]]),
                3
            ],
            'Argumento usado: resultados_examen=[["Mario Perez", 331, 1], ["Luisa Rey", 112, 5], ["Fernanda Torres", '
            '256, 2], ["Martín Sotomayor", 209, 4]]': [
                cantidad_aprobados(resultados_examen=[["Mario Perez", 331, 1],
                                                      ["Luisa Rey", 112, 5],
                                                      ["Fernanda Torres", 256, 2],
                                                      ["Martín Sotomayor", 209, 4]]),
                0
            ],
            'Argumento usado: resultados_examen=[["Mario Perez", 331, 6]]': [
                cantidad_aprobados(resultados_examen=[["Mario Perez", 331, 6]]),
                1
            ],
            'Argumento usado: resultados_examen=[]': [
                cantidad_aprobados(resultados_examen=[]),
                0
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_suma_diagonal(self):
        pruebas = {
            'Argumento usado: matriz=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]': [
                suma_diagonal(matriz=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]),
                15
            ],
            'Argumento usado: matriz=[[5, 3], [8, 0]]': [
                suma_diagonal(matriz=[[5, 3], [8, 0]]),
                5
            ],
            'Argumento usado: matriz=[]': [
                suma_diagonal(matriz=[]),
                0
            ],
            'Argumento usado: matriz=[[4]]': [
                suma_diagonal(matriz=[[4]]),
                4
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_buscar_pais(self):
        pruebas = {
            'Argumentos usados: ciudades=[("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), '
            '("Liverpool", "Inglaterra"), ("Madrid", "España")], nombre_ciudad="Glasgow"': [
                buscar_pais(ciudades=[("Buenos Aires", "Argentina"),
                                      ("Glasgow", "Escocia"),
                                      ("Liverpool", "Inglaterra"),
                                      ("Madrid", "España")],
                            nombre_ciudad="Glasgow"),
                "Escocia"
            ],
            'Argumentos usados: ciudades=[("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), '
            '("Liverpool", "Inglaterra"), ("Madrid", "España")], nombre_ciudad="Montevideo"': [
                buscar_pais(ciudades=[("Buenos Aires", "Argentina"),
                                      ("Glasgow", "Escocia"),
                                      ("Liverpool", "Inglaterra"),
                                      ("Madrid", "España")],
                            nombre_ciudad="Montevideo"),
                None
            ],
            'Argumentos usados: ciudades=[], nombre_ciudad="Glasgow"': [
                buscar_pais(ciudades=[], nombre_ciudad="Glasgow"),
                None
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_buscar_destino(self):
        pruebas = {
            'Argumentos usados: boletos=[(100, "Buenos Aires"), (110, "Madrid"), (120, "Glasgow")], '
            'ciudades=[("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), ("Liverpool", "Inglaterra"), '
            '("Madrid", "España")], numero_boleto=100': [
                buscar_destino(boletos=[(100, "Buenos Aires"),
                                        (110, "Madrid"),
                                        (120, "Glasgow")],
                               ciudades=[("Buenos Aires", "Argentina"),
                                         ("Glasgow", "Escocia"),
                                         ("Liverpool", "Inglaterra"),
                                         ("Madrid", "España")],
                               numero_boleto=100),
                "Argentina"
            ],
            'Argumentos usados: boletos=[(100, "Buenos Aires"), (110, "Madrid"), (120, "Glasgow"), (130, "Madrid")], '
            'ciudades=[("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), ("Liverpool", "Inglaterra"), '
            '("Madrid", "España")], numero_boleto=130': [
                buscar_destino(boletos=[(100, "Buenos Aires"),
                                        (110, "Madrid"),
                                        (120, "Glasgow"),
                                        (130, "Madrid")],
                               ciudades=[("Buenos Aires", "Argentina"),
                                         ("Glasgow", "Escocia"),
                                         ("Liverpool", "Inglaterra"),
                                         ("Madrid", "España")],
                               numero_boleto=130),
                "España"
            ],
            'Argumentos usados: boletos=[("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), '
            '("Liverpool", "Inglaterra"), ("Madrid", "España")], ciudades=[(100, "Buenos Aires"), (110, "Madrid"), '
            '(120, "Glasgow")], numero_boleto=140': [
                buscar_destino(boletos=[("Buenos Aires", "Argentina"),
                                        ("Glasgow", "Escocia"),
                                        ("Liverpool", "Inglaterra"),
                                        ("Madrid", "España")],
                               ciudades=[(100, "Buenos Aires"),
                                         (110, "Madrid"),
                                         (120, "Glasgow")],
                               numero_boleto=140),
                None
            ],
            'Argumentos usados: boletos=[("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), '
            '("Liverpool", "Inglaterra"), ("Madrid", "España")], ciudades=[(100, "Montevideo"), (110, "Madrid"), '
            '(120, "Glasgow")], numero_boleto=100': [
                buscar_destino(boletos=[("Buenos Aires", "Argentina"),
                                        ("Glasgow", "Escocia"),
                                        ("Liverpool", "Inglaterra"),
                                        ("Madrid", "España")],
                               ciudades=[(100, "Montevideo"),
                                      (110, "Madrid"),
                                      (120, "Glasgow")],
                               numero_boleto=100),
                None
            ],
            'Argumentos usados: boletos=[("Buenos Aires", "Argentina"), ("Glasgow", "Escocia")], ciudades=[], '
            'numero_boleto=100': [
                buscar_destino(boletos=[("Buenos Aires", "Argentina"),
                                        ("Glasgow", "Escocia")],
                               ciudades=[],
                               numero_boleto=100),
                None
            ],
            'Argumentos usados: boletos=[], ciudades=[(100, "Buenos Aires"), (110, "Madrid"), (120, "Glasgow")], '
            'numero_boleto=100': [
                buscar_destino(boletos=[],
                               ciudades=[(100, "Buenos Aires"),
                                         (110, "Madrid"),
                                         (120, "Glasgow")],
                               numero_boleto=100),
                None
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)
