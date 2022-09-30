#############################
# NO MODIFICAR ESTE ARCHIVO #
#############################

import unittest
from ESP.src.diccionarios import *


class TestsFuncionesDiccionarios(unittest.TestCase):

    def test_hallar_repetidos(self):
        pruebas = {
            'Argumentos usados: strings1=["abc", "cde", "abc", "fff"], strings2=["cde", "aaa"]': [
                hallar_repetidos(strings1=["abc", "cde", "abc", "fff"], strings2=["cde", "aaa"]),
                {"cde"}
            ],
            'Argumentos usados: strings1=["abc", "cde", "fgh", "ijk"], strings2=["fgh", "abc"]': [
                hallar_repetidos(strings1=["abc", "cde", "fgh", "ijk"], strings2=["fgh", "abc"]),
                {"abc", "fgh"}
            ],
            'Argumentos usados: strings1=["abc", "cde"], strings2=["fgh", "ijk"]': [
                hallar_repetidos(strings1=["abc", "cde"], strings2=["fgh", "ijk"]),
                set()
            ],
            'Argumentos usados: strings1=["abc"], strings2=["abc"]': [
                hallar_repetidos(strings1=["abc"], strings2=["abc"]),
                {"abc"}
            ],
            'Argumentos usados: strings1=[], strings2=[]': [
                hallar_repetidos(strings1=[], strings2=[]),
                set()
            ],
            'Argumentos usados: strings1=["abc", "cde", "abc", "fff"], strings2=[]': [
                hallar_repetidos(strings1=["abc", "cde", "abc", "fff"], strings2=[]),
                set()
            ],
            'Argumentos usados: strings1=[], strings2=["abc", "cde", "abc", "fff"]': [
                hallar_repetidos(strings1=[], strings2=["abc", "cde", "abc", "fff"]),
                set()
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_solo_una_mascota(self):
        pruebas = {
            'Argumentos usados: perros=["Lucrecia Borges", "Juan Sebastián Balsa", "Cristóbal Colombraro"], '
            'gatos=["Juan Sebastián Balsa", "Juan Jacobo Russo", "Ana Bologna", "Cristóbal Colombraro"]': [
                solo_una_mascota(perros=["Lucrecia Borges", "Juan Sebastián Balsa", "Cristóbal Colombraro"],
                                 gatos=["Juan Sebastián Balsa", "Juan Jacobo Russo", "Ana Bologna",
                                        "Cristóbal Colombraro"]),
                {"Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"}
            ],
            'Argumentos usados: perros=["Lucrecia Borges", "Juan Sebastián Balsa", "Cristóbal Colombraro"], '
            'gatos=["Juan Jacobo Russo", "Ana Bologna"]': [
                solo_una_mascota(perros=["Lucrecia Borges", "Juan Sebastián Balsa", "Cristóbal Colombraro"],
                                 gatos=["Juan Jacobo Russo", "Ana Bologna"]),
                {"Lucrecia Borges", "Juan Sebastián Balsa", "Cristóbal Colombraro", "Juan Jacobo Russo", "Ana Bologna"}
            ],
            'Argumentos usados: perros=["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"], '
            'gatos=["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"]': [
                solo_una_mascota(perros=["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"],
                                 gatos=["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"]),
                set()
            ],
            'Argumentos usados: perros=["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"], '
            'gatos=["Lucrecia Borges", "Juan Jacobo Russo"]': [
                solo_una_mascota(perros=["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"],
                                 gatos=["Lucrecia Borges", "Juan Jacobo Russo"]),
                {"Ana Bologna"}
            ],
            'Argumentos usados: perros=["Lucrecia Borges", "Juan Jacobo Russo"], gatos=["Lucrecia Borges", '
            '"Juan Jacobo Russo", "Ana Bologna"]': [
                solo_una_mascota(perros=["Lucrecia Borges", "Juan Jacobo Russo"],
                                 gatos=["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"]),
                {"Ana Bologna"}
            ],
            'Argumentos usados: perros=[], gatos=["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"]': [
                solo_una_mascota(perros=[], gatos=["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"]),
                {"Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"}
            ],
            'Argumentos usados: perros=["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"], gatos=[]': [
                solo_una_mascota(perros=["Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"], gatos=[]),
                {"Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"}
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_elementos_unicos(self):
        pruebas = {
            'Argumento usado: tuplas=[(1,2,3), (2,2,2,2), (3,4,5), (1,3,5,7,9)]': [
                elementos_unicos(tuplas=[(1, 2, 3), (2, 2, 2, 2), (3, 4, 5), (1, 3, 5, 7, 9)]),
                (1, 2, 3, 4, 5, 7, 9)
            ],
            'Argumento usado: tuplas=[(1,2,3), (1,2,3), (1,2,3)]': [
                elementos_unicos(tuplas=[(1, 2, 3), (1, 2, 3), (1, 2, 3)]),
                (1, 2, 3)
            ],
            'Argumento usado: tuplas=[(1,2,3)]': [
                elementos_unicos(tuplas=[(1, 2, 3)]),
                (1, 2, 3)
            ],
            'Argumento usado: tuplas=[(1,2,3), (4,5,6), (7,8,9)]': [
                elementos_unicos(tuplas=[(1, 2, 3), (4, 5, 6), (7, 8, 9)]),
                (1, 2, 3, 4, 5, 6, 7, 8, 9)
            ],
            'Argumento usado: tuplas=[(1,1,1), (1,1,1), (1,1,1)]': [
                elementos_unicos(tuplas=[(1, 1, 1), (1, 1, 1), (1, 1, 1)]),
                (1,)
            ],
            'Argumento usado: tuplas=[]': [
                elementos_unicos(tuplas=[]),
                ()
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_listar_apellidos(self):
        pruebas = {
            'Argumento usado: alumnos=["Lara Ruiz", "Esteban Raúl Perez", "Francina Soto", "Lucas Perez"]': [
                listar_apellidos(alumnos=["Lara Ruiz", "Esteban Raúl Perez", "Francina Soto", "Lucas Perez"]),
                {"Ruiz", "Perez", "Soto"}
            ],
            'Argumento usado: alumnos=[]': [
                listar_apellidos(alumnos=[]),
                set()
            ],
            'Argumento usado: alumnos=["Lara Ruiz", "Esteban Raúl Perez", "Francina Soto"]': [
                listar_apellidos(alumnos=["Lara Ruiz", "Esteban Raúl Perez", "Francina Soto"]),
                {"Ruiz", "Perez", "Soto"}
            ],
            'Argumento usado: alumnos=["Lara Ruiz", "Esteban Raúl Ruiz", "Francina Ruiz", "Lucas Ruiz"]': [
                listar_apellidos(alumnos=["Lara Ruiz", "Esteban Raúl Ruiz", "Francina Ruiz", "Lucas Ruiz"]),
                {"Ruiz"}
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_domicilios_facturacion(self):
        pruebas = {
            'Argumento usado: ventas=[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, '
            '"Mirasol 218"), ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"), ("Julián Rodriguez", 12, 5715.99, '
            '"La Mancha 761"), ("Jorge Russo", 15, 958, "Mirasol 218")]': [
                domicilios_facturacion(ventas=[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
                                               ("Jorge Russo", 7, 699, "Mirasol 218"),
                                               ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
                                               ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
                                               ("Jorge Russo", 15, 958, "Mirasol 218")]),
                {'Calle Las Flores 355', 'Mirasol 218', 'La Mancha 761'}
            ],
            'Argumento usado: ventas=[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Jorge Russo", 7, 699, '
            '"Mirasol 218"), ("Julián Rodriguez", 12, 5715.99, "La Mancha 761")]': [
                domicilios_facturacion(ventas=[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
                                               ("Jorge Russo", 7, 699, "Mirasol 218"),
                                               ("Julián Rodriguez", 12, 5715.99, "La Mancha 761")]),
                {'Calle Las Flores 355', 'Mirasol 218', 'La Mancha 761'}
            ],
            'Argumento usado: ventas=[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"), ("Nuria Costa", 5, '
            '12780.78, "Calle Las Flores 355"), ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355")]': [
                domicilios_facturacion(ventas=[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
                                               ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
                                               ("Nuria Costa", 5, 12780.78, "Calle Las Flores 355")]),
                {'Calle Las Flores 355'}
            ],
            'Argumento usado: ventas=[]': [
                domicilios_facturacion(ventas=[]),
                set()
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_agregar_pelicula(self):
        pruebas = {
            'Argumentos usados: peliculas={"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]}, '
            'pelicula=("Lord of the rings: The two towers", "Peter Jackson", 2002)': [
                agregar_pelicula(peliculas={"Joker": ["Todd Phillips", 2019],
                                            "Avatar": ["James Cameron", 2009]},
                                 pelicula=("Lord of the rings: The two towers", "Peter Jackson", 2002)),
                {"Joker": ["Todd Phillips", 2019],
                 "Avatar": ["James Cameron", 2009],
                 "Lord of the rings: The two towers": ["Peter Jackson", 2002]}
            ],
            'Argumentos usados: peliculas={}, pelicula=("Lord of the rings: The two towers", "Peter Jackson", 2002)': [
                agregar_pelicula(peliculas={}, pelicula=("Lord of the rings: The two towers", "Peter Jackson", 2002)),
                {"Lord of the rings: The two towers": ["Peter Jackson", 2002]}
            ],
            'Argumentos usados: peliculas={"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]}, '
            'pelicula=("Avatar", "James Cameron", 2009)': [
                agregar_pelicula(peliculas={"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]},
                                 pelicula=("Avatar", "James Cameron", 2009)),
                {"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]}
            ],
            'Argumentos usados: peliculas={"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]}, '
            'pelicula=()': [
                agregar_pelicula(peliculas={"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]},
                                 pelicula=()),
                {"Joker": ["Todd Phillips", 2019], "Avatar": ["James Cameron", 2009]}
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_mas_votados(self):
        pruebas = {
            'Argumentos usados: votos={1:["juan","juan","lorena","juan","lorena","paula"], 2:["romina","marcos",'
            '"guadalupe","guadalupe"], 3:["lucas","abril","lucas","abril","abril","serena","abril"]}, curso=3': [
                mas_votados(votos={1: ["juan", "juan", "lorena", "juan", "lorena", "paula"],
                                   2: ["romina", "marcos", "guadalupe", "guadalupe"],
                                   3: ["lucas", "abril", "lucas", "abril", "abril", "serena", "abril"]},
                            curso=3),
                {"lucas", "abril", "serena"}
            ],
            'Argumentos usados: votos={1:["juan","lorena","paula"], 2:["romina", "marcos","guadalupe","guadalupe"], 3:['
            '"lucas","abril","lucas","abril","abril","serena","abril"]}, curso=1': [
                mas_votados(votos={1: ["juan", "lorena", "paula"],
                                   2: ["romina", "marcos", "guadalupe", "guadalupe"],
                                   3: ["lucas", "abril", "lucas", "abril", "abril", "serena", "abril"]},
                            curso=1),
                {"juan", "lorena", "paula"}
            ],
            'Argumentos usados: votos={1:["lorena","lorena","lorena","lorena"], 2:["romina", "marcos","guadalupe",'
            '"guadalupe"], 3:["lucas","abril","lucas","abril","abril","serena","abril"]}, curso=1': [
                mas_votados(votos={1: ["lorena", "lorena", "lorena", "lorena"],
                                   2: ["romina", "marcos", "guadalupe", "guadalupe"],
                                   3: ["lucas", "abril", "lucas", "abril", "abril", "serena", "abril"]},
                            curso=1),
                {"lorena"}
            ],
            'Argumentos usados: votos={1:["juan","juan","lorena","juan","lorena","paula"], 2:["romina", "marcos",'
            '"guadalupe","guadalupe"], 3:["lucas","abril","lucas","abril","abril","serena","abril"]}, curso=4': [
                mas_votados(votos={1: ["juan", "juan", "lorena", "juan", "lorena", "paula"],
                                   2: ["romina", "marcos", "guadalupe", "guadalupe"],
                                   3: ["lucas", "abril", "lucas", "abril", "abril", "serena", "abril"]},
                            curso=4),
                set()
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_ocurrencias_digitos(self):
        pruebas = {
            'Argumento usado: digitos=[8, 9, 0, 4, 2, 2, 4, 1, 8, 2]': [
                ocurrencias_digitos(digitos=[8, 9, 0, 4, 2, 2, 4, 1, 8, 2]),
                {0: 1, 1: 1, 2: 3, 3: 0, 4: 2, 5: 0, 6: 0, 7: 0, 8: 2, 9: 1}
            ],
            'Argumento usado: digitos=[0, 0, 0, 0, 0, 0]': [
                ocurrencias_digitos(digitos=[0, 0, 0, 0, 0, 0]),
                {0: 6, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            ],
            'Argumento usado: digitos=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]': [
                ocurrencias_digitos(digitos=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]),
                {0: 1, 1: 1, 2: 1, 3: 1, 4: 1, 5: 1, 6: 1, 7: 1, 8: 1, 9: 1}
            ],
            'Argumento usado: digitos=[]': [
                ocurrencias_digitos(digitos=[]),
                {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_contar_ocurrencias(self):
        pruebas = {
            'Argumento usado: listas=(["i", "%", "u"], ["^", "%", "^", "s", "i", "i", "u"], ["a", "u"])': [
                contar_ocurrencias(listas=(["i", "%", "u"], ["^", "%", "^", "s", "i", "i", "u"], ["a", "u"])),
                {'i': 3, '%': 2, 'u': 3, 's': 1, '^': 2, 'a': 1}
            ],
            'Argumento usado: listas=(["i", "%", "u", "^", "%", "^", "s", "i", "i", "u", "a", "u"])': [
                contar_ocurrencias(listas=(["i", "%", "u", "^", "%", "^", "s", "i", "i", "u", "a", "u"])),
                {'i': 3, '%': 2, 'u': 3, 's': 1, '^': 2, 'a': 1}
            ],
            'Argumento usado: listas=(["i", "%", "u"], ["i", "%", "u"], ["i", "%", "u"])': [
                contar_ocurrencias(listas=(["i", "%", "u"], ["i", "%", "u"], ["i", "%", "u"])),
                {'i': 3, '%': 3, 'u': 3}
            ],
            'Argumento usado: listas=(["i", "i", "i"], ["i", "i", "i"], ["i", "i", "i"], ["i", "i", "i"])': [
                contar_ocurrencias(listas=(["i", "i", "i"], ["i", "i", "i"], ["i", "i", "i"], ["i", "i", "i"])),
                {'i': 12}
            ],
            'Argumento usado: listas=([], [], [], [], [])': [
                contar_ocurrencias(listas=([], [], [], [], [])),
                {}
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_mayor_valor(self):
        pruebas = {
            'Argumentos usados: ocurrencias={"a":1, "e":7, "i":4, "o":9, "u":3}': [
                mayor_valor(ocurrencias={"a": 1, "e": 7, "i": 4, "o": 9, "u": 3}),
                "o"
            ],
            'Argumentos usados: ocurrencias={"z":198}': [
                mayor_valor(ocurrencias={"z": 198}),
                "z"
            ],
            'Argumentos usados: ocurrencias={}': [
                mayor_valor(ocurrencias={}),
                ""
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_epoca_de_siembra(self):
        pruebas = {
            'Argumentos usados: vegetales={"espinaca":["febrero","marzo"], "ajo":["febrero","marzo","abril"], '
            '"berenjena":["julio","agosto","septiembre"]}, mes="marzo"': [
                epoca_de_siembra(vegetales={"espinaca": ["febrero", "marzo"],
                                            "ajo": ["febrero", "marzo", "abril"],
                                            "berenjena": ["julio", "agosto", "septiembre"]},
                                 mes="marzo"),
                ["espinaca", "ajo"]
            ],
            'Argumentos usados: vegetales={"espinaca":["febrero","marzo"], "ajo":["febrero","marzo","abril"], '
            '"berenjena":["julio","agosto","septiembre"]}, mes="diciembre"': [
                epoca_de_siembra(vegetales={"espinaca": ["febrero", "marzo"],
                                            "ajo": ["febrero", "marzo", "abril"],
                                            "berenjena": ["julio", "agosto", "septiembre"]},
                                 mes="diciembre"),
                []
            ],
            'Argumentos usados: vegetales={"espinaca":["febrero","marzo"], "ajo":["febrero","marzo","abril"], '
            '"berenjena":["julio","agosto","septiembre"]}, mes="agosto"': [
                epoca_de_siembra(vegetales={"espinaca": ["febrero", "marzo"],
                                            "ajo": ["febrero", "marzo", "abril"],
                                            "berenjena": ["julio", "agosto", "septiembre"]},
                                 mes="agosto"),
                ['berenjena']
            ],
            'Argumentos usados: (vegetales={}, mes="marzo")': [
                epoca_de_siembra(vegetales={}, mes="marzo"),
                []
            ],
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_asentar_pago(self):
        pruebas = {
            'Argumentos usados: socios={423:["Juana Saavedra", 4523114, True], 289:["Estela Gimenez", 6345112, False], '
            '657:["Lautaro Ruiz", 4767992, False]}, numero=289': [
                asentar_pago(socios={423: ["Juana Saavedra", 4523114, True],
                                     289: ["Estela Gimenez", 6345112, False],
                                     657: ["Lautaro Ruiz", 4767992, False]},
                             numero=289),
                {423: ["Juana Saavedra", 4523114, True],
                 289: ["Estela Gimenez", 6345112, True],
                 657: ["Lautaro Ruiz", 4767992, False]}
            ],
            'Argumentos usados: socios={423:["Juana Saavedra", 4523114, True], 289:["Estela Gimenez", 6345112, False], '
            '657:["Lautaro Ruiz", 4767992, False]}, numero=423': [
                asentar_pago(socios={423: ["Juana Saavedra", 4523114, True],
                                     289: ["Estela Gimenez", 6345112, False],
                                     657: ["Lautaro Ruiz", 4767992, False]},
                             numero=423),
                {423: ["Juana Saavedra", 4523114, True],
                 289: ["Estela Gimenez", 6345112, False],
                 657: ["Lautaro Ruiz", 4767992, False]}
            ],
            'Argumentos usados: socios={423:["Juana Saavedra", 4523114, True], 289:["Estela Gimenez", 6345112, False], '
            '657:["Lautaro Ruiz", 4767992, False]}, numero=158': [
                asentar_pago(socios={423: ["Juana Saavedra", 4523114, True],
                                     289: ["Estela Gimenez", 6345112, False],
                                     657: ["Lautaro Ruiz", 4767992, False]},
                             numero=158),
                {423: ["Juana Saavedra", 4523114, True],
                 289: ["Estela Gimenez", 6345112, False],
                 657: ["Lautaro Ruiz", 4767992, False]}
            ],
            'Argumentos usados: socios={}, numero=289': [
                asentar_pago(socios={}, numero=289),
                {}
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_socios_morosos(self):
        pruebas = {
            'Argumento usado: socios={423:["Juana Saavedra", 4523114, True], 289:["Estela Gimenez", 6345112, False], '
            '657:["Lautaro Ruiz", 4767992, False]}': [
                socios_morosos(socios={423: ["Juana Saavedra", 4523114, True],
                                       289: ["Estela Gimenez", 6345112, False],
                                       657: ["Lautaro Ruiz", 4767992, False]}),
                2
            ],
            'Argumento usado: socios={423:["Juana Saavedra", 4523114, False], 289:["Estela Gimenez", 6345112, False], '
            '657:["Lautaro Ruiz", 4767992, False]}': [
                socios_morosos(socios={423: ["Juana Saavedra", 4523114, False],
                                       289: ["Estela Gimenez", 6345112, False],
                                       657: ["Lautaro Ruiz", 4767992, False]}),
                3
            ],
            'Argumento usado: socios={423:["Juana Saavedra", 4523114, True], 289:["Estela Gimenez", 6345112, True], '
            '657:["Lautaro Ruiz", 4767992, True]}': [
                socios_morosos(socios={423: ["Juana Saavedra", 4523114, True],
                                       289: ["Estela Gimenez", 6345112, True],
                                       657: ["Lautaro Ruiz", 4767992, True]}),
                0
            ],
            'Argumento usado: socios={}': [
                socios_morosos(socios={}),
                0
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_eliminar_socio(self):
        pruebas = {
            'Argumentos usados: socios={423:["Juana Saavedra", 4523114, True], 289:["Estela Gimenez", 6345112, False], '
            '657:["Lautaro Ruiz", 4767992, False]}, nombre_socio="Estela Gimenez"': [
                eliminar_socio(socios={423: ["Juana Saavedra", 4523114, True],
                                       289: ["Estela Gimenez", 6345112, False],
                                       657: ["Lautaro Ruiz", 4767992, False]},
                               nombre_socio="Estela Gimenez"),
                {423: ["Juana Saavedra", 4523114, True],
                 657: ["Lautaro Ruiz", 4767992, False]}
            ],
            'Argumentos usados: socios={423:["Juana Saavedra", 4523114, True], 289:["Estela Gimenez", 6345112, False], '
            '657:["Lautaro Ruiz", 4767992, False]}, nombre_socio="Lucia Perez': [
                eliminar_socio(socios={423: ["Juana Saavedra", 4523114, True],
                                       289: ["Estela Gimenez", 6345112, False],
                                       657: ["Lautaro Ruiz", 4767992, False]},
                               nombre_socio="Lucia Perez"),
                {423: ["Juana Saavedra", 4523114, True],
                 289: ["Estela Gimenez", 6345112, False],
                 657: ["Lautaro Ruiz", 4767992, False]}
            ],
            'Argumentos usados: socios={}, nombre_socio="Estela Gimenez"': [
                eliminar_socio(socios={}, nombre_socio="Estela Gimenez"),
                {}
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_romano_a_arabigo(self):
        pruebas = {
            'Argumento usado: romano="MCMLXXIV"': [
                romano_a_arabigo(romano="MCMLXXIV"),
                1974
            ],
            'Argumento usado: romano="I"': [
                romano_a_arabigo(romano="I"),
                1
            ],
            'Argumento usado: romano="V"': [
                romano_a_arabigo(romano="V"),
                5
            ],
            'Argumento usado: romano="X"': [
                romano_a_arabigo(romano="X"),
                10
            ],
            'Argumento usado: romano="L"': [
                romano_a_arabigo(romano="L"),
                50
            ],
            'Argumento usado: romano="C"': [
                romano_a_arabigo(romano="C"),
                100
            ],
            'Argumento usado: romano="D"': [
                romano_a_arabigo(romano="D"),
                500
            ],
            'Argumento usado: romano="M"': [
                romano_a_arabigo(romano="M"),
                1000
            ],
            'Argumento usado: romano="MMMCMXCIX"': [
                romano_a_arabigo(romano="MMMCMXCIX"),
                3999
            ],
            'Argumento usado: romano="III"': [
                romano_a_arabigo(romano="III"),
                3
            ],
            'Argumento usado: romano="IV"': [
                romano_a_arabigo(romano="IV"),
                4
            ],
            'Argumento usado: romano="IX"': [
                romano_a_arabigo(romano="IX"),
                9
            ],
            'Argumento usado: romano="XL"': [
                romano_a_arabigo(romano="XL"),
                40
            ],
            'Argumento usado: romano="XC"': [
                romano_a_arabigo(romano="XC"),
                90
            ],
            'Argumento usado: romano="CD"': [
                romano_a_arabigo(romano="CD"),
                400
            ],
            'Argumento usado: romano="CM"': [
                romano_a_arabigo(romano="CM"),
                900
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_numero_telefonico(self):
        pruebas = {
            'Argumento usado: telefono="(325)444-TEST"': [
                numero_telefonico(telefono="(325)444-TEST"),
                "(325)444-8378"
            ],
            'Argumento usado: telefono="435-224-7613"': [
                numero_telefonico(telefono="(325)444-TEST"),
                "(325)444-8378"
            ],
            'Argumento usado: telefono="54212456"': [
                numero_telefonico(telefono="54212456"),
                "54212456"
            ],
            'Argumento usado: telefono="0800-TEST"': [
                numero_telefonico(telefono="0800-TEST"),
                "0800-8378"
            ],
            'Argumento usado: telefono="ABCDEFGHIJKLMNOPQRSTUVWXYZ"': [
                numero_telefonico(telefono="ABCDEFGHIJKLMNOPQRSTUVWXYZ"),
                "22233344455566677778889999"
            ],
            'Argumento usado: telefono="(325)444TEST"': [
                numero_telefonico(telefono="(325)444TEST"),
                "(325)4448378"
            ],
            'Argumento usado: telefono="(325)444-8378"': [
                numero_telefonico(telefono="(325)444-8378"),
                "(325)444-8378"
            ],
            'Argumento usado: telefono="(TEST)444-12345"': [
                numero_telefonico(telefono="(TEST)444-12345"),
                "(8378)444-12345"
            ],
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_cadenas_isomorficas(self):
        pruebas = {
            'Argumentos usados: cadena1="papel", cadena2="vivaz"': [
                cadenas_isomorficas(cadena1="papel", cadena2="vivaz"),
                True
            ],
            'Argumentos usados: cadena1="papel", cadena2="yoyos"': [
                cadenas_isomorficas(cadena1="papel", cadena2="yoyos"),
                False
            ],
            'Argumentos usados: cadena1="abcd", cadena2="efgh"': [
                cadenas_isomorficas(cadena1="abcd", cadena2="efgh"),
                True
            ],
            'Argumentos usados: cadena1="aaa", cadena2="bbb"': [
                cadenas_isomorficas(cadena1="aaa", cadena2="bbb"),
                True
            ],
            'Argumentos usados: cadena1="abb", cadena2="baa"': [
                cadenas_isomorficas(cadena1="abb", cadena2="baa"),
                True
            ],
            'Argumentos usados: cadena1="badc", cadena2="baba"': [
                cadenas_isomorficas(cadena1="badc", cadena2="baba"),
                False
            ],
            'Argumentos usados: cadena1="z", cadena2="z"': [
                cadenas_isomorficas(cadena1="z", cadena2="z"),
                True
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)

    def test_patron_de_palabras(self):
        pruebas = {
            'Argumentos usados: patron="xyyx", palabras="casa mar mar casa"': [
                patron_de_palabras(patron="xyyx", palabras="casa mar mar casa"),
                True
            ],
            'Argumentos usados: patron="xyyx", palabras="casa mar mar cerro"': [
                patron_de_palabras(patron="xyyx", palabras="casa mar mar cerro"),
                False
            ],
            'Argumentos usados: patron="xxxxx", palabras="perro"': [
                patron_de_palabras(patron="xxxxx", palabras="perro"),
                False
            ],
            'Argumentos usados: patron="x", palabras="casa casa casa casa"': [
                patron_de_palabras(patron="x", palabras="casa casa casa casa"),
                False
            ],
            'Argumentos usados: patron="xxx", palabras="casa casa casa"': [
                patron_de_palabras(patron="xxx", palabras="casa casa casa"),
                True
            ],
            'Argumentos usados: patron="xy", palabras="casa mar"': [
                patron_de_palabras(patron="xy", palabras="casa mar"),
                True
            ],
            'Argumentos usados: patron="x", palabras="casa"': [
                patron_de_palabras(patron="x", palabras="casa"),
                True
            ],
            'Argumentos usados: patron="", palabras="perro"': [
                patron_de_palabras(patron="", palabras="perro"),
                False
            ],
            'Argumentos usados: patron="xyxy", palabras=""': [
                patron_de_palabras(patron="xyxy", palabras=""),
                False
            ],
            'Argumentos usados: patron="", palabras=""': [
                patron_de_palabras(patron="", palabras=""),
                False
            ]
        }
        for prueba, (a, b) in pruebas.items():
            with self.subTest(prueba=prueba):
                self.assertEqual(a, b, prueba)
