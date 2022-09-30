# Soluciones propuestas

Este archivo contiene posibles soluciones para cada uno de los ejercicios. De ninguna manera esto implica que sean las
únicas soluciones ni tampoco las más eficientes. Es solo información a modo de ejemplo, que podría utilizarse como punto
de partida en caso de no poder resolver alguno de los desafíos.

Seleccionar la categoría del ejercicio y luego dar click sobre la función para que se muestre el código.


* [Números](#numeros)
* [Strings](#strings)
* [Listas y tuplas](#listas-y-tuplas)
* [Conjuntos y diccionarios](#conjuntos-y-diccionarios)


# Numeros

<details>
    <summary>
        <pre>
def menor(numero1, numero2):
    """
    Retorna el menor de dos números.
    Ejemplos:
        menor(numero1=3, numero2=1) -> 1
        menor(numero1=3, numero2=3) -> 3
    -Parámetros:
        numero1 (numérico): uno de los números a procesar.
        numero2 (numérico): otro de los números a procesar.
    -Valor retornado:
        (numérico) El menor de los dos números. numero1 si ambos son iguales.
    """
        </pre>
    </summary>
    <pre>
    if numero1 < numero2 or numero1 == numero2:
        return numero1
    else:
        return numero2
    </pre>
</details>


<details>
    <summary>
        <pre>
def valor_absoluto(numero):
    """
    Retorna el valor absoluto de un número.
    Ejemplos:
        valor_absoluto(numero=3) -> 3
        valor_absoluto(numero=-10) -> 10
    -Parámetro:
        numero (numérico): número cuyo valor absoluto se retornará.
    -Valor retornado:
        (numérico) El valor absoluto de numero.
    """
        </pre>
    </summary>
    <pre>
    if numero < 0:
        return numero * -1
    return numero
    </pre>
</details>


<details>
    <summary>
        <pre>
def buscar_mes(fecha):
    """
    Dada una fecha completa (incluyendo día, mes y año), retorna el mes.
    Ejemplos:
        buscar_mes(fecha=31122020) -> 12
        buscar_mes(fecha=5091946) -> 9
    -Parámetros:
        fecha (int): fecha a procesar, con formato ddmmaaaa o dmmaaaa (donde las "d" indican los dígitos del día,
        las "m" indican los dígitos del mes y las "a" indican los dígitos del año). Positivo.
    -Valor retornado:
        (int) Mes contenido en fecha.
    """
        </pre>
    </summary>
    <pre>
    return (fecha // 10000) % 100
    </pre>
</details>


<details>
    <summary>
        <pre>
def sumar_multiplos(inferior, superior, n):
    """
    Suma los múltiplos de n que se encuentran en un intervalo cerrado de números enteros.
    Ejemplos:
        sumar_multiplos(inferior=0, superior=30, n=5) -> 105
        sumar_multiplos(inferior=-30, superior=0, n=5) -> -105
    -Parámetros:
        inferior (int): límite inferior del intervalo. Menor o igual que superior.
        superior (int): límite superior del intervalo. Mayor o igual que inferior.
        n (int): número cuyos múltiplos se sumarán. Distinto de 0.
    -Valor retornado:
        (int) La suma de los números múltiplos de n que se encuentran entre inferior y superior (inclusive).
    """
        </pre>
    </summary>
    <pre>
    sumatoria = 0
    for numero in range(inferior, superior+1):
        if numero % n == 0:
            sumatoria += numero
    return sumatoria
    </pre>
</details>


<details>
    <summary>
        <pre>
def es_capicua(numero):
    """
    Evalúa si un número es capicúa o no. Los números capicúa son aquellos que se leen de igual manera, tanto de
    izquierda a derecha como de derecha a izquierda.
    Sugerencia: usar números únicamente, evitando otros tipos de datos.
    Ejemplos:
        es_capicua(numero=123321) -> True
        es_capicua(numero=1234) -> False
    -Parámetros:
        numero (int): número a evaluar. Positivo.
    -Valor retornado:
        (bool) True si el número es capicúa, False si no lo es.
    """
        </pre>
    </summary>
    <pre>
    numero_copia = numero
    invertido = 0
    while numero_copia != 0:
        resto = numero_copia % 10
        invertido = (invertido * 10) + resto
        numero_copia //= 10
    return numero == invertido
    </pre>
</details>


<details>
    <summary>
        <pre>
def es_bisiesto(anio):
    """
    Evalúa si un año es bisiesto según el calendario Gregoriano.
    Ejemplos:
        es_bisiesto(anio=2020) -> True
        es_bisiesto(anio=1800) -> False
    -Parámetro:
        anio (int): año a evaluar. Número positivo.
    -Valor retornado:
        (bool) True si el año es bisiesto. False si no lo es.
    """
        </pre>
    </summary>
    <pre>
    if anio % 4 == 0:
        if anio % 100 != 0 or anio % 400 == 0:
            return True
        else:
            return False
    return False
    </pre>
</details>


<details>
    <summary>
        <pre>
def dias_en_mes(mes, anio):
    """
    Calcula la cantidad de días que tiene un mes determinado, en un año determinado (para el caso de que se trate de
    febrero en un año bisiesto).
    Sugerencia: utilizar la función es_bisiesto() desarrollada anteriormente.
    Ejemplo:
        dias_en_mes(mes=11, anio=1981) -> 30
    -Parámetros:
        mes (int): número representando al mes. Entre 1 y 12.
        anio (int): número representando al año. Positivo.
    -Valor retornado:
        (int) Cantidad de días que tiene el mes.
    """
        </pre>
    </summary>
    <pre>
    if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
       return 31
    if mes == 4 or mes == 6 or mes == 9 or mes == 11:
        return 30
    if es_bisiesto(anio=anio):
        return 29
    else:
        return 28
    </pre>
</details>


<details>
    <summary>
        <pre>
def contar_digitos(numero):
    """
    Cuenta la cantidad de dígitos en un número.
    Ejemplo:
        contar_digitos(numero=120) -> 3
    -Parámetro:
        numero (int): número cuyos dígitos se contarán. Positivo.
    -Valor retornado:
        (int) Cantidad de dígitos en numero.
    """
        </pre>
    </summary>
    <pre>
    if numero == 0:
        return 1
    cantidad = 0
    while numero != 0:
        cantidad += 1
        numero //= 10
    return cantidad
    </pre>
</details>


<details>
    <summary>
        <pre>
def suma_digitos_cuadrados(numero):
    """
    Calcula la suma de los cuadrados de cada uno de los dígitos de un número.
    Ejemplo:
        suma_digitos_cuadrados(numero=15) -> 26
    -Parámetro:
        numero (int): número cuyos dígitos se procesarán. Positivo.
    -Valor retornado:
        (int) La suma de los cuadrados de los dígitos de numero.
    """
        </pre>
    </summary>
    <pre>
    suma_cuadrados = 0
    while numero != 0:
        digito = numero % 10
        suma_cuadrados += digito ** 2
        numero = numero // 10
    return suma_cuadrados
    </pre>
</details>


<details>
    <summary>
        <pre>
def porcentaje_digitos_pares(numero):
    """
    Calcula el porcentaje que representan los dígitos pares sobre el total de dígitos de un número.
    Ejemplo:
        porcentaje_digitos_pares(numero=5555666555) -> 30.0
    -Parámetro:
        numero (int): número cuyos dígitos se evaluarán. Positivo.
    -Valor retornado:
        (int) Porcentaje de dígitos pares en numero (de 0 a 100).
    """
        </pre>
    </summary>
    <pre>
    cantidad_total = 0
    cantidad_pares = 0
    while numero != 0:
        cantidad_total += 1
        digito = numero % 10
        if digito % 2 == 0:
            cantidad_pares += 1
        numero //= 10
    if cantidad_total != 0:
        return (cantidad_pares * 100) / cantidad_total
    else:
        return  0.0
    </pre>
</details>


<details>
    <summary>
        <pre>
def es_pronico(numero):
    """
    Evalúa si un número es un número "prónico". Un número es considerado "prónico" si es el producto de
    dos números naturales consecutivos.
    Ejemplo:
        es_pronico(numero=56) -> True
        (56 puede expresarse como 7*8).
    -Parámetro:
        numero (int): número a evaluar. Mayor que 0.
    -Valor retornado:
        (bool) True si numero es prónico, False si no lo es.
    """
        </pre>
    </summary>
    <pre>
    for i in range(numero):
        if i * (i+1) == numero:
            return True
    return False
    </pre>
</details>


<details>
    <summary>
        <pre>
def es_primo(numero):
    """
    Evalúa si un número es primo.
    Ejemplo:
        es_primo(numero=7) -> True
    -Parámetro:
        numero (int): número a evaluar. Positivo.
    -Valor retornado:
        (bool) True si el número es primo. False si no lo es.
    """
        </pre>
    </summary>
    <pre>
    if numero == 0 or numero == 1:
        return False
    for i in range(2, numero):
       if numero % i == 0:           
           return False
    return True
    </pre>
</details>


<details>
    <summary>
        <pre>
def factorial(numero):
    """
    Calcula el factorial de un número.
    Ejemplo:
        factorial(numero=4) -> 24
    -Parámetro:
        numero (int): número cuyo factorial se calculará. Positivo.
    -Valor retornado:
        (int) El factorial de numero.
    """
        </pre>
    </summary>
    <pre>
    resultado = 1
    if numero >= 0:
        for i in range(1, numero+1):
            resultado *= i
    return resultado
    </pre>
</details>


<details>
    <summary>
        <pre>
def suma_primeros_n_fibonacci(n):
    """
    Calcula la sumatoria de los primeros n números de la sucesión de Fibonacci.
    Se considera que los dos primeros números en la sucesión son 0 y 1.
    Ejemplo:
        suma_primeros_n_fibonacci(n=6) -> 12
    -Parámetros:
        n (int): cantidad de números Fibonacci a sumar. Mayor o igual que 2.
    -Valor retornado:
        (int) Sumatoria de los primeros n números de la sucesión de Fibonacci.
    """
        </pre>
    </summary>
    <pre>
    primero = 0
    segundo = 1
    suma = primero + segundo
    for i in range(n-2):
        siguiente = primero + segundo
        suma += siguiente
        primero = segundo
        segundo = siguiente
    return suma
    </pre>
</details>


<details>
    <summary>
        <pre>
def mayor_divisor(numero):
    """
    Calcula el mayor divisor entero de un número, exceptuando al propio número.
    Ejemplo:
        mayor_divisor(numero=182) -> 91
    -Parámetros:
        numero (int): número cuyo mayor divisor se calculará. Positivo.
    -Valor retornado:
        (int) Mayor número que divide a numero sin arrojar resto.
    """
        </pre>
    </summary>
    <pre>
    mayor = 0
    for i in range(1, numero):
        if numero % i == 0:
            if i > mayor:
                mayor = i
    return mayor
    </pre>
</details>


<details>
    <summary>
        <pre>
def mcd_euclides(m, n):
    """
    Calcula el máximo común divisor entre m y n usando el algoritmo de Euclides.
    Método de Euclides: al dividir m por n (números enteros), se obtiene un cociente q y un residuo r. Se ha demostrado
    que el máximo común divisor de m y n es el mismo que el de n y r. n no puede ser 0.
    Ejemplo:
        mcd_euclides(m=60, n=24) -> 12
    -Parámetros:
        m (int): número positivo.
        n (int): número positivo distinto de cero.
    -Valor retornado:
        (int) Mayor divisor común entre m y n.
    """
        </pre>
    </summary>
    <pre>
    while n != 0:
        r = m % n
        m = n
        n = r
    return m
    </pre>
</details>


<details>
    <summary>
        <pre>
def obtener_mes(dia_consecutivo, anio):
    """
    Obtiene el número de mes correspondiente, dada la cantidad de días transcurridos desde el 1 de enero de un año en
    particular (teniendo en cuenta la posibilidad de que sea bisiesto).
    Sugerencia: utilizar la función dias_en_mes() desarrollada anteriormente.
    Ejemplo:
        obtener_mes(dia_consecutivo=200, anio=1969) -> 7
        (el día consecutivo número 60 en un año bisiesto representa el 29 de febrero, mientras que en un año no bisiesto
         representa el 1 de marzo).
    -Parámetros:
        dia_consecutivo (int): número de días transcurridos desde el 1 de enero (entre 1 y 366). Positivo.
        anio (int): número de año (bisiesto o no). Positivo.
    -Valor retornado:
        (int) Número de mes (entre 1 y 12) correspondiente al dia_consecutivo en el anio dado.
    """
        </pre>
    </summary>
    <pre>
    dias_transcurridos = 0
    mes = 1
    while dias_transcurridos + dias_en_mes(mes, anio) < dia_consecutivo:
        dias_transcurridos += dias_en_mes(mes, anio)
        mes += 1
    return mes
    </pre>
</details>


<details>
    <summary>
        <pre>
def es_disarium(numero):
    """
    Evalúa si un número es un número "disarium". Un número es considerado "disarium" si la suma de sus dígitos, cada
    uno elevado a su respectiva posición dentro del número (empezando con la posición 1 desde la izquierda), es igual
    al número dado.
    Sugerencia: utilizar la función contar_digitos() desarrollada anteriormente.
    Ejemplo:
        es_disarium(numero=518) -> True
        (518 es un número disarium, ya que 5**1=5, 1**2=1, 8**3=512, y 5+1+512=518).
    -Parámetro:
        numero (int): número cuyos dígitos se procesarán. Positivo.
    -Valor retornado:
        (bool) True si numero es "disarium", False si no lo es.
    """
        </pre>
    </summary>
    <pre>
    posicion_digito = contar_digitos(numero=numero)
    numero_copia = numero
    suma = 0
    while numero_copia > 0:
        digito = numero_copia % 10
        suma = suma + (digito ** posicion_digito)
        posicion_digito -= 1
        numero_copia //= 10
    return suma == numero
    </pre>
</details>


<details>
    <summary>
        <pre>
def ordenar_monedas(cantidad):
    """
    Indica cuántos "escalones" pueden formarse con una cantidad específica de monedas que se ordenarán en forma de
    "escalera", donde cada escalón "n" debe estar formado por exactamente "n" monedas. El último escalón puede estar
    incompleto.
    Ejemplo:
        ordenar_monedas(cantidad=5) -> 2
        (Con 5 monedas pueden formarse solo 2 escalones completos, ya que no hay suficientes para el tercero:
        ¤
        ¤ ¤
        ¤ ¤
        )
    -Parámetro:
        cantidad (int): cantidad de monedas a usar. Positivo.
    -Valor retornado:
        (int) Cantidad máxima de escalones completos que pueden formarse con la cantidad de monedas dada.
    """
        </pre>
    </summary>
    <pre>
    i = 1
    while cantidad - i >= 0:
        cantidad -= i
        i += 1
    return i - 1
    </pre>
</details>


<details>
    <summary>
        <pre>
def cantidad_unos_solos(numero):
    """
    Cuenta, de un número, la cantidad de dígitos 1 que no están seguidos de otro 1 consecutivo.
    Sugerencia: evitar convertir el número o sus dígitos a otros tipos de datos.
    Ejemplos:
        cantidad_unos_solos(numero=141211) -> 2
        cantidad_unos_solos(numero=11411211) -> 0
    -Parámetro:
        numero (int): número cuyos dígitos se evaluarán. Positivo.
    -Valor retornado:
        (int) Cantidad de dígitos 1 no consecutivos en numero.
    """
        </pre>
    </summary>
    <pre>
    cantidad = 0
    anterior_es_uno = False
    unos_consecutivos = False
    while numero != 0:
        digito_actual = numero % 10
        if digito_actual == 1:
            if anterior_es_uno:
               unos_consecutivos = True 
            anterior_es_uno = True
        else:
            if anterior_es_uno and not unos_consecutivos:
                cantidad += 1
            anterior_es_uno = False
            unos_consecutivos = False
        numero //= 10
    if anterior_es_uno and not unos_consecutivos:
        return cantidad + 1
    return cantidad
    </pre>
</details>



# Strings

<details>
    <summary>
        <pre>
def cantidad_par_caracteres(cadena1, cadena2):
    """
    Indica si la cantidad de caracteres de ambas cadenas es par o no.
    Ejemplos:
        cantidad_par_caracteres(cadena1="aaaa", cadena2="aaaa") -> True
        cantidad_par_caracteres(cadena1="aaa", cadena2="aaaa") -> False
    -Parámetros:
        cadena1 (str): uno de los strings a procesar.
        cadena2 (str): otro de los strings a procesar.
    -Valor retornado:
        (bool) True si la cantidad de caracteres de cadena1 y la cantidad de caracteres de cadena2 son, ambas, números
        pares. False si al menos una de las dos cadenas tiene una cantidad impar de caracteres.
    """
        </pre>
    </summary>
    <pre>
    return len(cadena1) % 2 == 0 and len(cadena2) % 2 == 0
    </pre>
</details>


<details>
    <summary>
        <pre>
def contar_ocurrencias(cadena, caracter):
    """
    Cuenta la cantidad de veces que un carácter aparece en una cadena.
    Sugerencia: evitar el método count().
    Ejemplo:
        contar_ocurrencias(cadena="Esto es una frase", caracter="s") -> 3
    -Parámetros:
        cadena (str): string donde contar ocurrencias de un carácter.
        caracter (str): el carácter a contabilizar.
    -Valor retornado:
        (int) Cantidad de ocurrencias de caracter en cadena.
    """
        </pre>
    </summary>
    <pre>
    cantidad = 0
    for c in cadena:
        if c == caracter:
            cantidad += 1
    return cantidad
    </pre>
</details>


<details>
    <summary>
        <pre>
def contar_vocales_totales(cadena):
    """
    Cuenta la cantidad de vocales (incluyendo repeticiones) que hay en una cadena, teniendo en cuenta mayúsculas como
    minúsculas. Las vocales del idioma español son: a, e, i, o, u.
    Sugerencia: evitar el método count().
    Ejemplo:
        contar_vocales_totales(cadena="Esto es una frase") -> 7
    -Parámetro:
        cadena (str): string en el cual se contarán las vocales.
    -Valor retornado:
        (int) Cantidad total de vocales en cadena.
    """
        </pre>
    </summary>
    <pre>
    cantidad = 0
    for caracter in cadena:
        if caracter in "aeiouAEIOU":
            cantidad += 1
    return cantidad
    </pre>
</details>


<details>
    <summary>
        <pre>
def contar_vocales_unicas(cadena):
    """
    Cuenta la cantidad de vocales que hay en una cadena.
    Las vocales del idioma español son: a, e, i, o, u.
    Cada vocal debe contarse una única vez, indistintamente en su forma mayúscula o minúscula.
    Sugerencia: evitar el método count().
    Ejemplo:
        contar_vocales_unicas(cadena="Esto Es Una Frase") -> 4
    -Parámetro:
        cadena (str): string en el cual se contarán las vocales.
    -Valor retornado:
        (int) Cantidad de vocales únicas en cadena.
    """
        </pre>
    </summary>
    <pre>
    cadena_minusculas = cadena.lower()
    cantidad = 0
    for caracter in "aeiou":
        if caracter in cadena_minusculas:
            cantidad += 1
    return cantidad
    </pre>
</details>


<details>
    <summary>
        <pre>
def reemplazar_caracter_con_asterisco(cadena, caracter):
    """
    Reemplaza por '*' a todas las ocurrencias del carácter indicado.
    Sugerencia: evitar el método replace().
    Ejemplos:
        reemplazar_caracter_con_asterisco(cadena="esto es una frase", caracter="a") -> "esto es un* fr*se"
    -Parámetros:
        cadena (str): el string donde se harán los reemplazos.
        caracter (str): el carácter a reemplazar.
    -Valor retornado:
        (str) Un nuevo string con el contenido de cadena, donde todas las ocurrencias de caracter fueron reemplazadas
        por '*'.
    """
        </pre>
    </summary>
    <pre>
    nueva = ""
    for c in cadena:
        if c == caracter:
            nueva = nueva + "*"
        else:
            nueva = nueva + c
    return nueva
    </pre>
</details>


<details>
    <summary>
        <pre>
def invertir_cadena(cadena):
    """
    Invierte el orden de los caracteres de la cadena.
    Sugerencia: evitar usar rebanadas con paso negativo.
    Ejemplo:
        invertir_cadena(cadena="Esto es una frase!") -> "!esarf anu se otsE"
    Parámetro:
        cadena (str): string a invertir.
    -Valor retornado:
        (str) Un nuevo string con los caracteres de cadena en el orden inverso.
    """
        </pre>
    </summary>
    <pre>
    nueva = ""
    i = len(cadena)-1
    while i >= 0:
        nueva = nueva + cadena[i]
        i -= 1
    return nueva
    </pre>
</details>


<details>
    <summary>
        <pre>
def reemplazar_simbolos(cadena, nuevo_caracter):
    """
    Reemplaza todos los símbolos de la cadena por el carácter dado.
    Se consideran símbolos a los caracteres que no son letras, dígitos ni espacios.
    Ejemplo:
        reemplazar_simbolos(cadena="--Esto es 1 frase donde reemplazaremos con @ cada símbolo", nuevo_caracter="@") 
        -> "@@Esto es 1 frase donde reemplazaremos con @ cada símbolo"
    -Parámetros:
        cadena (str): string donde se efectuarán los reemplazos.
    -Valor retornado:
        (str) Un string donde cada símbolo ha sido reemplazado por nuevo_caracter.
    """
        </pre>
    </summary>
    <pre>
    cadena_reemplazada = ""
    for caracter in cadena:
        if (not caracter.isalpha()) and (not caracter.isdigit()) and caracter != " ":
            cadena_reemplazada = cadena_reemplazada + nuevo_caracter
        else:
            cadena_reemplazada = cadena_reemplazada + caracter
    return cadena_reemplazada
    </pre>
</details>


<details>
    <summary>
        <pre>
def porcentaje_digitos_numericos(cadena):
    """
    Retorna el porcentaje que representan los dígitos números sobre el total de caracteres de una cadena.
    Solo se retorna el número, sin el símbolo % y sin redondear (en caso de tener decimales).
    Ejemplos:
        porcentaje_digitos_numericos(cadena="Tenemos 1 dígito") -> 6.25
        porcentaje_digitos_numericos(cadena="1984") -> 100
    -Parámetro:
        cadena (str): string a procesar, que puede o no contener dígitos numéricos.
    -Valor retornado:
        (numérico) Porcentaje (número entre 0 y 100) de caracteres numéricos que posee la cadena, sobre su cantidad
        total de caracteres.
    """
        </pre>
    </summary>
    <pre>
    if len(cadena) == 0:
        return 0
    cantidad_numeros = 0
    for caracter in cadena:
        if caracter in "1234567890":
            cantidad_numeros += 1
    return (cantidad_numeros * 100) / len(cadena)
    </pre>
</details>


<details>
    <summary>
        <pre>
def clasificar_cadena_numerica(cadena):
    """
    Recibe un número en forma de string y retorna un nuevo string, conteniendo los caracteres que representan dígitos
    múltiplos de 2 y dígitos múltiplos de 3, ambos grupos separados por un '$'. Si un dígito es múltiplo de 2 y de 3
    al mismo tiempo, aparecerá a ambos lados del símbolo '$'.
    Ejemplo:
        clasificar_cadena_numerica(cadena="123456") -> "246$36"
        clasificar_cadena_numerica(cadena="2222") -> "2222$"
    -Parámetro:
        cadena (str): string numérico a procesar. El string solo contendrá dígitos numéricos.
    -Valor retornado:
        (str) String compuesto por la concatenación de los caracteres de la cadena que son múltiplos de 2 (en su
        representación numérica), seguidos de un '$' a continuación, seguidos de  la concatenación de los caracteres de
        la cadena que son múltiplos de 3.
    """
        </pre>
    </summary>
    <pre>
    multiplos2 = ""
    multiplos3 = ""
    for caracter in cadena:
        if int(caracter) % 2 == 0:
            multiplos2 += caracter
        if int(caracter) % 3 == 0:
            multiplos3 += caracter
    return multiplos2 + "$" + multiplos3
    </pre>
</details>


<details>
    <summary>
        <pre>
def caracteres_centrales(cadena):
    """
    Dada una cadena, retorna los 3 caracteres centrales.
    Ejemplos:
        caracteres_centrales(cadena="AbcDefGhi") -> "Def"
        caracteres_centrales(cadena="A   A") -> "   "
    -Parámetro:
        cadena (str) string a procesar. La cadena tendrá 5 o más caracteres y su longitud será impar.
    -Valor retornado:
        (str) String de longitud 3 conteniendo los caracteres ubicados en el medio de la cadena pasada por parámetro.
    """
        </pre>
    </summary>
    <pre>
    centro = (len(cadena) // 2) 
    return cadena[centro - 1:centro + 2]
    </pre>
</details>


<details>
    <summary>
        <pre>
def es_palindromo(cadena):
    """
    Verifica si una cadena es palíndromo, independientemente de mayúsculas y minúsculas.
    Se incluyen todos los caracteres, sean o no letras.
    Las letras acentuadas se consideran como caracteres diferentes de sus contrapartes no acentuadas.
    La cadena vacía no se considera palíndromo.
    Sugerencia: evitar las rebanadas con paso negativo y la función reversed().
    Ejemplos:
        es_palindromo(cadena="abba") -> True
        es_palindromo(cadena="baéceab") -> False
    -Parámetro:
        cadena (str): el string a procesar.
    -Valor retornado:
        (bool) True si la cadena es palíndromo. False si no lo es.
    """
        </pre>
    </summary>
    <pre>
    cadena_minusculas = cadena.lower()
    if len(cadena_minusculas) == 0:
        return False
    if len(cadena_minusculas) == 1:
        return True
    else:
        i = 0
        longitud = len(cadena_minusculas) - 1
        while (longitud > i):
            if (cadena_minusculas[i] != cadena_minusculas[longitud]):
                return False
            i = i + 1
            longitud = longitud - 1
        return True
    </pre>
</details>


<details>
    <summary>
        <pre>
def incluye_caracteres(cadena1, cadena2):
    """
    Indica si cadena2 incluye todos los caracteres que componen a cadena1.
    El orden de los caracteres no se tiene en cuenta.
    Se considera a la versión mayúscula y minúscula de una misma letra como caracteres diferentes.
    cadena1 puede contener caracteres repetidos y, en ese caso, cuentan como un único carácter a buscar en cadena2.
    Ejemplos:
        incluye_caracteres(cadena1="super", cadena2="supermercado") -> True       
        incluye_caracteres(cadena1="aaa", cadena2="rosa") -> True
    -Parámetros:
        cadena1 (str): el string cuyos caracteres deben buscarse en cadena2.
        cadena2 (str): el string donde se buscarán los caracteres de cadena1.
    -Valor retornado:
        (bool) True si cadena2 incluye todos los caracteres de cadena1. False si no incluye a todos.
    """
        </pre>
    </summary>
    <pre>
    for caracter in cadena1:
        if caracter not in cadena2:
            return False
    return True
    </pre>
</details>


<details>
    <summary>
        <pre>
def son_anagrama(cadena1, cadena2):
    """
    Indica si cadena1 es un anagrama de cadena2.
    No se tienen en cuenta mayúsculas y minúsculas pero sí las repeticiones de letras.
    Los strings a comparar solo contendrán letras.
    Ejemplos:
        son_anagrama(cadena1="aval", cadena2="lava") -> True
        son_anagrama(cadena1="aval", cadena2="lavar") -> False
    -Parámetros:
        cadena1 (str): un string a procesar, para saber si es anagrama de cadena2.
        cadena2 (str): un string a procesar, para saber si es anagrama de cadena1.
    -Valor retornado:
        (bool) True si son anagramas. False si no lo son.
    """
        </pre>
    </summary>
    <pre>
    if len(cadena1) != len(cadena2):
        return False
    cadena2_restante = cadena2.lower()
    for caracter in cadena1.lower():
        if caracter in cadena2_restante:
            cadena2_restante = cadena2_restante.replace(caracter, "", 1) 
        else:
            return False
    return cadena2_restante == ""
    </pre>
</details>


<details>
    <summary>
        <pre>
def cuantos_eliminar_para_anagrama(cadena1, cadena2):
    """
    Indica cuántos caracteres deben eliminarse para que cadena1 y cadena2 sean anagramas.
    No se tienen en cuenta mayúsculas y minúsculas pero sí las repeticiones de letras.
    Los strings a comparar solo contendrán letras.
    Ejemplo:
        cuantos_eliminar_para_anagrama(cadena1="avala", cadena2="lavar") -> 2
    -Parámetros:
        cadena1 (str): uno de los strings a procesar.
        cadena2 (str): otro string a procesar.
    -Valor retornado:
        (int) Cantidad de caracteres que deberían eliminarse para que ambas cadenas sean anagramas.
    """
        </pre>
    </summary>
    <pre>
    cantidad_caracteres_sobrantes = 0
    cadena2_restante = cadena2.lower()
    for caracter in cadena1.lower():
        if caracter not in cadena2_restante:
            cantidad_caracteres_sobrantes += 1
        else:
            cadena2_restante = cadena2_restante.replace(caracter, "", 1)             
    return cantidad_caracteres_sobrantes + len(cadena2_restante)
    </pre>
</details>


<details>
    <summary>
        <pre>
def invertir_palabras(cadena):
    """
    Invierte los caracteres de cada palabra en una cadena.
    Separador de palabras: un único espacio.
    La cadena no contendrá espacios al principio ni al final. Puede contener símbolos o dígitos y en ese caso se
    considerarán de la misma forma que las letras.
    Sugerencia: evitar usar el método split().
    Ejemplo:
        invertir_palabras(cadena="Esto es una frase.") -> "otsE se anu .esarf"
    -Parámetros:
        cadena (str): string formado por palabras que serán invertidas.
    -Valor retornado:
        (str) Un nuevo string donde cada palabra se encuentra invertida, sin modificar su posición original dentro de
        la cadena.
    """
        </pre>
    </summary>
    <pre>
    nueva = ""
    for i in range(cadena.count(" ")):
        espacio = cadena.find(" ")
        palabra = cadena[:espacio]
        nueva += palabra[::-1] + " "
        cadena = cadena[espacio+1:]
    nueva += cadena[::-1]
    return nueva
    </pre>
</details>


<details>
    <summary>
        <pre>
def longitud_ultima_palabra(cadena):
    """
    Retorna la longitud de la última palabra de una cadena.
    Separador de palabras: uno o más espacios.
    Ejemplos:
        longitud_ultima_palabra(cadena="esto es una frase") -> 5
        longitud_ultima_palabra(cadena="   espacios   ") -> 8
    -Parámetro:
        cadena (str): string compuesto por letras y espacios.
    -Valor retornado:
        (int) Cantidad de caracteres de la última palabra de la cadena.
    """
        </pre>
    </summary>
    <pre>
    if len(cadena) == 0:
        return 0
    cantidad = 0
    for i in range(len(cadena)):
        if cadena[i] != " ":
            cantidad += 1
        else:
            if i < len(cadena) - 1 and cadena[i + 1] != " ":
                cantidad = 0
    return cantidad
    </pre>
</details>


<details>
    <summary>
        <pre>
def convertir_a_titulo(cadena):
    """
    Convierte la primera letra de cada palabra a mayúsculas y el resto a minúsculas.
    Separador de palabras: cualquier símbolo (excluyendo letras y números), excepto apóstrofos.
    No debe modificarse la cantidad de espacios.
    Sugerencia: evitar el uso de title().
    Ejemplos:
        convertir_a_titulo(cadena="esto es una frase") -> "Esto Es Una Frase"
        convertir_a_titulo(cadena="ESTO ES UNA FRASE") -> "Esto Es Una Frase"
    -Parámetro:
        cadena (str): string a convertir.
    -Valor retornado:
        (str) Un nuevo string con el contenido de cadena, donde la primera letra de cada palabra es mayúscula y el
        resto son minúsculas.
    """
        </pre>
    </summary>
    <pre>
    nueva = ""
    inicio_palabra = True
    for caracter in cadena:
        if not caracter.isalpha():
            nueva = nueva + caracter
            if (not caracter.isdigit()) and caracter != "'":
                inicio_palabra = True
        else:
            if inicio_palabra:
                nueva = nueva + caracter.upper()
                inicio_palabra = False
            else:
                nueva = nueva+caracter.lower()
    return nueva
    </pre>
</details>


<details>
    <summary>
        <pre>
def cifrar_cesar(cadena, n):
    """
    Reemplaza cada letra de la cadena por otra del alfabeto, que se encuentre n posiciones hacia la derecha.
    Los corrimientos son circulares (si el alfabeto termina antes de poder correr la cantidad de lugares necesarios,
    se vuelve a comenzar desde la letra “a”).
    La cadena puede contener letras minúsculas, símbolos y dígitos. El cifrado solo se realizará sobre las letras,
    dejando al resto de caracteres sin modificación.
    La cantidad de corrimientos (n) será un número entre 1 y 27.
    Ejemplos:
        cifrar_cesar(cadena="esto es una frase", n=2) -> "guvq gu woc htcug"
        cifrar_cesar(cadena="abc123 xyz987!", n=4) -> "efg123 bcd987!"
    -Parámetros:
        cadena (str): string a cifrar.
        n (int): cantidad de posiciones que se moverá cada carácter dentro del alfabeto español de 27 letras.
    -Valor retornado:
        (str) Un nuevo string donde cada letra ha sido reemplazado por otra del alfabeto, ubicada n posiciones hacia la
        derecha.
    """
        </pre>
    </summary>
    <pre>
    alfabeto = "abcdefghijklmnñopqrstuvwxyz"
    cifrado = ""
    for caracter in cadena:
        if caracter in alfabeto:
            posicion = alfabeto.find(caracter)
            posicion = (posicion + n) % 27
            cifrado += alfabeto[posicion]
        else:
            cifrado += caracter
    return cifrado
    </pre>
</details>


<details>
    <summary>
        <pre>
def rotar_n_posiciones(cadena, n):
    """
    Dada una cadena, rota cada carácter n posiciones a la derecha, en forma circular (volviendo al principio al llegar
    al final).
    Los caracteres pueden ser letras, dígitos o símbolos.
    n no está necesariamente limitado a la longitud de cadena.
    Ejemplos:
        rotar_n_posiciones(cadena="Esto es una frase", n=6) -> " fraseEsto es una"
        rotar_n_posiciones(cadena="palabra", n=3) -> "brapala"
    -Parámetros:
        cadena (str): string a partir del cual se producirán las rotaciones.
        n (int): cantidad de posiciones que se moverá cada carácter dentro del string.
    -Valor retornado:
        (str) Un nuevo string donde cada carácter se ha desplazado n posiciones hacia la derecha.
    """
        </pre>
    </summary>
    <pre>
    rotada = cadena
    for posicion in range(len(cadena)):
        nueva_posicion = (posicion + n) % len(cadena)
        rotada = rotada[:nueva_posicion] + cadena[posicion] + rotada[nueva_posicion + 1:]
    return rotada
    </pre>
</details>


<details>
    <summary>
        <pre>
def comprimir_RLE(cadena):
    """
    Comprime un string utilizando la codificación RLE ("Run-Length Encoding").
    RLE: por cada grupo de caracteres consecutivos repetidos, se almacenará una única ocurrencia del carácter,
    seguida del número de ocurrencias en caso de que sea mayor que 1 (ejemplo: 'aaab' se comprime como 'a3b').
    La cadena solo estará compuesta por letras y/o símbolos.
    Ejemplos:
        comprimir_RLE(cadena="aaabbc") -> "a3b2c"
        comprimir_RLE(cadena="abcde") -> "abcde"
    -Parámetro:
        cadena (str): string a comprimir.
    -Valor retornado:
        (str) String comprimido mediante RLE.
    """
        </pre>
    </summary>
    <pre>
    comprimido = ""
    if len(cadena) < 2:
        return cadena
    posicion = 1
    cantidad = 1
    while posicion < len(cadena):
        if cadena[posicion] != cadena[posicion - 1]:
            comprimido += cadena[posicion - 1]
            if cantidad != 1:
                comprimido += str(cantidad)
                cantidad = 1
        else:
            cantidad += 1
        posicion += 1
    comprimido += cadena[posicion - 1]
    if cantidad != 1:
        comprimido += str(cantidad)
    return comprimido
    </pre>
</details>



# Listas y tuplas

<details>
    <summary>
        <pre>
def productoria_numeros(numeros):
    """
    Retorna el producto de todos los números en una lista.
    La lista solo contendrá números.
    Ejemplo:
        productoria_numeros(numeros=[1, 2, 3, 4]) -> 24
    -Parámetros:
        numeros (list, elementos: numéricos): lista cuyos números se multiplicarán.
    -Valor retornado:
        (numérico / None) El producto de todos los números en la lista. Si la lista está vacía, retorna None.
    """
        </pre>
    </summary>
    <pre>
    if len(numeros) == 0:
        return None
    producto = 1
    for numero in numeros:
        producto *= numero
    return producto
    </pre>
</details>


<details>
    <summary>
        <pre>
def mayor_elemento(strings):
    """
    Retorna el mayor elemento de una lista de strings.
    Ejemplo:
        mayor_elemento(strings=["x", "y", "z"]) -> "z"
    -Parámetros:
        strings (list; elementos: str): la lista donde se buscará el mayor elemento.
    -Valor retornado:
        (str / None) El mayor de los strings contenidos en la lista. Si la lista está vacía, retorna None.
    """
        </pre>
    </summary>
    <pre>
    if len(strings) == 0:
        return None
    mayor = ""
    for cadena in strings:
        if cadena > mayor:
            mayor = cadena
    return mayor
    </pre>
</details>


<details>
    <summary>
        <pre>
def mayor_ganancia(precios):
    """
    Dada una lista donde cada elemento representa el precio de las acciones de una empresa en un día determinado,
    retorna la mayor ganancia obtenida si se compra en el día de menor precio y se vende el día en que el precio
    es mayor. La lista contendrá al menos dos elementos.
    Ejemplo:
        mayor_ganancia(precios=[70, 53, 15, 23, 41, 30]) -> 55
        (Si los precios son [70, 53, 15, 23, 41, 30] la mayor ganancia se obtiene comprando a 15 y vendiendo a 70,
        entonces: 70-15=55).
    -Parámetro:
        precios (list; elementos: numéricos): lista con los precios de las acciones en cada día. len(precios) >= 2.
    -Valor retornado:
        (numérico) La mayor ganancia que puede obtenerse si se compra al menor valor y se vende al mayor valor.
    """
        </pre>
    </summary>
    <pre>
    maximo = precios[0]
    minimo = precios[0]
    for precio in precios:
        if precio > maximo:
            maximo = precio
        elif precio < minimo:
            minimo = precio
    return maximo - minimo
    </pre>
</details>


<details>
    <summary>
        <pre>
def elementos_unicos(puede_tener_duplicados):
    """
    Retorna una nueva lista con los elementos que no se repiten.
    Ejemplos:
        elementos_unicos(puede_tener_duplicados=[3, False, "a", 1, 1, 2, 4, False, 4]) -> [3, "a", 2]
        elementos_unicos(puede_tener_duplicados=[1, 1, 1]) -> []
    -Parámetro:
        puede_tener_duplicados (list; elementos: heterogéneos): lista que puede o no tener elementos duplicados.
    -Valor retornado:
        (list; elementos: heterogéneos) Una nueva lista, con los elementos de puede_tener_duplicados que sean únicos.
    """
        </pre>
    </summary>
    <pre>
    nueva = []
    for elemento in puede_tener_duplicados:
        if puede_tener_duplicados.count(elemento) == 1:
            nueva.append(elemento)
    return nueva
    </pre>
</details>


<details>
    <summary>
        <pre>
def porcentaje_pares_impares(numeros):
    """
    Dada una lista de números, retorna en una tupla el porcentaje de números pares e impares que contiene.
    La lista contendrá al menos un elemento.
    Ejemplos:
        porcentaje_pares_impares(numeros=[-5, 3, 2, -4, 7]) -> (40.0, 60.0)
        porcentaje_pares_impares(numeros=[1, 1, 1, 1]) -> (0.0, 100.0)
    -Parámetro:
        numeros (list; elementos: int): lista de números. len(numeros) >= 1.
    -Valor retornado:
        (tuple; elementos: float) Una tupla donde el primer elemento representa el porcentaje (de 0 a 100) de números pares sobre el total de
        elementos contenidos en numeros y el segundo elemento representa el porcentaje de números impares contenidos en
        numeros.
    """
        </pre>
    </summary>
    <pre>
    cantidad_pares = 0
    cantidad_impares = 0
    for numero in numeros:
        if numero % 2 == 0:
            cantidad_pares += 1
        else:
            cantidad_impares += 1
    return (cantidad_pares * 100) / len(numeros), (cantidad_impares * 100) / len(numeros)
    </pre>
</details>


<details>
    <summary>
        <pre>
def sumar_indice(numeros):
    """
    A cada elemento de una lista de números, le suma el índice donde se encuentra.
    Ejemplos:
        sumar_indice(numeros=[1, 2, 3, 4, 5, 6]) -> [1, 3, 5, 7, 9, 11]
        sumar_indice(numeros=[0, 0, 0]) -> [0, 1, 2]
    -Parámetros:
        numeros (list; elementos: numéricos): lista de números.
    -Valor retornado:
        (list; elementos: numéricos) Una nueva lista donde, a cada elemento de numeros se le ha sumado su índice.
    """
        </pre>
    </summary>
    <pre>
    nueva = []
    for indice in range(len(numeros)):
        nueva.append(numeros[indice] + indice)
    return nueva
    </pre>
</details>


<details>
    <summary>
        <pre>
def sumas_parciales(numeros):
    """
    Retorna una nueva lista donde cada elemento es la suma parcial de sí mismo más todos los elementos anteriores
    dentro de la lista original.
    Ejemplo:
        sumas_parciales(numeros=[4, 6, 10, 7]) -> [4, 10, 20, 27]
        (Cada número es calculado como: 4, 6+4, 10+6+4, 7+10+6+4).
    -Parámetros:
        numeros (list; elementos: numéricos): lista de números.
    -Valor retornado:
        (list; elementos: numéricos) Una nueva lista donde cada elemento es la suma de sí mismo más todos los
        anteriores.
    """
        </pre>
    </summary>
    <pre>
    nueva = []
    subtotal = 0
    for numero in numeros:
        subtotal += numero
        nueva.append(subtotal)
    return nueva
    </pre>
</details>


<details>
    <summary>
        <pre>
def numeros_faltantes(numeros):
    """
    Dada una lista de n elementos numéricos enteros, retorna una nueva lista cuyos elementos son los números entre 0 y
    n-1 que no aparecen en la lista pasada por parámetro.
    Ejemplos:
        numeros_faltantes(numeros=[5, 0, 2, 9, 8, 12, 9]) -> [1, 3, 4, 6]
        (n=7, entonces: 1, 3, 4, 6 son los números entre 0 y 6 que no aparecen en la lista).
        numeros_faltantes(numeros=[3, 7, 15, 3, 9]) -> [0, 1, 2, 4]
    -Parámetro:
        numeros (list; elementos: int): una lista de números, de longitud n.
    -Valor retornado:
        (list; elementos: int) Una nueva lista donde los elementos son los números entre 0 y n-1 que no aparecen en
        numeros.
    """
        </pre>
    </summary>
    <pre>
    nueva = []
    for i in range(len(numeros)):
        if i not in numeros:
            nueva.append(i)
    return nueva
    </pre>
</details>


<details>
    <summary>
        <pre>
def cuantos_numeros_menores(numeros):
    """
    Dada una lista con números, por cada numeros[i] indica cuántos números en la lista son menores que él.
    Ejemplo:
        cuantos_numeros_menores(numeros=[6, 3, 3, 4, 2]) -> [4, 1, 1, 3, 0]
        (Ya que i=0 almacena el número 6 y hay otros cuatro elementos en nums que son menores que 6: 3, 3, 4, 1.
        i=1 almacena el número 3 y hay un elemento menor: 2. Lo mismo sucede con i=2. i=3 almacena el 4 y hay tres
        elementos menores: 3, 3, 2. Y para i=4, que almacena el número 2, no hay elementos menores).
    -Parámetros:
        numeros (list; elementos: numéricos): lista de números.
    -Valor retornado:
        (list; elementos: numéricos) Una nueva lista donde cada elemento j es la cantidad de elementos menores que
        numeros[i] existentes en numeros.
    """
        </pre>
    </summary>
    <pre>
    nueva = []
    for numero_actual in numeros:
        menores = 0
        for numero_a_comparar in numeros:
            if numero_a_comparar < numero_actual:
                menores += 1
        nueva.append(menores)
    return nueva            
    </pre>
</details>


<details>
    <summary>
        <pre>
def dos_maximos(numeros):
    """
    Retorna los dos números más grandes contenidos en una lista.
    La lista contendrá al menos dos elementos.
    Ejemplo:
        dos_maximos(numeros=[5, 3, 6, 2, 8]) -> (8, 6)
    -Parámetro:
        numeros (list; elementos: numéricos): la lista con números a evaluar. len(numeros) >= 2.
    -Valor retornado:
        (tuple; 2 elementos: numéricos) Una tupla con los dos números mayores contenidos dentro de numeros, donde el
        elemento en la posición 0 es mayor o igual que el elemento en la posición 1.
    """
        </pre>
    </summary>
    <pre>
    maximo1 = numeros[0]
    maximo2 = numeros[1]
    for numero in numeros:
        if numero > maximo1:
            maximo2 = maximo1
            maximo1 = numero
        elif numero > maximo2:
            maximo2 = numero
    return (maximo1, maximo2)
    </pre>
</details>


<details>
    <summary>
        <pre>
def jugada_uno(mano, carta_descubierta):
    """
    Dada una "mano" de cartas que tiene un jugador del juego "Uno" y la carta que está descubierta sobre la mesa,
    retorna True si el jugador puede hacer una jugada, o False en caso contrario.
    El jugador puede hacer una jugada si:
    * tiene una carta con el mismo color que la carta descubierta, o
    * tiene una carta con el mismo número que la carta descubierta.
    Las cartas se representan por un string con el color y el número, separados por un espacio. El número está entre 
    0 y 9. La cantidad de cartas en una mano puede variar y puede ser 0.
    Ejemplos:
        jugada_uno(mano=["rojo 2", "azul 5", "verde 1"], carta_descubierta="rojo 3") -> True
        jugada_uno(mano=["rojo 2", "azul 5", "verde 1"], carta_descubierta="amarillo 3") -> False
    -Parámetros:
        mano (list; elementos: str): lista con las cartas que tiene en la mano el jugador.
        carta_descubierta (str): carta que se encuentra descubierta sobre la mesa.
    -Valor retornado:
        (bool) True si el jugador está habilitado a hacer una jugada (el color o el número de una de sus cartas
        coincide con el color o el número de la carta descubierta). False en caso contrario.
    """
        </pre>
    </summary>
    <pre>
    color_carta_descubierta = carta_descubierta[:len(carta_descubierta)-2]
    numero_carta_descubierta = carta_descubierta[:-2:-1]
    for carta in mano:
        color = carta[:len(carta)-2]
        numero = carta[:-2:-1]
        if color == color_carta_descubierta or numero == numero_carta_descubierta:
            return True
    return False
    </pre>
</details>


<details>
    <summary>
        <pre>
def descartar_ocurrencias_extra(numeros, n):
    """
    Dada una lista y un número n retorna una nueva lista donde, si un elemento aparece más de n veces en numeros, se 
    descartan las ocurrencias sobrantes, dejando solo las primeras n. El resto de los elementos seguirán apareciendo
    en el mismo orden relativo.
    Ejemplos:
        descartar_ocurrencias_extra(numeros=[1, 2, 3, 2, 3, 3], n=1) -> [1, 2, 3]
        descartar_ocurrencias_extra(numeros=[1, 2, 3, 2, 3, 3], n=3) -> [1, 2, 3, 2, 3, 3]
    -Parámetros:
        numeros (list; elementos: int): la lista a procesar.
        n (int): cantidad de ocurrencias máximas que pueden aparecer de cada elemento.
    -Valor retornado:
        (list; elementos: int) Una nueva lista donde los elementos sean los mismos y en el mismo orden que en numeros,
        exceptuando las ocurrencias de n.
    """
        </pre>
    </summary>
    <pre>
    nueva = []
    for elemento in numeros:
        if nueva.count(elemento) < n:
            nueva.append(elemento)
    return nueva
    </pre>
</details>


<details>
    <summary>
        <pre>
def es_desplazamiento(numeros1, numeros2, n):
    """
    Dadas dos listas, indica si la primera de ellas es igual a la segunda con sus elementos desplazados (rotados) n
    posiciones hacia la derecha, de manera circular (es decir: al llegar al final de la lista se retorna al principio).
    Las dos listas tendrán la misma longitud.
    Ejemplos:
        es_desplazamiento(numeros1=[1, 2, 3, 4], numeros2=[3, 4, 1, 2], n=2) -> True
        es_desplazamiento(numeros1=[1, 2], numeros2=[3, 4], n=1) -> False
    -Parámetros:
        numeros1 (list; elementos: numéricos): la lista desplazada.
        numeros2 (list; elementos: numéricos): la lista con la cual se comparará numeros1.
        n (int): cantidad de posiciones de rotación. Positivo.
    -Valor retornado:
        (bool) True si numeros1 equivale a numeros2 con sus elementos rotados n posiciones hacia la derecha. False en
        el caso contrario.
    """
        </pre>
    </summary>
    <pre>
    return numeros1 == numeros2[n:] + numeros2[:n]
    </pre>
</details>


<details>
    <summary>
        <pre>
def suma_cada_n(numeros, n):
    """
    Dada una lista de números y un número positivo n, retorna la suma de cada n elementos de la lista.
    n puede ser mayor que la longitud de la lista y no necesariamente es un múltiplo de esta longitud.
    n no puede ser 0.
    Si n es mayor que la longitud de la lista, retorna 0.
    Sugerencia: evitar la función sum().
    Ejemplo:
        suma_cada_n(numeros=[5, 2, 1, 6, 4, 9, 3, 7, 8], n=3) -> 18
        (Pues 1+9+8=18).
        suma_cada_n(numeros=[1.5, 2, -3, 4], n=5) ->0
    -Parámetros:
        numeros (list; elementos: numéricos): lista de números.
        n (int): número entero mayor que 0.
    -Valor retornado:
        (int) Suma de los elementos de numeros, comenzando por el elemento en la posición n y saltando de a n
        posiciones. 0 si n es mayor que la cantidad de elementos en la lista.
    """
        </pre>
    </summary>
    <pre>
    if n == 0:
        return numeros[0]
    suma = 0
    for i in range(len(numeros)):
        if (i+1) % n == 0:
            suma += numeros[i]
    return suma
    </pre>
</details>


<details>
    <summary>
        <pre>
def desplazar_ceros(numeros):
    """
    Dada una lista con números enteros, desplaza todos los ceros hacia la derecha (el final de la lista), sin modificar
    el orden relativo de los demás números.
    Los desplazamientos deben hacerse sobre la lista original, sin utilizar una lista adicional.
    Ejemplos:
        desplazar_ceros(numeros=[5, 8, 0, 3, 0, 0, 4]) -> [5, 8, 3, 4, 0, 0, 0]
        desplazar_ceros(numeros=[1, 2, 3, 0, 0, 0]) -> [1, 2, 3, 0, 0, 0]
    -Parámetro:
        numeros (list; elementos: int): la lista con números a procesar.
    -Valor retornado:
        (list; elementos: int) La lista numeros, con sus ceros ubicados de forma contigua al final y el resto de los
        elementos manteniendo su orden relativo.
    """
        </pre>
    </summary>
    <pre>
    i = 0
    for j in range(len(numeros)):
        if numeros[j] != 0:
            numeros[i], numeros[j] = numeros[j], numeros[i]
            i += 1
    return numeros
    </pre>
</details>


<details>
    <summary>
        <pre>
def desanidar(listas):
    """
    Dada una lista cuyos elementos son listas, retorna una nueva lista con un nivel menos de anidamiento.
    Sugerencia: evitar usar bucles anidados.
    Ejemplos:
        desanidar(listas=[[1, 0, 4], ["a", "b"], [True, False, True, True]]) 
        -> [1, 0, 4, "a", "b", True, False, True, True]
        desanidar(listas=[[], ["a", "b"]]) -> ["a", "b"]
    -Parámetro:
        listas (list; elementos: list, con elementos heterogéneos): una lista que contiene listas como elementos (los
        elementos de éstas pueden ser de cualquier tipo).
    -Valor retornado:
        (list; elementos: heterogéneos) Una nueva lista cuyos elementos son directamente los elementos que están
        contenidos dentro de las listas anidadas dentro de la pasada por parámetro, sin alterar su orden.
    """
        </pre>
    </summary>
    <pre>
    nueva = []
    for sub_lista in listas:
        nueva = nueva + sub_lista
    return nueva
    </pre>
</details>


<details>
    <summary>
        <pre>
def cantidad_aprobados(resultados_examen):
    """
    Dada una lista con los resultados de cada alumno en un examen, retorna cuántos de ellos fueron aprobados. El
    examen se aprueba con una calificación de 6 o más. Los datos de los alumnos están formados por listas que
    contienen: nombre, número de identificación, calificación.
    Ejemplo:
        cantidad_aprobados(resultados_examen=[["Mario Perez", 331, 6],
                                              ["Luisa Rey", 112, 3],
                                              ["Fernanda Torres", 256, 8],
                                              ["Martín Sotomayor", 209, 7]])
        -> 3
    -Parámetro:
        resultados_examen (list; elementos: list, con 3 elementos: str, int, int): lista con datos de alumnos,
        contenidos en listas anidadas.
    -Valor retornado:
        (int) Cantidad de alumnos que aprobaron el examen.
    """
        </pre>
    </summary>
    <pre>
    aprobados = 0
    for resultado in resultados_examen:
        if resultado[2] >= 6:
            aprobados += 1
    return aprobados
    </pre>
</details>


<details>
    <summary>
        <pre>
def suma_diagonal(matriz):
    """
    Dada una matriz cuadrada (conformada por una lista de listas), retorna la suma de su diagonal principal.
    Ejemplo:
        suma_diagonal(matriz=[[1, 2, 3], [4, 5, 6], [7, 8, 9]]) -> 15
        (Ya que la matriz puede leerse como:
        [[1,2,3],
        [4,5,6],
        [7,8,9]]
        y esto retorna 15, pues 1+5+9=15).
    -Parámetro:
        matriz (list; elementos: list, con elementos numéricos): lista de listas, formando una matriz de n columnas y
        n filas.
    -Valor retornado:
        (numeric) Suma de la diagonal principal.
    """
        </pre>
    </summary>
    <pre>
    suma = 0
    for i in range(len(matriz)):
        suma += matriz[i][i]
    return suma
    </pre>
</details>


<details>
    <summary>
        <pre>
def buscar_pais(ciudades, nombre_ciudad):
    """
    Dada una lista con tuplas conteniendo ciudad y país al que pertenece, y el nombre de una ciudad, retorna el país al
    que la ciudad pertenece.
    En caso de que la ciudad no exista en la lista, retornará None.
    Ejemplo:
        buscar_pais(ciudades=[("Buenos Aires", "Argentina"),
                              ("Glasgow", "Escocia"),
                              ("Liverpool", "Inglaterra"),
                              ("Madrid", "España")],
                    nombre_ciudad="Glasgow")
        -> "Escocia"
    -Parámetros:
        -ciudades (list; elementos: tuple, con 2 elementos: str, str): lista de ciudades. Cada ciudad está representada
        por una tupla en la forma: (nombre de ciudad, país al que pertenece).
        -nombre_ciudad (str): nombre de una ciudad.
    -Valor retornado:
        (str / None) Nombre del país al que corresponde la ciudad pasada por parámetro. None si la ciudad no existe en
        la lista ciudades.
    """
        </pre>
    </summary>
    <pre>
    for ciudad in ciudades:
        if nombre_ciudad == ciudad[0]:
            return ciudad[1]
    return None
    </pre>
</details>


<details>
    <summary>
        <pre>
def buscar_destino(boletos, ciudades, numero_boleto):
    """
    Dado el número de un boleto de viaje, retorna el país de destino.
    La función recibe una lista con boletos de viaje (de cada boleto se tiene el número y la ciudad destino) y otra
    lista con datos de ciudades (de cada una se tiene el nombre de ciudad y país donde está ubicada). Además, recibe un
    número de boleto. De acuerdo el número de boleto ubicará la ciudad destino y, de acuerdo a la ciudad destino,
    retornará el país al que pertenece. Si el número de boleto no se encuentra en la lista, retornará None.
    Sugerencia: utilizar la función buscar_pais() desarrollada anteriormente.
    Ejemplo:
        buscar_destino(boletos=[(100, "Buenos Aires"), (110, "Madrid"), (120, "Glasgow")],
                       ciudades=[("Buenos Aires", "Argentina"), ("Glasgow", "Escocia"), ("Liverpool", "Inglaterra"), 
                                 ("Madrid", "España")],
                       numero_boleto=100),
        -> "Argentina"
    -Parámetros:
        -boletos (list; elementos: tuple, con 2 elementos: int, str): lista con los boletos de viaje. Cada boleto está
        representado por una tupla en la forma: (número de boleto, ciudad destino).
        -ciudades (list; elementos: tuple, con 2 elementos: str, str): lista de ciudades. Cada ciudad está representada
        por una tupla en la forma: (nombre de ciudad, país al que pertenece).
        -numero_boleto (int): número de un boleto de viaje.
    -Valor retornado:
        (str) Nombre del país de destino correspondiente al boleto identificado por numero_boleto.
    """
        </pre>
    </summary>
    <pre>
    for boleto in boletos:
        if numero_boleto == boleto[0]:
            return buscar_pais(ciudades, boleto[1])
    return None
    </pre>
</details>



# Conjuntos y diccionarios

<details>
    <summary>
        <pre>
def hallar_repetidos(strings1, strings2):
    """
    Dadas dos listas de strings, retorna cuáles de esos strings están incluidos en ambas listas.
    Sugerencia: evitar iterar por las listas para lograr el cometido.
    Ejemplo:
        hallar_repetidos(strings1=["abc", "cde", "abc", "fff"], strings2=["cde", "aaa"]) -> {"cde"}
    -Parámetros:
        strings1 (list; elementos: str): lista con strings a procesar.
        strings2 (list; elementos: str): lista con strings a procesar.
    -Valor retornado:
        (set; elementos: str) Los strings que coinciden en strings1 y strings2.
    """
        </pre>
    </summary>
    <pre>
    return set(strings1) & set(strings2)
    </pre>
</details>


<details>
    <summary>
        <pre>
def solo_una_mascota(perros, gatos):
    """
    Dada una lista de dueños de mascotas que tienen perros y otra lista de dueños que tienen gatos (donde un mismo
    nombre puede estar en ambas, en caso de tener ambas mascotas), retorna cuáles de esas personas tiene únicamente
    perro o únicamente gato, pero no ambos.
    Sugerencia: evitar iterar por las listas para lograr el cometido.
    Ejemplo:
         solo_una_mascota(perros=["Lucrecia Borges", "Juan Sebastián Balsa", "Cristóbal Colombraro"],
                          gatos=["Juan Sebastián Balsa", "Juan Jacobo Russo", "Ana Bologna", "Cristóbal Colombraro"])
        -> {"Lucrecia Borges", "Juan Jacobo Russo", "Ana Bologna"}
    -Parámetros:
        perros (list; elementos: str): lista con los nombres de dueños de perros.
        gatos(list; elementos: str): lista con los nombres de dueños de gatos.
    -Valor retornado:
        (set; elementos: str) Los nombres de aquellos dueños de mascota que solo tienen perros o solo tienen gatos
        pero no ambos.
    """
        </pre>
    </summary>
    <pre>
    return set(perros) ^ set(gatos)
    </pre>
</details>


<details>
    <summary>
        <pre>
def elementos_unicos(tuplas):
    """
    Dada una cantidad indeterminada de tuplas que contienen números, retorna una tupla que combine todas las
    anteriores, pero donde cada número aparece una única vez (sin duplicados).
    Ejemplo:
        elementos_unicos(tuplas=[(1,2,3), (2,2,2,2), (3,4,5), (1,3,5,7,9)]) -> (1,2,3,4,5,7,9)
    -Parámetro:
        tuplas (list; elementos: tuple, con elementos int): lista conteniendo tuplas de números.
    -Valor retornado:
        (tuple; elementos: int) Tupla donde se combinan todos los números de las tuplas dadas, con una única
        ocurrencia de cada número.
    """
        </pre>
    </summary>
    <pre>
    unicos = set()
    for tupla in tuplas:
        unicos.update(tupla)
    return tuple(unicos)
    </pre>
</details>


<details>
    <summary>
        <pre>
def listar_apellidos(alumnos):
    """
    Dada una lista conteniendo los nombres y apellidos de los alumnos de una institución, retorna una estructura que
    contiene los apellidos únicamente, sin repeticiones. Los nombres y apellidos de los alumnos están contenidos en un
    único string, separados por un espacio. Cada alumno puede tener más de un nombre pero solo un apellido, en la
    forma: "nombre(s) apellido".
    Ejemplo:
        listar_apellidos(alumnos=["Lara Ruiz", "Esteban Raúl Perez", "Francina Soto", "Lucas Perez"])
        -> {"Ruiz", "Perez", "Soto"}
    -Parámetro:
        alumnos (list; elementos: str): lista de alumnos.
    -Valor retornado:
        (set; elementos: str) Conjunto conteniendo los apellidos únicos en la lista alumnos.
    """
        </pre>
    </summary>
    <pre>
    apellidos = set()
    for alumno in alumnos:
        apellido = alumno.split()[-1]
        apellidos.add(apellido)
    return apellidos
    </pre>
</details>


<details>
    <summary>
        <pre>
def domicilios_facturacion(ventas):
    """
    Dada una lista con datos de las compras hechas por clientes de una empresa a lo largo de un mes, la cual contiene
    tuplas con información de cada venta: (nombre del cliente, día del mes, monto de la compra, domicilio del cliente),
    retorna los domicilios de cada cliente al cual se le debe enviar una factura de compra. Cada cliente puede haber
    hecho más de una compra en el mes, por lo que cada domicilio debe aparecer una sola vez.
    Ejemplo:
        domicilios_facturacion(ventas=[("Nuria Costa", 5, 12780.78, "Calle Las Flores 355"),
                                       (Jorge Russo", 7, 699, "Mirasol 218"),
                                       ("Nuria Costa", 7, 532.90, "Calle Las Flores 355"),
                                       ("Julián Rodriguez", 12, 5715.99, "La Mancha 761"),
                                       ("Jorge Russo", 15, 958, "Mirasol 218")])
        -> {'Calle Las Flores 355', 'Mirasol 218', 'La Mancha 761'}
    -Parámetro:
        (list; elementos: tuple, con elementos heterogéneos) ventas: lista con tuplas representando cada una de las
        ventas del mes.
    -Valor retornado:
        (set; elementos: str) Conjunto conteniendo los domicilios a los cuales se debe enviar la factura.
    """
        </pre>
    </summary>
    <pre>
    domicilios = set()
    for venta in ventas:
        domicilios.add(venta[3])
    return domicilios
    </pre>
</details>


<details>
    <summary>
        <pre>
def agregar_pelicula(peliculas, pelicula):
    """
    Agrega datos de una película a un diccionario y lo retorna modificado. Si la película ya existe, la reemplaza con
    los nuevos datos. Los datos que se almacenan de cada película son: nombre, director, año de estreno. El diccionario
    usa el nombre de cada película como claves y una lista con el resto de datos como valor.
    Ejemplo:
        agregar_pelicula(peliculas={"Joker": ["Todd Phillips", 2019],
                                    "Avatar": ["James Cameron", 2009]},
                         pelicula=("Lord of the rings: The two towers", "Peter Jackson", 2002))
        -> {"Joker": ["Todd Phillips", 2019],
            "Avatar": ["James Cameron", 2009],
            "Lord of the rings: The two towers": ["Peter Jackson", 2002]}
    -Parámetros:
        peliculas (dict; clave: str; valor: list, con 2 elementos: str, int): diccionario de películas.
        pelicula (tuple; 3 elementos: str, str, int): tupla con los datos de la película a agregar: nombre,
        director, año de estreno.
    -Valor retornado:
        (dict; clave: str; valor: list, con 2 elementos: str, int) El diccionario peliculas con el nuevo dato agregado.
    """
        </pre>
    </summary>
    <pre>
    if pelicula:
        peliculas[pelicula[0]] = [pelicula[1], pelicula[2]]
    return peliculas
    </pre>
</details>


<details>
    <summary>
        <pre>
def mas_votados(votos, curso):
    """
    Dado un diccionario con los votos que se hicieron para seleccionar al "mejor compañero" en los cursos de un
    instituto educativo, y dado un número de curso, retorna los nombres de todos los alumnos que fueron votados, sin
    repeticiones. El diccionario tiene como claves los números de los cursos y como valores listas de strings con cada
    voto. Si el número de curso dado no se encuentra en el diccionario, retorna un conjunto vacío.
    Ejemplo:
        mas_votados(votos={1:["juan", "juan", "lorena", "juan", "lorena", "paula"],
                           2:["romina", "marcos", "guadalupe", "guadalupe"],
                           3:["lucas", "abril", "lucas", "abril", "abril", "serena", "abril"]},
                    curso=3)
        -> {"lucas", "abril", "serena"}
    -Parámetros:
        votos (dict; clave: int; valor: list, con elementos str): diccionario con los votos de cada curso, donde las
        claves son los números de curso y los valores son listas conteniendo cada uno de los votos. 
        curso (int): número del curso del cual se buscarán los nombres de compañeros votados.
    -Valor retornado:
        (set; elementos: str) Conjunto con los nombres de los alumnos votados en el curso.
    """
        </pre>
    </summary>
    <pre>
    if curso in votos:
        return set(votos[curso])
    else:
        return set()
    </pre>
</details>


<details>
    <summary>
        <pre>
def ocurrencias_digitos(digitos=digitos):
    """
    Dada una lista que contiene dígitos numéricos, informa la cantidad de ocurrencias de cada dígito, indicando el
    valor 0 para los dígitos (entre el 0 y el 9) que no se encuentran en la lista.
    Sugerencia: evitar el uso de collections.Counter().
    Ejemplo:
        ocurrencias_digitos(digitos=[8, 9, 0, 4, 2, 2, 4, 1, 8, 2]) -> {0:1, 1:1, 2:3, 3:0, 4:2, 5:0, 6:0, 7:0, 8:2, 9:1}
    -Parámetro:
        digitos (list; elementos: int): lista cuyos elementos son dígitos numéricos (entre el 0 y el 9).
    -Valor retornado:
        (dict; clave: int; valor: int) Diccionario contabilizando las ocurrencias de cada dígito, donde las claves son
        los dígitos del 0 al 9.
    """
        </pre>
    </summary>
    <pre>
    ocurrencias = {}
    for i in range(10):
        ocurrencias[i] = 0
    for digito in digitos:
        ocurrencias[digito] += 1
    return ocurrencias
    </pre>
</details>


<details>
    <summary>
        <pre>
def contar_ocurrencias(listas):
    """
    Dada una tupla que contiene listas de caracteres, cuenta la cantidad de ocurrencias de cada carácter en todas las
    listas.
    Ejemplo:
        contar_ocurrencias(listas=(["i", "%", "u"],
                                   ["^", "%", "^", "s", "i", "i", "u"],
                                   ["a", "u"]))
        -> {'i':3, '%':2, 'u':3, 's':1, '^':2, 'a':1}
    -Parámetro:
        listas (tuple; elementos: list, con elementos str): tupla conteniendo listas cuyos elementos son caracteres
        (strings de longitud 1).
    -Valor retornado: 
       (dict; clave: str; valor: int) Diccionario contabilizando las ocurrencias de cada letra.
    """
        </pre>
    </summary>
    <pre>
    ocurrencias = {}
    for lista in listas:
        for letra in lista:
            if letra not in ocurrencias:
                ocurrencias[letra] = 1
            else:
                ocurrencias[letra] += 1
    return ocurrencias
    </pre>
</details>


<details>
    <summary>
        <pre>
def mayor_valor(ocurrencias):
    """
    Dado un diccionario con valores únicos de tipo numérico positivos, retorna cuál es la clave que corresponde al
    mayor valor. Si el diccionario está vacío, retorna string vacío. Cada valor solo ocurre una vez en el diccionario.
    Sugerencia: evitar el uso de max().
    Ejemplo:
        mayor_valor(ocurrencias={"a":1, "e":7, "i":4, "o":9, "u":3}) -> "o"
    -Parámetro:
        ocurrencias (dict; clave: str; valor: int): diccionario cuyas claves son letras y los valores son las
        ocurrencias de cada una. Solo existe un único valor mayor que todos.
    -Valor retornado:
        (str) Clave que tiene asociado el mayor valor, o string vacío si el diccionario es vacío.
    """
        </pre>
    </summary>
    <pre>
    mayor_valor_parcial = -1
    clave_parcial = ""
    for clave, valor in ocurrencias.items():
        if valor > mayor_valor_parcial:
            mayor_valor_parcial = valor
            clave_parcial = clave
    return clave_parcial
    </pre>
</details>


<details>
    <summary>
        <pre>
def epoca_de_siembra(vegetales, mes):
    """
    Dado un diccionario conteniendo los meses de siembra de diversos vegetales y el nombre de un mes, retorna qué
    vegetales pueden sembrarse en ese mes.
    Ejemplo:
        epoca_de_siembra(vegetales={"espinaca": ["febrero","marzo"],
                                    "ajo": ["febrero","marzo","abril"],
                                    "berenjena": ["julio","agosto","septiembre"]},
                         mes="marzo")
        -> ["espinaca", "ajo"]
    -Parámetros:
        vegetales (dict; clave: str; valor: list, con elementos str): diccionario donde las claves son los nombres de
        diversos vegetales y los valores son listas con los meses en que cada vegetal puede sembrarse. 
        mes (str): el mes para el cual se busca saber qué vegetales pueden sembrarse.
    -Valor retornado:
        (list; elementos: str) Lista con los vegetales que pueden sembrarse en el mes.
    """
        </pre>
    </summary>
    <pre>
    vegetales_a_sembrar = []
    for clave, valor in vegetales.items():
        if mes in valor:
            vegetales_a_sembrar.append(clave)
    return vegetales_a_sembrar
    </pre>
</details>


<details>
    <summary>
        <pre>
def asentar_pago(socios, numero):
    """
    Dado un diccionario con la información de socios de un club y el número de un socio, modifica el diccionario para
    indicar que ese socio tiene los pagos de la cuota social al día. El diccionario tiene como claves los números de
    socio y, como valores, listas con los datos del socio: [nombre, teléfono, estado de pagos (True si están al día,
    False en caso contrario)].
    Ejemplo:
        asentar_pago(socios={423:["Juana Saavedra", 4523114, True],
                             289:["Estela Gimenez", 6345112, False],
                             657:["Lautaro Ruiz", 4767992, False]},
                     numero=289)
        -> {423:["Juana Saavedra", 4523114, True],
            289:["Estela Gimenez", 6345112, True],
            657:["Lautaro Ruiz", 4767992, False]}
    -Parámetros:
        socios (dict; clave: int; valor: list, con 3 elementos: str, int, bool): diccionario con los datos de los 
        ocios del club. Los números de socio son todos positivos.
        numero (int): número de socio a modificar.
    -Valor retornado:
        (dict; clave: int; valor: list, con 3 elementos: str, int, bool) Diccionario de socios en el cual se ha
        asentado el pago del socio correspondiente a numero, en caso de existir.
    """
        </pre>
    </summary>
    <pre>
    if numero in socios:
        socios[numero][2] = True
    return socios
    </pre>
</details>


<details>
    <summary>
        <pre>
def socios_morosos(socios):
    """
    Dado un diccionario con la información de socios de un club, retorna cuántos de ellos adeudan el pago de la cuota
    social. El diccionario tiene como claves los números de socio y, como valores, listas con los datos de ese socio:
    [nombre, teléfono, estado de pagos (True si están al día, False en caso contrario)].
    Ejemplo:
        socios_morosos(socios={423:["Juana Saavedra", 4523114, True],
                               289:["Estela Gimenez", 6345112, False],
                               657:["Lautaro Ruiz", 4767992, False]}) 
        -> 2
    -Parámetro:
        socios (dict; clave: int; valor: list, con 3 elementos: str, int, bool): diccionario con los datos de los
        socios del club. Las claves son todos números positivos.
    -Valor retornado:
        (int) Cantidad de socios que no tienen los pagos al día.
    """
        </pre>
    </summary>
    <pre>
    morosos = 0
    for datos in socios.values():
        if not datos[2]:
            morosos += 1
    return morosos
    </pre>
</details>


<details>
    <summary>
        <pre>
def eliminar_socio(socios, nombre_socio):
    """
    Dado un diccionario con la información de socios de un club y el nombre de un socio, lo elimina del diccionario. El
    diccionario tiene como claves los números de socio y, como valores, listas con los datos de ese socio: [nombre,
    teléfono, estado de pagos (True si están al día, False en caso contrario)]. Si el nombre dado no corresponde a
    ningún socio, el diccionario no se modifica. 
    Ejemplo:
        eliminar_socio(socios={423:["Juana Saavedra", 4523114, True],
                               289:["Estela Gimenez", 6345112, False],
                               657:["Lautaro Ruiz", 4767992, False]},
                       nombre_socio="Estela Gimenez")
        -> {423:["Juana Saavedra", 4523114, True], 657:["Lautaro Ruiz", 4767992, False]}
    -Parámetros:
        socios (dict; clave: int; valor: list, con 3 elementos: str, int, bool): diccionario con los datos de los
        socios del club. Las claves son todos números positivos mayores que cero. Los nombres de socios no se repiten
        en los valores del diccionario.
        socio (str): nombre y apellido del socio a eliminar.
    -Valor retornado:
        (dict; clave: int; valor: list, con 3 elementos: str, int, bool) Diccionario de socios del cual se ha eliminado
        el socio, en caso de existir.
    """
        </pre>
    </summary>
    <pre>
    numero_a_borrar = -1
    for numero, datos in socios.items():
        if nombre_socio == datos[0]:
            numero_a_borrar = numero
            break
    if numero_a_borrar != -1:
        del socios[numero]
    return socios
    </pre>
</details>


<details>
    <summary>
        <pre>
def romano_a_arabigo(romano):
    """
    Dado un número romano, retorna su equivalente en números arábigos en base decimal (usando reglas simplificadas).
    Las equivalencias utilizadas son: I=1, V=5, X=10, L=50, C=100, D=500, M=1000.
    Reglas:
    Una letra repetida hasta 3 veces: se suma.
    I delante de V o X significa restar 1.
    X delante de L o C significa restar 10.
    C delante de D o M significa restar 100.
    Ejemplo:
        romano_a_arabigo(romano="MCMLXXIV") -> 1974
    -Parámetro:
        romano (str): número romano a convertir. En mayúsculas. Es un número romano válido. Su equivalente en arábigo
        está entre 1 y 3999.
    -Valor retornado:
        (int) Número arábigo en base 10, equivalente a romano.
    """
        </pre>
    </summary>
    <pre>
    equivalencias = {'M':1000, 'D':500, 'C':100, 'L':50, 'X':10, 'V':5, 'I':1}
    arabigo = 0
    for i in range(len(romano)-1):
        if equivalencias[romano[i]] < equivalencias[romano[i+1]]:
            arabigo -= equivalencias[romano[i]]
        else:
            arabigo += equivalencias[romano[i]]
    arabigo += equivalencias[romano[len(romano)-1]]
    return arabigo
    </pre>
</details>


<details>
    <summary>
        <pre>
def numero_telefonico(telefono):
    """
    Dado un número de teléfono conteniendo letras, lo retorna con sus equivalentes en números. El número dado solo
    contendrá números, letras mayúsculas, '-', '(' y ')'. Solo se convertirán las letras, dejando los números y otros
    símbolos sin modificación.
    Las equivalencias utilizadas son:
    A, B, C = 2
    D, E, F = 3
    G, H, I = 4
    J, K, L = 5
    M, N, O = 6
    P, Q, R, S = 7
    T, U, V = 8
    W, X, Y, Z = 10
    Ejemplo:
        numero_telefonico(telefono="(325)444-TEST") -> "(325)444-8378"
    -Parámetro:
        telefono (str): un número telefónico que puede contener letras mayúsculas, números, guiones y paréntesis.
    -Valor retornado:
        (str) El número telefónico con sus letras convertidas a números.
    """
        </pre>
    </summary>
    <pre>
    resultado = ""
    equivalencias = {'2':"ABC", '3':"DEF", '4':"GHI", '5':"JKL", '6':"MNO", '7':"PQRS", '8':"TUV", '9':"WXYZ"}
    no_convertir = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '(', ')', '-')
    for caracter in telefono:
        if caracter in no_convertir:
            resultado += caracter
        else:
            for numero, letras in equivalencias.items():
                if caracter in letras:
                    resultado += numero
                    break
    return resultado
    </pre>
</details>


<details>
    <summary>
        <pre>
def cadenas_isomorficas(cadena1, cadena2):
    """
    Dadas dos cadenas de texto, define si son isomórficas o no. Dos cadenas, a y b, son isomórficas si puede
    reemplazarse cada carácter de a para obtener b. Todas las ocurrencias de un carácter deben ser reemplazadas
    con otro carácter, conservando su orden. No puede haber dos caracteres que sean reemplazados por el mismo carácter,
    pero sí es válido que un carácter se reemplace a sí mismo. Se asume que ambas cadenas tienen igual longitud y están
    compuestas por caracteres ascii válidos.
    Ejemplos:
        cadenas_isomorficas(cadena1="papel", cadena2="vivaz") -> True
        (Pues pueden hacerse los reemplazos 'p'='v'; 'a'='i'; 'p'='v'; 'e'='a'; 'l'='z').
        cadenas_isomorficas(cadena1="papel", cadena2="yoyos") -> False
        (Pues pueden hacerse los reemplazos 'p'='y'; 'a'='o'; 'p'='y'; pero al intentar reemplazar 'e'='o' sucede que
        la 'o' ya era reemplazo de la letra 'a').
    -Parámetros:
        cadena1 (str): una cadena de texto. len(cadena1) == len(cadena2).
        cadena2 (str): cadena para evaluar si es isomórfica con cadena1.
    -Valor retornado:
        (bool) True si las cadenas son isomórficas, False si no lo son.
    """
        </pre>
    </summary>
    <pre>
    equivalencias = {}
    ya_usadas = set()
    cantidad_iteraciones = len(cadena1)
    for i in range(cantidad_iteraciones):
        if cadena1[i] not in equivalencias:
            if cadena2[i] not in ya_usadas:
                equivalencias[cadena1[i]] = cadena2[i]
                ya_usadas.add(cadena2[i])
            else:
                return False
        else:
            if equivalencias[cadena1[i]] != cadena2[i]:
                return False
    return True
    </pre>
</details>


<details>
    <summary>
        <pre>
def patron_de_palabras(patron, palabras):
    """
    Dado un patrón y una cadena de texto compuesta por palabras, indica si la cadena sigue el patrón, de manera que
    haya una biyección entre cada letra del patrón y cada palabra de la cadena. Se considera que la cadena "sigue" el
    patrón si cada letra del mismo puede reemplazarse con una palabra de la cadena y una misma letra del patrón no
    reemplaza a dos palabras diferentes. Cada palabra de la cadena debe tener una letra correspondiente en el
    patrón y cada letra del patrón debe corresponder a una palabra.
    Ejemplos:
        patron_de_palabras(patron="xyyx", palabras="casa mar mar casa") -> True
        (Pues puede asociarse 'x'='casa'; 'y'='mar').
        patron_de_palabras(patron="xyyx", palabras="casa mar mar cerro") -> False
        (Pues 'x' no puede asociarse al mismo tiempo con 'casa' y con 'cerro').
    -Parámetros:
        patron (str): patrón a verificar. Solo contiene letras minúsculas.
        palabras (str): cadena con palabras. Las palabras estarán separadas por un único espacio y no habrá espacios al
        inicio ni al final de la cadena. palabras contendrá solo letras minúsculas y el carácter ' '.
    -Valor retornado:
        (bool) True si las palabras de la cadena siguen el patrón dado. False en caso contrario o si alguno de los
        strings es vacío.
    """
        </pre>
    </summary>
    <pre>
    pattern_matching = {}
    lista_de_palabras = palabras.split()
    if len(patron) != len(lista_de_palabras) or len(patron) == 0 or len(lista_de_palabras) == 0:
        return False
    for i in range(len(patron)):
        if patron[i] not in pattern_matching:
            pattern_matching[patron[i]] = lista_de_palabras[i]
        else:
            if pattern_matching[patron[i]] != lista_de_palabras[i]:
                return False
    return True
    </pre>
</details>