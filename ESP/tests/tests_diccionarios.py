#############################
# NO MODIFICAR ESTE ARCHIVO #
#############################

import unittest
from ESP.src.diccionarios import *


class TestsFuncionesDiccionarios(unittest.TestCase):

    def test_hallar_repetidos(self):
        pruebas = {
            'Argumentos usados: ["abc", "cde", "abc", "fff"], ["cde", "aaa"]': [
                hallar_repetidos(["abc", "cde", "abc", "fff"], ["cde", "aaa"]),
                {"cde"}
            ],
            'Argumentos usados: ["abc", "cde", "fgh", "ijk"], ["fgh", "abc"]': [
                hallar_repetidos(["abc", "cde", "fgh", "ijk"], ["fgh", "abc"]),
                {"abc", "fgh"}
            ],
            'Argumentos usados: ["abc", "cde"], ["fgh", "ijk"]': [
                hallar_repetidos(["abc", "cde"], ["fgh", "ijk"]),
                set()
            ],
            'Argumentos usados: ["abc"], ["abc"]': [
                hallar_repetidos(["abc"], ["abc"]),
                {"abc"}
            ],
            'Argumentos usados: [], []': [
                hallar_repetidos([], []),
                set()
            ],
            'Argumentos usados: ["abc", "cde", "abc", "fff"], []': [
                hallar_repetidos(["abc", "cde", "abc", "fff"], []),
                set()
            ],
            'Argumentos usados: [], ["abc", "cde", "abc", "fff"]': [
                hallar_repetidos([], ["abc", "cde", "abc", "fff"]),
                set()
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_solo_una_mascota(self):
        pruebas = {
            'Argumentos usados: ["Lucrecia Borges", "Juan Sebastián Balsa", "Cristóbal Colombraro"], ["Juan Sebastián '
            'Balsa", "Juan Jacobo Russo", "Ana Bologna", "Cristóbal Colombraro"]': [
                solo_una_mascota(["Lucrecia Borges", "Juan Sebastián Balsa", "Cristóbal Colombraro"],
                                 ["Juan Sebastián Balsa", "Juan Jacobo Russo", "Ana Bologna", "Cristóbal Colombraro"]),
                {"Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"}
            ],
            'Argumentos usados: ["Lucrecia Borges", "Juan Sebastián Balsa", "Cristóbal Colombraro"], ["Juan Jacobo '
            'Russo", "Ana Bologna"]': [
                solo_una_mascota(["Lucrecia Borges", "Juan Sebastián Balsa", "Cristóbal Colombraro"],
                                 ["Juan Jacobo Russo", "Ana Bologna"]),
                {"Lucrecia Borges", "Juan Sebastián Balsa", "Cristóbal Colombraro", "Juan Jacobo Russo", "Ana Bologna"}
            ],
            'Argumentos usados: ["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"], ["Lucrecia Borges", "Juan '
            'Jacobo Russo", "Ana Bologna"]': [
                solo_una_mascota(["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"],
                                 ["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"]),
                set()
            ],
            'Argumentos usados: ["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"], ["Lucrecia Borges", "Juan '
            'Jacobo Russo"]': [
                solo_una_mascota(["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"],
                                 ["Lucrecia Borges", "Juan Jacobo Russo"]),
                {"Ana Bologna"}
            ],
            'Argumentos usados: ["Lucrecia Borges", "Juan Jacobo Russo"], ["Lucrecia Borges", "Juan Jacobo Russo", '
            '"Ana Bologna"]': [
                solo_una_mascota(["Lucrecia Borges", "Juan Jacobo Russo"],
                                 ["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"]),
                {"Ana Bologna"}
            ],
            'Argumentos usados: [], ["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"]': [
                solo_una_mascota([],
                                 ["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"]),
                {"Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"}
            ],
            'Argumentos usados: ["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"], []': [
                solo_una_mascota(["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"],
                                 []),
                {"Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"}
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_elementos_unicos(self):
        pruebas = {
            'Argumento usado: [(1,2,3), (2,2,2,2), (3,4,5), (1,3,5,7,9)]': [
                elementos_unicos([(1, 2, 3), (2, 2, 2, 2), (3, 4, 5), (1, 3, 5, 7, 9)]),
                (1, 2, 3, 4, 5, 7, 9)
            ],
            'Argumento usado: [(1,2,3), (1,2,3), (1,2,3)]': [
                elementos_unicos([(1, 2, 3), (1, 2, 3), (1, 2, 3)]),
                (1, 2, 3)
            ],
            'Argumento usado: [(1,2,3)]': [
                elementos_unicos([(1, 2, 3)]),
                (1, 2, 3)
            ],
            'Argumento usado: [(1,2,3), (4,5,6), (7,8,9)]': [
                elementos_unicos([(1, 2, 3), (4, 5, 6), (7, 8, 9)]),
                (1, 2, 3, 4, 5, 6, 7, 8, 9)
            ],
            'Argumento usado: [(1,1,1), (1,1,1), (1,1,1)]': [
                elementos_unicos([(1, 1, 1), (1, 1, 1), (1, 1, 1)]),
                (1,)
            ],
            'Argumento usado: []': [
                elementos_unicos([]),
                ()
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_listar_apellidos(self):
        pruebas = {
            'Argumento usado: ["Lara Ruiz", "Esteban Raúl Perez", "Francina Soto", "Lucas Perez"]': [
                listar_apellidos(["Lara Ruiz", "Esteban Raúl Perez", "Francina Soto", "Lucas Perez"]),
                {"Ruiz", "Perez", "Soto"}
            ],
            'Argumento usado: []': [
                listar_apellidos([]),
                set()
            ],
            'Argumento usado: ["Lara Ruiz", "Esteban Raúl Perez", "Francina Soto"]': [
                listar_apellidos(["Lara Ruiz", "Esteban Raúl Perez", "Francina Soto"]),
                {"Ruiz", "Perez", "Soto"}
            ],
            'Argumento usado: ["Lara Ruiz", "Esteban Raúl Ruiz", "Francina Ruiz", "Lucas Ruiz"]': [
                listar_apellidos(["Lara Ruiz", "Esteban Raúl Ruiz", "Francina Ruiz", "Lucas Ruiz"]),
                {"Ruiz"}
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_domicilios_facturacion(self):
        pruebas = {
            'Argumento usado: [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol '
            '218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, "La Mancha '
            '761"), ("Jorge Russo", 15, 958, "Mirasol 218")]': [
                domicilios_facturacion([("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
                                        ("Jorge Russo", 7, 699, "Mirasol 218"),
                                        ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
                                        ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
                                        ("Jorge Russo", 15, 958, "Mirasol 218")]),
                {'Calle Las Flores 355', 'Mirasol 218', 'La Mancha 761'}
            ],
            'Argumento usado: [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, "Mirasol '
            '218"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761")]': [
                domicilios_facturacion([("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
                                        ("Jorge Russo", 7, 699, "Mirasol 218"),
                                        ("Julián Rodriguez", 12, 5715.99, "La Mancha 761")]),
                {'Calle Las Flores 355', 'Mirasol 218', 'La Mancha 761'}
            ],
            'Argumento usado: [("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Nuria Costa", 5, 12780.78, '
            '"Calle Las Flores 355"), ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355")]': [
                domicilios_facturacion([("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
                                        ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
                                        ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355")]),
                {'Calle Las Flores 355'}
            ],
            'Argumento usado: []': [
                domicilios_facturacion([]),
                set()
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_agregar_pelicula(self):
        pruebas = {
            'Argumentos usados: {"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]}, ("Lord of the '
            'rings: The two towers", "Peter Jackson", 2002)': [
                agregar_pelicula({"Joker": ["Todd Phillips", 2019],
                                  "Avatar": ["James Cameron", 2009]},
                                 ("Lord of the rings: The two towers", "Peter Jackson", 2002)),
                {"Joker": ["Todd Phillips", 2019],
                 "Avatar": ["James Cameron", 2009],
                 "Lord of the rings: The two towers": ["Peter Jackson", 2002]}
            ],
            'Argumentos usados: {}, ("Lord of the rings: The two towers", "Peter Jackson", 2002)': [
                agregar_pelicula({}, ("Lord of the rings: The two towers", "Peter Jackson", 2002)),
                {"Lord of the rings: The two towers": ["Peter Jackson", 2002]}
            ],
            'Argumentos usados: {"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]}, ("Avatar", '
            '"James Cameron", 2009)': [
                agregar_pelicula({"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]},
                                 ("Avatar", "James Cameron", 2009)),
                {"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]}
            ],
            'Argumentos usados: {"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]}, ()': [
                agregar_pelicula({"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]}, ()),
                {"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]}
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_mas_votados(self):
        pruebas = {
            'Argumentos usados: {1:["juan","juan","lorena","juan","lorena","paula"], 2:["romina","marcos","guadalupe"'
            ',"guadalupe"], 3:["lucas","abril","lucas","abril","abril","serena","abril"]}, 3': [
                mas_votados({1: ["juan", "juan", "lorena", "juan", "lorena", "paula"],
                             2: ["romina", "marcos", "guadalupe", "guadalupe"],
                             3: ["lucas", "abril", "lucas", "abril", "abril", "serena", "abril"]},
                            3),
                {"lucas", "abril", "serena"}
            ],
            'Argumentos usados: {1:["juan","lorena","paula"], 2:["romina", "marcos","guadalupe","guadalupe"], 3:['
            '"lucas","abril","lucas","abril","abril","serena","abril"]}, 1': [
                mas_votados({1: ["juan", "lorena", "paula"],
                             2: ["romina", "marcos", "guadalupe", "guadalupe"],
                             3: ["lucas", "abril", "lucas", "abril", "abril", "serena", "abril"]},
                            1),
                {"juan", "lorena", "paula"}
            ],
            'Argumentos usados: {1:["lorena","lorena","lorena","lorena"], 2:["romina", "marcos","guadalupe","guadalupe'
            '"], 3:["lucas","abril","lucas","abril","abril","serena","abril"]}, 1': [
                mas_votados({1: ["lorena", "lorena", "lorena", "lorena"],
                             2: ["romina", "marcos", "guadalupe", "guadalupe"],
                             3: ["lucas", "abril", "lucas", "abril", "abril", "serena", "abril"]},
                            1),
                {"lorena"}
            ],
            'Argumentos usados: {1:["juan","juan","lorena","juan","lorena","paula"], 2:["romina", "marcos","guadalupe"'
            ',"guadalupe"], 3:["lucas","abril","lucas","abril","abril","serena","abril"]}, 4': [
                mas_votados({1: ["juan", "juan", "lorena", "juan", "lorena", "paula"],
                             2: ["romina", "marcos", "guadalupe", "guadalupe"],
                             3: ["lucas", "abril", "lucas", "abril", "abril", "serena", "abril"]},
                            4),
                set()
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_ocurrencias_digitos(self):
        pruebas = {
            'Argumento usado: [8, 9, 0, 4, 2, 2, 4, 1, 8, 2]': [
                ocurrencias_digitos([8, 9, 0, 4, 2, 2, 4, 1, 8, 2]),
                {0: 1, 1: 1, 2: 3, 3: 0, 4: 2, 5: 0, 6: 0, 7: 0, 8: 2, 9: 1}
            ],
            'Argumento usado: [0, 0, 0, 0, 0, 0]': [
                ocurrencias_digitos([0, 0, 0, 0, 0, 0]),
                {0: 6, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            ],
            'Argumento usado: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]': [
                ocurrencias_digitos([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
                {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
            ],
            'Argumento usado: []': [
                ocurrencias_digitos([]),
                {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_contar_ocurrencias(self):
        pruebas = {
            'Argumento usado: (["i", "%", "u"], ["^", "%", "^", "s", "i", "i", "u"], ["a", "u"])': [
                contar_ocurrencias((["i", "%", "u"], ["^", "%", "^", "s", "i", "i", "u"], ["a", "u"])),
                {'i': 3, '%': 2, 'u': 3, 's': 1, '^': 2, 'a': 1}
            ],
            'Argumento usado: (["i", "%", "u", "^", "%", "^", "s", "i", "i", "u", "a", "u"])': [
                contar_ocurrencias((["i", "%", "u", "^", "%", "^", "s", "i", "i", "u", "a", "u"])),
                {'i': 3, '%': 2, 'u': 3, 's': 1, '^': 2, 'a': 1}
            ],
            'Argumento usado: (["i", "%", "u"], ["i", "%", "u"], ["i", "%", "u"])': [
                contar_ocurrencias((["i", "%", "u"], ["i", "%", "u"], ["i", "%", "u"])),
                {'i': 3, '%': 3, 'u': 3}
            ],
            'Argumento usado: (["i", "i", "i"], ["i", "i", "i"], ["i", "i", "i"], ["i", "i", "i"])': [
                contar_ocurrencias((["i", "i", "i"], ["i", "i", "i"], ["i", "i", "i"], ["i", "i", "i"])),
                {'i': 12}
            ],
            'Argumento usado: ([], [], [], [], [])': [
                contar_ocurrencias(([], [], [], [], [])),
                {}
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_mayor_valor(self):
        pruebas = {
            'Argumentos usados: {"a":1, "e":7, "i":4, "o":9, "u":3}': [
                mayor_valor({"a": 1, "e": 7, "i": 4, "o": 9, "u": 3}),
                "o"
            ],
            'Argumentos usados: {"z":198}': [
                mayor_valor({"z": 198}),
                "z"
            ],
            'Argumentos usados: {}': [
                mayor_valor({}),
                ""
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_epoca_de_siembra(self):
        pruebas = {
            'Argumentos usados: {"espinaca":["febrero","marzo"], "ajo":["febrero","marzo","abril"], "berenjena":'
            '["julio","agosto","septiembre"]}, "marzo"': [
                epoca_de_siembra({"espinaca": ["febrero", "marzo"],
                                  "ajo": ["febrero", "marzo", "abril"],
                                  "berenjena": ["julio", "agosto", "septiembre"]},
                                 "marzo"),
                ["espinaca", "ajo"]
            ],
            'Argumentos usados: {"espinaca":["febrero","marzo"], "ajo":["febrero","marzo","abril"], "berenjena":'
            '["julio","agosto","septiembre"]}, "diciembre"': [
                epoca_de_siembra({"espinaca": ["febrero", "marzo"],
                                  "ajo": ["febrero", "marzo", "abril"],
                                  "berenjena": ["julio", "agosto", "septiembre"]},
                                 "diciembre"),
                []
            ],
            'Argumentos usados: {"espinaca":["febrero","marzo"], "ajo":["febrero","marzo","abril"], "berenjena":'
            '["julio","agosto","septiembre"]}, "agosto"': [
                epoca_de_siembra({"espinaca": ["febrero", "marzo"],
                                  "ajo": ["febrero", "marzo", "abril"],
                                  "berenjena": ["julio", "agosto", "septiembre"]},
                                 "agosto"),
                ['berenjena']
            ],
            'Argumentos usados: ({}, "marzo")': [
                epoca_de_siembra({}, "marzo"),
                []
            ],
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_asentar_pago(self):
        pruebas = {
            'Argumentos usados: {423:["Juana Saavedra", 4523114, True], 289:["Estela Gimenez", 6345112, False], 657:'
            '["Lautaro Ruiz", 4767992, False]}, 289': [
                asentar_pago({423: ["Juana Saavedra", 4523114, True],
                              289: ["Estela Gimenez", 6345112, False],
                              657: ["Lautaro Ruiz", 4767992, False]},
                             289),
                {423: ["Juana Saavedra", 4523114, True],
                 289: ["Estela Gimenez", 6345112, True],
                 657: ["Lautaro Ruiz", 4767992, False]}
            ],
            'Argumentos usados: {423:["Juana Saavedra", 4523114, True], 289:["Estela Gimenez", 6345112, False], 657:'
            '["Lautaro Ruiz", 4767992, False]}, 423': [
                asentar_pago({423: ["Juana Saavedra", 4523114, True],
                              289: ["Estela Gimenez", 6345112, False],
                              657: ["Lautaro Ruiz", 4767992, False]},
                             423),
                {423: ["Juana Saavedra", 4523114, True],
                 289: ["Estela Gimenez", 6345112, False],
                 657: ["Lautaro Ruiz", 4767992, False]}
            ],
            'Argumentos usados: {423:["Juana Saavedra", 4523114, True], 289:["Estela Gimenez", 6345112, False], 657:'
            '["Lautaro Ruiz", 4767992, False]}, 158': [
                asentar_pago({423: ["Juana Saavedra", 4523114, True],
                              289: ["Estela Gimenez", 6345112, False],
                              657: ["Lautaro Ruiz", 4767992, False]},
                             158),
                {423: ["Juana Saavedra", 4523114, True],
                 289: ["Estela Gimenez", 6345112, False],
                 657: ["Lautaro Ruiz", 4767992, False]}
            ],
            'Argumentos usados: {}, 289': [
                asentar_pago({}, 289),
                {}
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_socios_morosos(self):
        pruebas = {
            'Argumento usado: {423:["Juana Saavedra", 4523114, True], 289:["Estela Gimenez", 6345112, False], 657:'
            '["Lautaro Ruiz", 4767992, False]}': [
                socios_morosos({423: ["Juana Saavedra", 4523114, True],
                                289: ["Estela Gimenez", 6345112, False],
                                657: ["Lautaro Ruiz", 4767992, False]}),
                2
            ],
            'Argumento usado: {423:["Juana Saavedra", 4523114, False], 289:["Estela Gimenez", 6345112, False], 657:'
            '["Lautaro Ruiz", 4767992, False]}': [
                socios_morosos({423: ["Juana Saavedra", 4523114, False],
                                289: ["Estela Gimenez", 6345112, False],
                                657: ["Lautaro Ruiz", 4767992, False]}),
                3
            ],
            'Argumento usado: {423:["Juana Saavedra", 4523114, True], 289:["Estela Gimenez", 6345112, True], 657:'
            '["Lautaro Ruiz", 4767992, True]}': [
                socios_morosos({423: ["Juana Saavedra", 4523114, True],
                                289: ["Estela Gimenez", 6345112, True],
                                657: ["Lautaro Ruiz", 4767992, True]}),
                0
            ],
            'Argumento usado: {}': [
                socios_morosos({}),
                0
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_eliminar_socio(self):
        pruebas = {
            'Argumentos usados: {423:["Juana Saavedra", 4523114, True], 289:["Estela Gimenez", 6345112, False], 657:'
            '["Lautaro Ruiz", 4767992, False]}, "Estela Gimenez"': [
                eliminar_socio({423: ["Juana Saavedra", 4523114, True],
                                289: ["Estela Gimenez", 6345112, False],
                                657: ["Lautaro Ruiz", 4767992, False]}, "Estela Gimenez"),
                {423: ["Juana Saavedra", 4523114, True],
                 657: ["Lautaro Ruiz", 4767992, False]}
            ],
            'Argumento usado: {423:["Juana Saavedra", 4523114, True], 289:["Estela Gimenez", 6345112, False], 657:'
            '["Lautaro Ruiz", 4767992, False]}, "Lucia Perez': [
                eliminar_socio({423: ["Juana Saavedra", 4523114, True],
                                289: ["Estela Gimenez", 6345112, False],
                                657: ["Lautaro Ruiz", 4767992, False]}, "Lucia Perez"),
                {423: ["Juana Saavedra", 4523114, True],
                 289: ["Estela Gimenez", 6345112, False],
                 657: ["Lautaro Ruiz", 4767992, False]}
            ],
            'Argumento usado: {}, "Estela Gimenez"': [
                eliminar_socio({}, "Estela Gimenez"),
                {}
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_romano_a_arabigo(self):
        pruebas = {
            'Argumento usado: MCMLXXIV': [
                romano_a_arabigo("MCMLXXIV"),
                1974
            ],
            'Argumento usado: I': [
                romano_a_arabigo("I"),
                1
            ],
            'Argumento usado: V': [
                romano_a_arabigo("V"),
                5
            ],
            'Argumento usado: X': [
                romano_a_arabigo("X"),
                10
            ],
            'Argumento usado: L': [
                romano_a_arabigo("L"),
                50
            ],
            'Argumento usado: C': [
                romano_a_arabigo("C"),
                100
            ],
            'Argumento usado: D': [
                romano_a_arabigo("D"),
                500
            ],
            'Argumento usado: M': [
                romano_a_arabigo("M"),
                1000
            ],
            'Argumento usado: MMMCMXCIX': [
                romano_a_arabigo("MMMCMXCIX"),
                3999
            ],
            'Argumento usado: III': [
                romano_a_arabigo("III"),
                3
            ],
            'Argumento usado: IV': [
                romano_a_arabigo("IV"),
                4
            ],
            'Argumento usado: IX': [
                romano_a_arabigo("IX"),
                9
            ],
            'Argumento usado: XL': [
                romano_a_arabigo("XL"),
                40
            ],
            'Argumento usado: XC': [
                romano_a_arabigo("XC"),
                90
            ],
            'Argumento usado: CD': [
                romano_a_arabigo("CD"),
                400
            ],
            'Argumento usado: CM': [
                romano_a_arabigo("CM"),
                900
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_numero_telefonico(self):
        pruebas = {
            'Argumento usado: "(325)444-TEST"': [
                numero_telefonico("(325)444-TEST"),
                "(325)444-8378"
            ],
            'Argumento usado: "435-224-7613"': [
                numero_telefonico("(325)444-TEST"),
                "(325)444-8378"
            ],
            'Argumento usado: "54212456"': [
                numero_telefonico("54212456"),
                "54212456"
            ],
            'Argumento usado: "0800-TEST"': [
                numero_telefonico("0800-TEST"),
                "0800-8378"
            ],
            'Argumento usado: "ABCDEFGHIJKLMNOPQRSTUVWXYZ"': [
                numero_telefonico("ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
                "22233344455566677778889999"
            ],
            'Argumento usado: "(325)444TEST"': [
                numero_telefonico("(325)444TEST"),
                "(325)4448378"
            ],
            'Argumento usado: "(325)444-8378"': [
                numero_telefonico("(325)444-8378"),
                "(325)444-8378"
            ],
            'Argumento usado: "(TEST)444-12345"': [
                numero_telefonico("(TEST)444-12345"),
                "(8378)444-12345"
            ],
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_cadenas_isomorficas(self):
        pruebas = {
            'Argumentos usados: "papel", "vivaz"': [
                cadenas_isomorficas("papel", "vivaz"),
                True
            ],
            'Argumentos usados: "papel", "yoyos"': [
                cadenas_isomorficas("papel", "yoyos"),
                False
            ],
            'Argumentos usados: "abcd", "efgh"': [
                cadenas_isomorficas("abcd", "efgh"),
                True
            ],
            'Argumentos usados: "aaa", "bbb"': [
                cadenas_isomorficas("aaa", "bbb"),
                True
            ],
            'Argumentos usados: "abb", "baa"': [
                cadenas_isomorficas("abb", "baa"),
                True
            ],
            'Argumentos usados: "badc", "baba"': [
                cadenas_isomorficas("badc", "baba"),
                False
            ],
            'Argumentos usados: "z", "z"': [
                cadenas_isomorficas("z", "z"),
                True
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)
