##################################
#     TEMA: LISTAS Y TUPLAS      #
##################################


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass


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
    pass
    

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
    pass


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
    pass


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
    pass


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
    pass
    

def suma_cada_n(numeros, n):
    """
    Dada una lista de números y un número positivo n, retorna la suma de cada n elementos de la lista.
    n puede ser mayor que la longitud de la lista y no necesariamente es un múltiplo de esta longitud.
    n no puede ser 0.
    Si n es mayor que la longitud de la lista, retorna 0.
    Sugerencia: evitar el uso de sum().
    Ejemplo:
        suma_cada_n(numeros=[5, 2, 1, 6, 4, 9, 3, 7, 8], n=3) -> 18
        (Pues 1+9+8=18).
        suma_cada_n(numeros=[1.5, 2, -3, 4], n=5) -> 0
    -Parámetros:
        numeros (list; elementos: numéricos): lista de números.
        n (int): número entero mayor que 0.
    -Valor retornado:
        (int) Suma de los elementos de numeros, comenzando por el elemento en la posición n y saltando de a n
        posiciones. 0 si n es mayor que la cantidad de elementos en la lista.
    """
    pass


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
    pass
        

def desanidar(listas):
    """
    Dada una lista cuyos elementos son listas, retorna una nueva lista con un nivel menos de anidamiento.
    Sugerencia: evitar usar bucles anidados.
    Ejemplos:
        desanidar(listas=[[1, 0, 4], ["a", "b"], [True, False, True, True]])
        -> [1, 0, 4, "a", "b", True, False, True, True]
        desanidar(listas[[], ["a", "b"]]) -> ["a", "b"]
    -Parámetro:
        listas (list; elementos: list, con elementos heterogéneos): una lista que contiene listas como elementos (los
        elementos de éstas pueden ser de cualquier tipo).
    -Valor retornado:
        (list; elementos: heterogéneos) Una nueva lista cuyos elementos son directamente los elementos que están
        contenidos dentro de las listas anidadas dentro de la pasada por parámetro, sin alterar su orden.
    """
    pass


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
    pass


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
    pass


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
    pass


def buscar_destino(boletos, ciudades, numero_boleto):
    """
    Dado el número de un boleto de viaje, retorna el país de destino.
    La función recibe una lista con boletos de viaje (de cada boleto se tiene el número y la ciudad destino) y otra
    lista con datos de ciudades (de cada una se tiene el nombre de ciudad y país donde está ubicada). Además, recibe un
    número de boleto. De acuerdo el número de boleto ubicará la ciudad destino y, de acuerdo a la ciudad destino,
    retornará el país al que pertenece. Si el número de boleto no se encuentra en la lista, retornará None.
    Sugerencia: utilizar la función buscar_pais() definida anteriormente.
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
    pass
