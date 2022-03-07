#############################
# NO MODIFICAR ESTE ARCHIVO #
#############################

import unittest
from src.strings import *


class TestsFuncionesStrings(unittest.TestCase):

    def test_cantidad_par_caracteres(self):
        pruebas = {
            'Argumentos usados: "aaa", "aaa"': [
                cantidad_par_caracteres("aaa", "aaa"), 
                False
            ],
            'Argumentos usados: "aaa", "aaaa"': [
                cantidad_par_caracteres("aaa", "aaaa"), 
                False
            ],
            'Argumentos usados: "aaaa", "aaa"': [
                cantidad_par_caracteres("aaaa", "aaa"), 
                False
            ],
            'Argumentos usados: "aaaa", "aaaa"': [
                cantidad_par_caracteres("aaaa", "aaaa"), 
                True
            ],
            'Argumentos usados: "" (string vacío), "aaaa"': [
                cantidad_par_caracteres("", "aaaa"), 
                True
            ],
            'Argumentos usados: "aaaa", ""': [
                cantidad_par_caracteres("aaaa", ""), 
                True
            ],
            'Argumentos usados: "" (string vacío), ""': [
                cantidad_par_caracteres("", ""), 
                True
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_contar_ocurrencias(self):
        pruebas = {
            'Argumentos usados: "Esto es una frase", "s"': [
                contar_ocurrencias("Esto es una frase", "s"), 
                3
            ],
            'Argumentos usados: "Esto es una frase", "x"': [
                contar_ocurrencias("Esto es una frase", "x"), 
                0
            ],
            'Argumentos usados: "Esto es una frase", "e"': [
                contar_ocurrencias("Esto es una frase", "e"), 
                2
            ],
            'Argumentos usados: "Esto es una frase", "E"': [
                contar_ocurrencias("Esto es una frase", "E"), 
                1
            ],
            'Argumentos usados: "" (string vacío), "a"': [
                contar_ocurrencias("", "a"), 0
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)

    
    def test_contar_vocales_totales(self):
        pruebas = {
            'Argumento usado: "Esto es una frase"': [
                contar_vocales_totales("Esto es una frase"), 
                7
            ],
            'Argumento usado: "aeiou"': [
                contar_vocales_totales("aeiou"), 
                5
            ],
            'Argumento usado: "AEIOU"': [
                contar_vocales_totales("AEIOU"), 
                5
            ],
            'Argumento usado: "abcdEfgHijkLMnOPqrsTuVwXyz"': [
                contar_vocales_totales("abcdEfgHijkLMnOPqrsTuVwXyz"), 
                5
            ],
            'Argumento usado: "zzz"': [
                contar_vocales_totales("zzz"), 
                0
            ],
            'Argumento usado: "123"': [
                contar_vocales_totales("123"), 
                0
            ],
            'Argumento usado: ""': [
                contar_vocales_totales(""), 
                0
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_contar_vocales_unicas(self):
        pruebas = {
            'Argumento usado: "Esto Es Una Frase"': [
                contar_vocales_unicas("Esto Es Una Frase"), 
                4
            ],
            'Argumento usado: "aeiou"': [
                contar_vocales_unicas("aeiou"), 
                5
            ],
            'Argumento usado: "aeiouAEIOU"': [
                contar_vocales_unicas("aeiouAEIOU"), 
                5
            ],
            'Argumento usado: "aaeeiioouuAAEEIIOOUU"': [
                contar_vocales_unicas("aeiouAEIOU"), 
                5
            ],
            'Argumento usado: "abcdEfgHijkLMnOPqrsTuVwXyz"': [
                contar_vocales_unicas("abcdEfgHijkLMnOPqrsTuVwXyz"), 
                5
            ],
            'Argumento usado: "zzz"': [
                contar_vocales_unicas("zzz"), 
                0
            ],
            'Argumento usado: "123"': [
                contar_vocales_unicas("123"), 
                0
            ],
            'Argumento usado: "" (string vacío)': [
                contar_vocales_unicas(""), 0
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_reemplazar_caracter_con_asterisco(self):
        pruebas = {
            'Argumentos usados: "esto es una frase", "a"': [
                reemplazar_caracter_con_asterisco("esto es una frase", "a"), 
                "esto es un* fr*se"
            ],
            'Argumentos usados: "esto es una frase", "u"': [
                reemplazar_caracter_con_asterisco("esto es una frase", "u"), 
                "esto es *na frase"
            ],
            'Argumentos usados: "Esto es una frase", "E"': [
                reemplazar_caracter_con_asterisco("Esto es una frase", "E"), 
                "*sto es una frase"
            ],
            'Argumentos usados: "esto es una frase", "z"': [
                reemplazar_caracter_con_asterisco("esto es una frase", "z"), 
                "esto es una frase"
            ],
            'Argumentos usados: "esto es una frase", ""': [
                reemplazar_caracter_con_asterisco("esto es una frase", ""), 
                "esto es una frase"
            ],
            'Argumentos usados: "" (string vacío), "a"': [
                reemplazar_caracter_con_asterisco("", "a"), ""
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_invertir_cadena(self):
        pruebas = {
            'Argumento usado: "Esto es una frase!"': [
                invertir_cadena("Esto es una frase!"), 
                "!esarf anu se otsE"
            ],
            'Argumento usado: "aaaa"': [
                invertir_cadena("aaaa"), 
                "aaaa"
            ],
            'Argumento usado: "a"': [
                invertir_cadena("a"), 
                "a"
            ],
            'Argumento usado: ""': [
                invertir_cadena(""), 
                ""
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_reemplazar_simbolos(self):
        pruebas = {
            'Argumentos usados: "--Esto es 1 frase donde reemplazaremos con @ cada símbolo", "@"': [
                reemplazar_simbolos("--Esto es 1 frase donde reemplazaremos con @ cada símbolo", "@"), 
                "@@Esto es 1 frase donde reemplazaremos con @ cada símbolo"
            ],
            'Argumentos usados: "Esto es una frase", "*"': [
                reemplazar_simbolos("Esto es una frase", "*"), 
                "Esto es una frase"
            ],
            'Argumentos usados: "Esto es una frase!", "-"': [
                reemplazar_simbolos("Esto es una frase!", "-"), 
                "Esto es una frase-"
            ],
            'Argumentos usados: "/$Esto/ es@ una# frase=", "@"': [
                reemplazar_simbolos("/$Esto/ es@ una# frase=", "@"), 
                "@@Esto@ es@ una@ frase@"
            ],
            'Argumentos usados: "1234", "}"': [
                reemplazar_simbolos("1234", "}"), 
                "1234"
            ],
            'Argumentos usados: "@@@", "@"': [
                reemplazar_simbolos("@@@", "@"), 
                "@@@"
            ],
            'Argumentos usados: " " (string vacío), "*"': [
                reemplazar_simbolos(" ", "*"), 
                " "
            ],
            'Argumentos usados: "" (string vacío), "*"': [
                reemplazar_simbolos("", "*"), 
                ""
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_porcentaje_digitos_numericos(self):
        pruebas = {
            'Argumento usado: "Tenemos 1 dígito"': [
                porcentaje_digitos_numericos("Tenemos 1 dígito"), 
                6.25
            ],
            'Argumento usado: "1984"': [
                porcentaje_digitos_numericos("1984"), 
                100
            ],
            'Argumento usado: "Esto es una frase"': [
                porcentaje_digitos_numericos("Esto es una frase"), 
                0
            ],
            'Argumento usado: "" (string vacío)': [
                porcentaje_digitos_numericos(""), 
                0
            ],
            'Argumento usado: "abc1"': [
                porcentaje_digitos_numericos("abc1"), 
                25
            ],
            'Argumento usado: "Matemática: 10"': [
                porcentaje_digitos_numericos("Matemática: 10"), 
                14.285714285714286
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_clasificar_cadena_numerica(self):
        pruebas = {
            'Argumento usado: "123456"': [
                clasificar_cadena_numerica("123456"),
                "246$36"
            ],
            'Argumento usado: "2222"': [
                clasificar_cadena_numerica("2222"), 
                "2222$"
            ],
            'Argumento usado: "1234567890"': [
                clasificar_cadena_numerica("1234567890"), 
                "24680$3690"
            ],
            'Argumento usado: "3333"': [
                clasificar_cadena_numerica("3333"), 
                "$3333"
            ],
            'Argumento usado: "6666"': [
                clasificar_cadena_numerica("6666"), 
                "6666$6666"
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_caracteres_centrales(self):
        pruebas = {
            'Argumento usado: "AbcDefGhi"': [
                caracteres_centrales("AbcDefGhi"), 
                "Def"
            ],
            'Argumento usado: "A   A"': [
                caracteres_centrales("A   A"), 
                "   "
            ],
            'Argumento usado: "bAAAb"': [
                caracteres_centrales("bAAAb"), 
                "AAA"
            ],
            'Argumento usado: "AAAAA"': [
                caracteres_centrales("AAAAA"), 
                "AAA"
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_es_palindromo(self):
        pruebas = {
            'Argumento usado: "abba"': [
                es_palindromo("abba"), 
                True
            ],
            'Argumento usado: "baéceab"': [
                es_palindromo("baéceab"), 
                False
            ],
            'Argumento usado: "aba"': [
                es_palindromo("aba"),
                 True
            ],
            'Argumento usado: "aa"': [
                es_palindromo("aa"), 
                True
            ],
            'Argumento usado: "a"': [
                es_palindromo("a"), 
                True
            ],
            'Argumento usado: "" (string vacío)': [
                es_palindromo(""), 
                False
            ],
            'Argumento usado: "Aba"': [
                es_palindromo("Aba"), 
                True
            ],
            'Argumento usado: "ab"': [
                es_palindromo("ab"), 
                False
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)
                

    def test_incluye_caracteres(self):
        pruebas = {
            'Argumentos usados: "super", "supermercado"': [
                incluye_caracteres("super", "supermercado"), 
                True
            ],
            'Argumentos usados: "aaa", "rosa"': [
                incluye_caracteres("aaa", "rosa"), 
                True
            ],
            'Argumentos usados: "abc", "abecedario"': [
                incluye_caracteres("abc", "abecedario"), 
                True
            ],
            'Argumentos usados: "e", "celular"': [
                incluye_caracteres("e", "celular"), 
                True
            ],
            'Argumentos usados: "abcf", "abecedario"': [
                incluye_caracteres("abcf", "abecedario"), 
                False
            ],
            'Argumentos usados: "Plt", "pelota"': [
                incluye_caracteres("Plt", "pelota"), 
                False
            ],
            'Argumentos usados: "Plt", "Pelota"': [
                incluye_caracteres("Plt", "Pelota"), 
                True
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_son_anagrama(self):
        pruebas = {
            'Argumentos usados: "aval", "lava"': [
                son_anagrama("aval", "lava"), 
                True
            ],
            'Argumentos usados: "aval", "lavar"': [
                son_anagrama("aval", "lavar"), 
                False
            ],
            'Argumentos usados: "aaa", "aaa"': [
                son_anagrama("aaa", "aaa"), 
                True
            ],
            'Argumentos usados: "Aaa", "aaa"': [
                son_anagrama("aaa", "aaa"), 
                True
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)        


    def test_cuantos_eliminar_para_anagrama(self):
        pruebas = {
            'Argumentos usados: "avala", "lavar"': [
                cuantos_eliminar_para_anagrama("avala", "lavar"), 
                2
            ],
            'Argumentos usados: "aval", "lava"': [
                cuantos_eliminar_para_anagrama("aval", "lava"),
                0
            ],
            'Argumentos usados: "aval", "lavar"': [
                cuantos_eliminar_para_anagrama("aval", "lavar"), 
                1
            ],
            'Argumentos usados: "avala", "lava"': [
                cuantos_eliminar_para_anagrama("avala", "lava"), 
                1
            ],
            'Argumentos usados: "AVAL", "lavaran"': [
                cuantos_eliminar_para_anagrama("AVAL", "lavaran"), 
                3
            ],
            'Argumentos usados: "aval", "LAVA"': [
                cuantos_eliminar_para_anagrama("aval", "LAVA"), 
                0
            ],
            'Argumentos usados: "abc", "def"': [
                cuantos_eliminar_para_anagrama("abc", "def"), 
                6
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_invertir_palabras(self):
        pruebas = {
            'Argumentos usados: "Esto es una frase."': [
                invertir_palabras("Esto es una frase."), 
                "otsE se anu .esarf"
            ],
            'Argumentos usados: "otsE se anu !esarf"': [
                invertir_palabras("otsE se anu !esarf"), 
                "Esto es una frase!"
            ],
            'Argumentos usados: "palabra"': [
                invertir_palabras("palabra"), 
                "arbalap"
            ],
            'Argumentos usados: "123"': [
                invertir_palabras("123"), 
                "321"
            ],
            'Argumentos usados: "a b c"': [
                invertir_palabras("a b c"), 
                "a b c"
            ],
            'Argumentos usados: "" (string vacío)': [
                invertir_palabras(""), 
                ""
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_longitud_ultima_palabra(self):
        pruebas = {
            'Argumento usado: "esto es una frase"': [
                longitud_ultima_palabra("esto es una frase"), 
                5
            ],
            'Argumento usado: "   espacios   "': [
                longitud_ultima_palabra("   espacios   "), 
                8
            ],
            'Argumento usado: "palabra"': [
                longitud_ultima_palabra("palabra"), 
                7
            ],
            'Argumento usado: "   esto   es   una   frase   "': [
                longitud_ultima_palabra("   esto   es   una   frase   "), 
                5
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_convertir_a_titulo(self):
        pruebas = {
            'Argumento usado: "esto es una frase"': [
                convertir_a_titulo("esto es una frase"),
                "Esto Es Una Frase"
            ],
            'Argumento usado: "ESTO ES UNA FRASE"': [
                convertir_a_titulo("ESTO ES UNA FRASE"),
                "Esto Es Una Frase"
            ],
            'Argumento usado: "palabra"': [
                convertir_a_titulo("palabra"),
                "Palabra"
            ],
            'Argumento usado: "Palabra"': [
                convertir_a_titulo("Palabra"), 
                "Palabra"
            ],
            'Argumento usado: "    esto es una frase"': [
                convertir_a_titulo("    esto es una frase"), 
                "    Esto Es Una Frase"
            ],
            'Argumento usado: "esto es una frase   "': [
                convertir_a_titulo("esto es una frase   "), 
                "Esto Es Una Frase   "
            ],
            'Argumento usado: "esto   es   una   frase"': [
                convertir_a_titulo("esto   es   una   frase"), 
                "Esto   Es   Una   Frase"
            ],
            'Argumento usado: "1esto 2es 3una 4frase"': [
                convertir_a_titulo("1esto 2es 3una 4frase"), 
                "1Esto 2Es 3Una 4Frase"
            ],
            'Argumento usado: "esto1 es2 una3 frase4"': [
                convertir_a_titulo("esto1 es2 una3 frase4"), 
                "Esto1 Es2 Una3 Frase4"
            ],
            'Argumento usado: "e1s2t3o4 e1s2 u1n2a3 f1r2a3s4e5"': [
                convertir_a_titulo("e1s2t3o4 e1s2 u1n2a3 f1r2a3s4e5"), 
                "E1s2t3o4 E1s2 U1n2a3 F1r2a3s4e5"
            ],
            'Argumento usado: "esto_es_una_frase"': [
                convertir_a_titulo("esto_es_una_frase"), 
                "Esto_Es_Una_Frase"
            ],
            'Argumento usado: "They\'re my best friend\'s siblings"': [
                convertir_a_titulo("They're my best friend's siblings"), 
                "They're My Best Friend's Siblings"
            ],
            'Argumento usado: "" (string vacío)': [
                convertir_a_titulo(""), 
                ""
            ],
            'Argumento usado: " "': [
                convertir_a_titulo(" "), 
                " "
            ],
            'Argumento usado: "123"': [
                convertir_a_titulo("123"), 
                "123"
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_cifrar_cesar(self):
        pruebas = {
            'Argumentos usados: "esto es una frase", 2': [
                cifrar_cesar("esto es una frase", 2), 
                "guvq gu woc htcug"
            ],
            'Argumentos usados: "abc123 xyz987!", 4': [
                cifrar_cesar("abc123 xyz987!", 4), 
                "efg123 bcd987!"
            ],
            'Argumentos usados: "esto es una frase", 6': [
                cifrar_cesar("esto es una frase", 6), 
                "kyzu ky asg lxgyk"
            ],
            'Argumentos usados: "123", 8': [
                cifrar_cesar("123", 8), 
                "123"
            ],
            'Argumentos usados: "esto es una frase", 27': [
                cifrar_cesar("esto es una frase", 27), 
                "esto es una frase"
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_rotar_n_posiciones(self):
        pruebas = {
            'Argumentos usados: "Esto es una frase", 6': [
                rotar_n_posiciones("Esto es una frase", 6), 
                " fraseEsto es una"
            ],
            'Argumentos usados: "palabra", 3': [
                rotar_n_posiciones("palabra", 3), 
                "brapala"
            ],
            'Argumentos usados: "palabra", 10': [
                rotar_n_posiciones("palabra", 10), 
                "brapala"
            ],
            'Argumentos usados: "Esto es una frase", 0': [
                rotar_n_posiciones("Esto es una frase", 0), 
                "Esto es una frase"
            ],
            'Argumentos usados: "palabra", 7': [
                rotar_n_posiciones("palabra", 7), 
                "palabra"
            ],
            'Argumentos usados: "", 5': [
                rotar_n_posiciones("", 5), 
                ""
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)


    def test_comprimir_RLE(self):
        pruebas = {
            'Argumento usado: "aaabbc"': [
                comprimir_RLE("aaabbc"), 
                "a3b2c"
            ],
            'Argumento usado: "abcde"': [
                comprimir_RLE("abcde"), 
                "abcde"
            ],
            'Argumento usado: "abbccc"': [
                comprimir_RLE("abbccc"), 
                "ab2c3"
            ],
            'Argumento usado: "a"': [
                comprimir_RLE("a"), 
                "a"
            ],
            'Argumento usado: "aaaa"': [
                comprimir_RLE("aaaa"), 
                "a4"
            ],
            'Argumento usado: "Aaaa"': [
                comprimir_RLE("Aaaa"), 
                "Aa3"
            ],
            'Argumento usado: "a$bb&&&&&c"': [
                comprimir_RLE("a$bb&&&&&c"), 
                "a$b2&5c"
            ],
            'Argumento usado: ""': [
                comprimir_RLE(""), ""
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba = prueba):
                self.assertEqual(a, b, prueba)