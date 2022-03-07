##################################
#         TEMA: STRINGS          #
##################################


def cantidad_par_caracteres(cadena1, cadena2):
    """
    Indica si la cantidad de caracteres de ambas cadenas es par o no.
    Ejemplos:
        cantidad_par_caracteres("aaaa", "aaaa") -> True
        cantidad_par_caracteres("aaa", "aaaa") -> False
    -Parámetros:
        cadena1 (str): uno de los strings a procesar.
        cadena2 (str): otro de los strings a procesar.
    -Valor retornado:
        (bool) True si la cantidad de caracteres de cadena1 y la cantidad de caracteres de cadena2 son, ambas, números
        pares. False si al menos una de las dos cadenas tiene una cantidad impar de caracteres.
    """
    pass


def contar_ocurrencias(cadena, caracter):
    """
    Cuenta la cantidad de veces que un carácter aparece en una cadena.
    Sugerencia: evitar el método count().
    Ejemplo:
        contar_ocurrencias("Esto es una frase", "s") -> 3
    -Parámetros:
        cadena (str): string donde contar ocurrencias de un carácter.
        caracter (str): el carácter a contabilizar.
    -Valor retornado:
        (int) Cantidad de ocurrencias de caracter en cadena.
    """
    pass


def contar_vocales_totales(cadena):
    """
    Cuenta la cantidad de vocales (incluyendo repeticiones) que hay en una cadena, teniendo en cuenta mayúsculas como
    minúsculas. Las vocales del idioma español son: a, e, i, o, u.
    Sugerencia: evitar el método count().
    Ejemplo:
        contar_vocales_totales("Esto es una frase") -> 7
    -Parámetro:
        cadena (str): string en el cual se contarán las vocales.
    -Valor retornado:
        (int) Cantidad total de vocales en cadena.
    """
    pass


def contar_vocales_unicas(cadena):
    """
    Cuenta la cantidad de vocales que hay en una cadena.
    Las vocales del idioma español son: a, e, i, o, u.
    Cada vocal debe contarse una única vez, indistintamente en su forma mayúscula o minúscula.
    Sugerencia: evitar el método count().
    Ejemplo:
        contar_vocales_unicas("Esto Es Una Frase") -> 4
    -Parámetro:
        cadena (str): string en el cual se contarán las vocales.
    -Valor retornado:
        (int) Cantidad de vocales únicas en cadena.
    """
    pass


def reemplazar_caracter_con_asterisco(cadena, caracter):
    """
    Reemplaza por '*' a todas las ocurrencias del carácter indicado.
    Sugerencia: evitar el método replace().
    Ejemplos:
        reemplazar_caracter_con_asterisco("esto es una frase", "a") -> "esto es un* fr*se"
    -Parámetros:
        cadena (str): el string donde se harán los reemplazos.
        caracter (str): el carácter a reemplazar.
    -Valor retornado:
        (str) Un nuevo string con el contenido de cadena, donde todas las ocurrencias de caracter fueron reemplazadas
        por '*'.
    """
    pass


def invertir_cadena(cadena):
    """
    Invierte el orden de los caracteres de la cadena.
    Sugerencia: evitar usar rebanadas con paso negativo.
    Ejemplo:
        invertir_cadena("Esto es una frase!") -> "!esarf anu se otsE"
    Parámetro:
        cadena (str): string a invertir.
    -Valor retornado:
        (str) Un nuevo string con los caracteres de cadena en el orden inverso.
    """
    pass


def reemplazar_simbolos(cadena, nuevo_caracter):
    """
    Reemplaza todos los símbolos de la cadena por el carácter dado.
    Se consideran símbolos a los caracteres que no son letras, dígitos ni espacios.
    Ejemplo:
        reemplazar_simbolos("--Esto es 1 frase donde reemplazaremos con @ cada símbolo", "@") 
        -> "@@Esto es 1 frase donde reemplazaremos con @ cada símbolo"
    -Parámetros:
        cadena (str): string donde se efectuarán los reemplazos.
    -Valor retornado:
        (str) Un string donde cada símbolo ha sido reemplazado por nuevo_caracter.
    """
    pass


def porcentaje_digitos_numericos(cadena):
    """
    Retorna el porcentaje que representan los dígitos números sobre el total de caracteres de una cadena.
    Solo se retorna el número, sin el símbolo % y sin redondear (en caso de tener decimales).
    Ejemplos:
        porcentaje_digitos_numericos("Tenemos 1 dígito") -> 6.25
        porcentaje_digitos_numericos("1984") -> 100
    -Parámetro:
        cadena (str): string a procesar, que puede o no contener dígitos numéricos.
    -Valor retornado:
        (numérico) Porcentaje (número entre 0 y 100) de caracteres numéricos que posee la cadena, sobre su cantidad
        total de caracteres.
    """
    pass


def clasificar_cadena_numerica(cadena):
    """
    Recibe un número en forma de string y retorna un nuevo string, conteniendo los caracteres que representan dígitos
    múltiplos de 2 y dígitos múltiplos de 3, ambos grupos separados por un '$'. Si un dígito es múltiplo de 2 y de 3
    al mismo tiempo, aparecerá a ambos lados del símbolo '$'.
    Ejemplo:
        clasificar_cadena_numerica("123456") -> "246$36"
        clasificar_cadena_numerica("2222") -> "2222$"
    -Parámetro:
        cadena (str): string numérico a procesar. El string solo contendrá dígitos numéricos.
    -Valor retornado:
        (str) String compuesto por la concatenación de los caracteres de la cadena que son múltiplos de 2 (en su
        representación numérica), seguidos de un '$' a continuación, seguidos de  la concatenación de los caracteres de
        la cadena que son múltiplos de 3.
    """
    pass


def caracteres_centrales(cadena):
    """
    Dada una cadena, retorna los 3 caracteres centrales.
    Ejemplos:
        caracteres_centrales("AbcDefGhi") -> "Def"
        caracteres_centrales("A   A") -> "   "
    -Parámetro:
        cadena (str) string a procesar. La cadena tendrá 5 o más caracteres y su longitud será impar.
    -Valor retornado:
        (str) String de longitud 3 conteniendo los caracteres ubicados en el medio de la cadena pasada por parámetro.
    """    
    pass


def es_palindromo(cadena):
    """
    Verifica si una cadena es palíndromo, independientemente de mayúsculas y minúsculas.
    Se incluyen todos los caracteres, sean o no letras.
    Las letras acentuadas se consideran como caracteres diferentes de sus contrapartes no acentuadas.
    La cadena vacía no se considera palíndromo.
    Sugerencia: evitar las rebanadas con paso negativo y la función reversed().
    Ejemplos:
        es_palindromo("abba") -> True
        es_palindromo("baéceab") -> False
    -Parámetro:
        cadena (str): el string a procesar.
    -Valor retornado:
        (bool) True si la cadena es palíndromo. False si no lo es.
    """
    pass


def incluye_caracteres(cadena1, cadena2):
    """
    Indica si cadena2 incluye todos los caracteres que componen a cadena1.
    El orden de los caracteres no se tiene en cuenta.
    Se considera a la versión mayúscula y minúscula de una misma letra como caracteres diferentes.
    cadena1 puede contener caracteres repetidos y, en ese caso, cuentan como un único carácter a buscar en cadena2.
    Ejemplos:
        incluye_caracteres("super", "supermercado") -> True       
        incluye_caracteres("aaa", "rosa") -> True
    -Parámetros:
        cadena1 (str): el string cuyos caracteres deben buscarse en cadena2.
        cadena2 (str): el string donde se buscarán los caracteres de cadena1.
    -Valor retornado:
        (bool) True si cadena2 incluye todos los caracteres de cadena1. False si no incluye a todos.
    """
    pass


def son_anagrama(cadena1, cadena2):
    """
    Indica si cadena1 es un anagrama de cadena2.
    No se tienen en cuenta mayúsculas y minúsculas pero sí las repeticiones de letras.
    Los strings a comparar solo contendrán letras.
    Ejemplos:
        son_anagrama("aval", "lava") -> True
        son_anagrama("aval", "lavar") -> False
    -Parámetros:
        cadena1 (str): un string a procesar, para saber si es anagrama de cadena2.
        cadena2 (str): un string a procesar, para saber si es anagrama de cadena1.
    -Valor retornado:
        (bool) True si son anagramas. False si no lo son.
    """
    pass


def cuantos_eliminar_para_anagrama(cadena1, cadena2):
    """
    Indica cuántos caracteres deben eliminarse para que cadena1 y cadena2 sean anagramas.
    No se tienen en cuenta mayúsculas y minúsculas pero sí las repeticiones de letras.
    Los strings a comparar solo contendrán letras.
    Ejemplo:
        cuantos_eliminar_para_anagrama("avala", "lavar") -> 2
    -Parámetros:
        cadena1 (str): uno de los strings a procesar.
        cadena2 (str): otro string a procesar.
    -Valor retornado:
        (int) Cantidad de caracteres que deberían eliminarse para que ambas cadenas sean anagramas.
    """
    pass


def invertir_palabras(cadena):
    """
    Invierte los caracteres de cada palabra en una cadena.
    Separador de palabras: un único espacio.
    La cadena no contendrá espacios al principio ni al final. Puede contener símbolos o dígitos y en ese caso se
    considerarán de la misma forma que las letras.
    Sugerencia: evitar usar el método split().
    Ejemplo:
        invertir_palabras("Esto es una frase.") -> "otsE se anu .esarf"
    -Parámetros:
        cadena (str): string formado por palabras que serán invertidas.
    -Valor retornado:
        (str) Un nuevo string donde cada palabra se encuentra invertida, sin modificar su posición original dentro de
        la cadena.
    """
    pass


def longitud_ultima_palabra(cadena):
    """
    Retorna la longitud de la última palabra de una cadena.
    Separador de palabras: uno o más espacios.
    Ejemplos:
        longitud_ultima_palabra("esto es una frase") -> 5
        longitud_ultima_palabra("   espacios   ") -> 8
    -Parámetro:
        cadena (str): string compuesto por letras y espacios.
    -Valor retornado:
        (int) Cantidad de caracteres de la última palabra de la cadena.
    """
    pass


def convertir_a_titulo(cadena):
    """
    Convierte la primera letra de cada palabra a mayúsculas y el resto a minúsculas.
    Separador de palabras: cualquier símbolo (excluyendo letras y números), excepto apóstrofos.
    No debe modificarse la cantidad de espacios.
    Sugerencia: evitar usar el método title().
    Ejemplos:
        convertir_a_titulo("esto es una frase") -> "Esto Es Una Frase"
        convertir_a_titulo("ESTO ES UNA FRASE") -> "Esto Es Una Frase"
    -Parámetro:
        cadena (str): string a convertir.
    -Valor retornado:
        (str) Un nuevo string con el contenido de cadena, donde la primera letra de cada palabra es mayúscula y el
        resto son minúsculas.
    """
    pass


def cifrar_cesar(cadena, n):
    """
    Reemplaza cada letra de la cadena por otra del alfabeto, que se encuentre n posiciones hacia la derecha.
    Los corrimientos son circulares (si el alfabeto termina antes de poder correr la cantidad de lugares necesarios,
    se vuelve a comenzar desde la letra “a”).
    La cadena puede contener letras minúsculas, símbolos y dígitos. El cifrado solo se realizará sobre las letras,
    dejando al resto de caracteres sin modificación.
    La cantidad de corrimientos (n) será un número entre 1 y 27.
    Ejemplos:
        cifrar_cesar("esto es una frase", 2) -> "guvq gu woc htcug"
        cifrar_cesar("abc123 xyz987!", 4) -> "efg123 bcd987!"
    -Parámetros:
        cadena (str): string a cifrar.
        n (int): cantidad de posiciones que se moverá cada carácter dentro del alfabeto español de 27 letras.
    -Valor retornado:
        (str) Un nuevo string donde cada letra ha sido reemplazado por otra del alfabeto, ubicada n posiciones hacia la
        derecha.
    """
    pass


def rotar_n_posiciones(cadena, n):
    """
    Dada una cadena, rota cada carácter n posiciones a la derecha, en forma circular (volviendo al principio al llegar
    al final).
    Los caracteres pueden ser letras, dígitos o símbolos.
    n no está necesariamente limitado a la longitud de cadena.
    Ejemplos:
        rotar_n_posiciones("Esto es una frase", 6) -> " fraseEsto es una"
        rotar_n_posiciones("palabra", 3) -> "brapala"
    -Parámetros:
        cadena (str): string a partir del cual se producirán las rotaciones.
        n (int): cantidad de posiciones que se moverá cada carácter dentro del string.
    -Valor retornado:
        (str) Un nuevo string donde cada carácter se ha desplazado n posiciones hacia la derecha.
    """
    pass


def comprimir_RLE(cadena):
    """
    Comprime un string utilizando la codificación RLE ("Run-Length Encoding").
    RLE: por cada grupo de caracteres consecutivos repetidos, se almacenará una única ocurrencia del carácter,
    seguida del número de ocurrencias en caso de que sea mayor que 1 (ejemplo: 'aaab' se comprime como 'a3b').
    La cadena solo estará compuesta por letras y/o símbolos.
    Ejemplos:
        comprimir_RLE("aaabbc") -> "a3b2c"
        comprimir_RLE("abcde") -> "abcde"
    -Parámetro:
        cadena (str): string a comprimir.
    -Valor retornado:
        (str) String comprimido mediante RLE.
    """
    pass
