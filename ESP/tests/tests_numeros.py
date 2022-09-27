#############################
# NO MODIFICAR ESTE ARCHIVO #
#############################

import unittest
from ESP.src.numeros import *


class TestsFuncionesNumeros(unittest.TestCase):

    def test_menor(self):
        pruebas = {
            'Argumentos usados: 3, 1': [
                menor(3, 1), 
                1
            ],
            'Argumentos usados: 3, 3': [
                menor(3, 3), 
                3
            ],
            'Argumentos usados: -4, 1': [
                menor(-4, 1), 
                -4
            ],
            'Argumentos usados: 2, -3': [
                menor(2, -3), 
                -3
            ],
            'Argumentos usados: -1, -1': [
                menor(-1, -1), 
                -1
            ],
            'Argumentos usados: 0, 0': [
                menor(0, 0), 
                0
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_valor_absoluto(self):
        pruebas = {
            'Argumento usado: 3': [
                valor_absoluto(3), 
                3
            ],
            'Argumento usado: -10': [
                valor_absoluto(-10), 
                10
            ],
            'Argumento usado: 0': [
                valor_absoluto(0), 
                0
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_buscar_mes(self):
        pruebas = {
            'Argumento usado: 31122020': [
                buscar_mes(31122020), 
                12
            ],
            'Argumento usado: 5091946': [
                buscar_mes(5091946), 
                9
            ],
            'Argumento usado: 10021582': [
                buscar_mes(10021582), 
                2
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_sumar_multiplos(self):
        pruebas = {
            'Argumentos usados: 0, 30, 5': [
                sumar_multiplos(0, 30, 5), 
                105
            ],
            'Argumentos usados: -30, 0, 5': [
                sumar_multiplos(-30, 0, 5), 
                -105
            ],
            'Argumentos usados: 100, 105, 9': [
                sumar_multiplos(100, 105, 9), 
                0
            ],
            'Argumentos usados: 5, 5, 4': [
                sumar_multiplos(5, 5, 4), 
                0
            ],
            'Argumentos usados: 0, 0, 1': [
                sumar_multiplos(0, 0, 1), 
                0
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_es_capicua(self):
        pruebas = {
            'Argumento usado: 123321': [
                es_capicua(123321), 
                True
            ],
            'Argumento usado: 1234': [
                es_capicua(1234), 
                False
            ],
            'Argumento usado: 0': [
                es_capicua(0), 
                True
            ],
            'Argumento usado: 111': [
                es_capicua(111), 
                True
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_es_bisiesto(self):
        pruebas = {
            'Argumento usado: 2000': [
                es_bisiesto(2000), 
                True
            ],
            'Argumento usado: 2020': [
                es_bisiesto(2020), 
                True
            ],
            'Argumento usado: 1800': [
                es_bisiesto(1800), 
                False
            ],
            'Argumento usado: 1533': [
                es_bisiesto(1533), 
                False
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_dias_en_mes(self):
        pruebas = {
            'Argumentos usados: 11, 1981': [
                dias_en_mes(11, 1981), 
                30
            ],
            'Argumentos usados: 12, 2020': [
                dias_en_mes(12, 2020), 
                31
            ],
            'Argumentos usados: 2, 2020': [
                dias_en_mes(2, 2020), 
                29
            ],
            'Argumentos usados: 2, 2019': [
                dias_en_mes(2, 2019), 
                28
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_contar_digitos(self):
        pruebas = {
            'Argumento usado: 120': [
                contar_digitos(120), 
                3
            ],
            'Argumento usado: 123456789': [
                contar_digitos(123456789), 
                9
            ],
            'Argumento usado: 1': [
                contar_digitos(1), 
                1
            ],
            'Argumento usado: 0': [
                contar_digitos(0), 
                1
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_suma_digitos_cuadrados(self):
        pruebas = {
            'Argumento usado: 2': [
                suma_digitos_cuadrados(2), 
                4
            ],
            'Argumento usado: 200': [
                suma_digitos_cuadrados(200), 
                4
            ],
            'Argumento usado: 15': [
                suma_digitos_cuadrados(15), 
                26
            ],
            'Argumento usado: 6503': [
                suma_digitos_cuadrados(6503), 
                70
            ],
            'Argumento usado: 0': [
                suma_digitos_cuadrados(0), 
                0
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_porcentaje_digitos_pares(self):
        pruebas = {
            'Argumento usado: 123456': [
                porcentaje_digitos_pares(123456), 
                50.0
            ],
            'Argumento usado: 5555666555': [
                porcentaje_digitos_pares(5555666555), 
                30.0
            ],
            'Argumento usado: 0': [
                porcentaje_digitos_pares(0), 
                0.0
            ],
            'Argumento usado: 1': [
                porcentaje_digitos_pares(1), 
                0.0
            ],
            'Argumento usado: 1111': [
                porcentaje_digitos_pares(1111), 
                0.0
            ],
            'Argumento usado: 2222': [
                porcentaje_digitos_pares(2222), 
                100.0
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_es_pronico(self):
        pruebas = {
            'Argumento usado: 56': [
                es_pronico(56), 
                True
            ],
            'Argumento usado: 182': [
                es_pronico(182), 
                True
            ],
            'Argumento usado: 8': [
                es_pronico(8), 
                False
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_es_primo(self):
        pruebas = {
            'Argumento usado: 7': [
                es_primo(7), 
                True
            ],
            'Argumento usado: 10': [
                es_primo(10), 
                False
            ],
            'Argumento usado: 0': [
                es_primo(0), 
                False
            ],
            'Argumento usado: 47': [
                es_primo(47), 
                True
            ]

        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_factorial(self):
        pruebas = {
            'Argumento usado: 4': [
                factorial(4), 
                24
            ],
            'Argumento usado: 0': [
                factorial(0), 
                1
            ],
            'Argumento usado: 1': [
                factorial(1), 
                1
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_suma_primeros_n_fibonacci(self):
        pruebas = {
            'Argumento usado: 6': [
                suma_primeros_n_fibonacci(6), 
                12
            ],
            'Argumento usado: 2': [
                suma_primeros_n_fibonacci(2), 
                1
            ],
            'Argumento usado: 3': [
                suma_primeros_n_fibonacci(15), 
                986
            ],
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_mayor_divisor(self):
        pruebas = {
            'Argumento usado: 182': [
                mayor_divisor(182), 
                91
            ],
            'Argumento usado: 25': [
                mayor_divisor(25), 
                5
            ],
            'Argumento usado: 8': [
                mayor_divisor(8), 
                4
            ],
            'Argumento usado: 1': [
                mayor_divisor(1), 
                0
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_mcd_euclides(self):
        pruebas = {
            'Argumentos usados: 60, 24': [
                mcd_euclides(60, 24), 
                12
            ],
            'Argumentos usados: 24, 60': [
                mcd_euclides(24, 60), 
                12
            ],
            'Argumentos usados: 10, 20': [
                mcd_euclides(10, 20), 
                10
            ],
            'Argumentos usados: 1, 625': [
                mcd_euclides(1, 625), 
                1
            ],
            'Argumentos usados: 0, 14': [
                mcd_euclides(0, 14), 
                14
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_obtener_mes(self):
        pruebas = {
            'Argumentos usados: 200, 1969': [
                obtener_mes(200, 1969), 
                7
            ],
            'Argumentos usados: 1, 1981': [
                obtener_mes(1, 1981), 
                1
            ],
            'Argumentos usados: 60, 2020': [
                obtener_mes(60, 2020), 
                2
            ],
            'Argumentos usados: 60, 2018': [
                obtener_mes(60, 2018), 
                3
            ],
            'Argumentos usados: 365, 2014': [
                obtener_mes(365, 2014), 
                12
            ],
            'Argumentos usados: 366, 2020': [
                obtener_mes(366, 2020), 
                12
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_es_disarium(self):
        pruebas = {
            'Argumento usado: 518': [
                es_disarium(518), 
                True
            ],
            'Argumento usado: 175': [
                es_disarium(175), 
                True
            ],
            'Argumento usado: 89': [
                es_disarium(89), 
                True
            ],
            'Argumento usado: 182': [
                es_disarium(182), 
                False
            ],
            'Argumento usado: 91': [
                es_disarium(91), 
                False
            ],
            'Argumento usado: 4': [
                es_disarium(4), 
                True
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_ordenar_monedas(self):
        pruebas = {
            'Argumento usado: 5': [
                ordenar_monedas(5), 
                2
            ],
            'Argumento usado: 6': [
                ordenar_monedas(6), 
                3
            ],
            'Argumento usado: 8': [
                ordenar_monedas(8), 
                3
            ],
            'Argumento usado: 10': [
                ordenar_monedas(10), 
                4
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_cantidad_unos_solos(self):
        pruebas = {
            'Argumento usado: 141211': [
                cantidad_unos_solos(141211), 
                2
            ],
            'Argumento usado: 11411211': [
                cantidad_unos_solos(11411211), 
                0
            ],
            'Argumento usado: 1141121': [
                cantidad_unos_solos(1141121), 
                1
            ],
            'Argumento usado: 1111': [
                cantidad_unos_solos(1111), 
                0
            ],
            'Argumento usado: 321': [
                cantidad_unos_solos(321), 
                1
            ],
            'Argumento usado: 8888': [
                cantidad_unos_solos(8888), 
                0
            ],
            'Argumento usado: 0': [
                cantidad_unos_solos(0), 
                0
            ],
            'Argumento usado: 1': [
                cantidad_unos_solos(1), 
                1
            ],
            'Argumento usado: 12131415161718191': [
                cantidad_unos_solos(12131415161718191), 
                9
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)

