# ESPAÑOL
*[(scroll down or click here for English version)](#english)*

## Objetivo

Este proyecto intenta ser una herramienta con la cual practicar desafíos (o ejercicios) de programación, desde un nivel
inicial, usando Python 3.

Los ejercicios se enfocan en desarrollar habilidades algorítmicas y de razonamiento lógico así como aprender a trabajar
con las bases de la programación y los tipos de datos fundamentales. No se centra en aprender los detalles del lenguaje
Python. Es por ello que se alienta a que desarrolles tus propias soluciones evitando utilizar algunas herramientas
que provee el lenguaje.

Los desafíos se dividen en temas para ayudarte a practicar ciertos tipos y estructuras de datos, pero eso no excluye
otras posibles soluciones (que podrían incluso ser más eficientes).

## Cómo está planteado el proyecto

Se presenta una serie de funciones incompletas (sin su cuerpo), y cierta documentación que muestra cómo debería
comportarse cada función. Además, cada función tiene una serie de pruebas (tests) unitarias. Necesitarás completar el
cuerpo de las funciones de acuerdo a la consigna de cada una, de manera que todas las pruebas pasen.

Al ejecutar el proyecto, se correrán las pruebas para evaluar si el resultado es el esperado.

Los ejercicios están divididos en las siguientes categorías o temas: *números, strings, listas y tuplas, conjuntos y
diccionarios*; lo que significa que se sugiere resolverlos utilizando estos tipos de datos con el fin de practicar las
bases. Pero también pueden resolverse en otras formas, siempre que los tests pasen exitosamente.


## Cómo usar este proyecto

Python 3 deberá estar instalado en el sistema (la versión deberá ser superior a la 3.4).

Asumiendo que usarás la versión en español, primero ingresa en la carpeta **ESP**. Ésta contiene dos carpetas: **src** y
**tests**. La carpeta [**src**](/ESP/src) contiene archivos relacionados a cada tema (de los mencionados arriba) y en
cada archivo se encuentran varias funciones con el cuerpo vacío, que deberás completar con tu código. La carpeta
[**tests**](/ESP/tests) incluye las pruebas unitarias y su contenido no debe ser modificado. Al agregar el cuerpo de 
alguna función en */ESP/src*, podrás ejecutar las pruebas unitarias para determinar si tu algoritmo es correcto.

Inicialmente, todas las pruebas deberían fallar. El objetivo es escribir el cuerpo de las funciones (reemplazando la
instrucción "pass" por tu código) para hacer que las pruebas pasen. Entonces, luego de agregar el cuerpo a una o más
funciones, necesitarás ejecutar las pruebas para ver si pasan o fallan. Cuando las pruebas pasen, mostrarán "ok" en su
resultado; si alguna prueba falla, mostrará qué función se ejecutó, qué argumentos se usaron para invocarla, qué retornó
y cuál era el valor de retorno esperado.


### Soluciones

Dentro de la carpeta **ESP** también se encuentra un archivo llamado
[**soluciones_propuestas.md**](/ESP/soluciones_propuestas.md) que muestra código con posibles resoluciones a cada uno de
os ejercicios. De ninguna manera esto implica que sean las únicas soluciones ni tampoco las más eficientes. Es solo
información a modo de ejemplo, que podría utilizarse como punto de partida en caso de no poder resolver alguno de los
desafíos. El archivo está escrito con [markdown](https://es.wikipedia.org/wiki/Markdown) de manera de poder ocultar el 
código y dejar visible únicamente la
consigna, para poder seleccionar cuál de las funciones se desea ver. Se recomienda visualizar este archivo en un
programa que interprete `markdown` (por ejemplo, un navegador web).


### Cómo escribir el código

Completar el cuerpo de cada función de manera que cumpla con lo que se espera de ella, según la documentación (no
olvides eliminar la instrucción "pass") y las pruebas unitarias. La documentación de la función indica 
cuál es su objetivo, qué representan y de qué tipo son los parámetros y qué se espera que la función retorne. También es
recomendable usar las pruebas unitarias de la carpeta **tests** para guiarte en el proceso de escribir el código (pero 
no se espera que modifiques estas pruebas de ninguna forma). Solo se debe agregar contenido a las funciones, sin 
modificar nada más (nombre, parámetros o documentación de las funciones) ni el resto del archivo, ni las pruebas 
unitarias.


### Orden de los temas

Aunque es posible comenzar por cualquiera de los temas propuestos, existe un orden que permite resolverlos con
dificultad incremental:

1. Números
2. Strings
3. Listas y tuplas
4. Conjuntos y diccionarios

Esto implica que los ejercicios del módulo numeros.py pueden resolverse sin utilizar strings, listas, conjuntos ni
diccionarios. Los ejercicios del módulo strings pueden incluir manipulación de números. Los ejercicios de listas y
tuplas pueden incluir manipulación de números y de strings. Los ejercicios de conjuntos pueden incluir listas, strings
y números. Finalmente, los ejercicios de diccionarios pueden incluir cualquiera de los temas anteriores (conjuntos,
listas, tuplas, strings y números).


## Ejecutar las pruebas

Para probar tu código y evaluar tus algoritmos, es posible correr las pruebas para una sola función (esto es, un solo 
ejercicio), para todas las funciones de una categoría (números, strings, listas & tuplas, conjuntos & diccionarios), o 
para todas las categorías a la vez. Para esto se puede utilizar una terminal o también configurar el IDE de preferencia.
En el caso de la terminal, se deberá cambia al directorio ("CD") de la carpeta del proyecto (ejemplo: si el proyecto se 
encuentra en C:/miusuario/proyecto será esa la carpeta donde deberás situarte) y luego ejecutar el comando 
correspondiente. Se debe tener en cuenta que, dependiendo de cómo se haya instalado el intérprete, podría ser necesario 
reemplazar el comando "python" por "python3" o algún otro comando. En caso de utilizar Pycharm, las configuraciones se
crearán desde el menú superior "Run > Edit Configurations" y luego "Add new run configuration".

### Ejecutar las pruebas de una función/ejercicio:

En la terminal, ejecutar el siguiente comando:

`python -m unittest -v ruta/al/archivo.py -k funcion_de_pruebas`

donde *ruta/al/archivo.py* debe reemplazarse con la ruta desde la carpeta raíz del proyecto hasta el archivo de 
pruebas que contiene las pruebas que se ejecutarán (ej.: **ESP/tests/tests_numeros.py**) y *funcion_de_pruebas* debe 
reemplazarse con la función de pruebas a ejecutar (ej.: **test_factorial**). Por ejemplo, para ejecutar las pruebas de 
la función del ejercicio *factorial* de la categoría *numeros*:

`python -m unittest -v ESP/tests/tests_numeros.py -k test_factorial`

Para hacer lo mismo utilizando una configuración de Pycharm, selecciona la opción "Module name" y luego da clic en "..." 
para abrir un nuevo diálogo donde deberás escribir el nombre del archivo de la categoría a ejecutar (ej.: 
**tests_numeros**) y seleccionarlo del menú desplegable. Luego, en "Additional Arguments", ingresar "-k 
test_function_name" (reemplazando con el nombre de la función a ejecutar). Verifica que la opción "Add contents to 
PYTHONPATH" esté tildada.


### Ejecutar todas las pruebas de una categoría:

`python -m unittest -v ruta/al/archivo.py`

donde *ruta/al/archivo.py* debe reemplazarse con la ruta desde la carpeta raíz del proyecto hasta el archivo de 
pruebas que contiene las pruebas que se ejecutarán (ej.: **ESP/tests/tests_numeros.py**). Por ejemplo, para ejecutar las
pruebas de los ejercicios de la categoría *numeros*.

`python -m unittest -v ESP/tests/tests_numeros.py`

Para hacer lo mismo utilizando una configuración de Pycharm, selecciona la opción "Module name" y luego da clic en "..." 
para abrir un nuevo diálogo donde deberás escribir el nombre del archivo de la categoría a ejecutar (ej.: 
**tests_numeros**) y seleccionarlo del menú desplegable. Verifica que la opción "Add contents to PYTHONPATH" esté 
tildada.


### Ejecutar las pruebas de más de una categoría a la vez:

Para ejecutar las pruebas de más de una categoría (o incluso todas las categorías al mismo tiempo), corre el archivo 
**ejecutar_tests.py**. En caso de ejecutar mediante terminal o línea de comandos, primero se deberá configurar la 
variable de entorno **PYTHONPATH** para que apunte a la carpeta del proyecto. Para evitar configurarla de manera 
definitiva, existe la opción de hacerlo de forma temporal, en cada sesión de la terminal. Para ello abre la terminal, CD
al directorio del proyecto y luego ejecuta el siguiente comando:

`export PYTHONPATH="$PWD"` si estás en Linux/Mac, o

`set PYTHONPATH=%cd%` si estás en Windows.

A continuación, corre **ejecutar_tests.py** usando:

`python ESP/ejecutar_tests.py`

Si se utiliza Pycharm, será suficiente con correr el archivo **ejecutar_tests.py**, seleccionándolo y luego presionando 
Ctrl+Mayús+F10 o simplemente dando clic al botón "Run".

Si deseas obviar la ejecución de alguna categoría de pruebas, comenta (anteponiendo un #) la línea correspondiente en 
el archivo **ejecutar_tests.py**. La línea a comentar se verá como esta: 
`suite.addTests(loader.loadTestsFromModule(categoria_a_obviar))`.


## Abordaje sugerido

Al escribir código con fines profesionales es más probable que muchas de las tareas incluidas en estos ejercicios se
resuelvan mediante herramientas predefinidas del lenguaje. Pero se recomienda que en este proyecto intentes evitar
usarlas y crees tus propios algoritmos, a fin de ejercitar el razonamiento lógico y las estructuras básicas de la
programación. Con esa intención, en algunas funciones se sugiere evitar ciertas herramientas y encontrar soluciones
alternativas.

Todos los desafíos planteados en este proyecto pueden ser resueltos sin necesidad de importar bibliotecas o módulos
adicionales (solo modificando el cuerpo de cada función).

Además, las categorías planteadas sugieren ciertos tipos y estructuras de datos para ayudar a reforzar el pensamiento
algorítmico, incluso cuando podrían encontrarse soluciones alternativas más eficientes. De todas formas, nada impide que
resuelvas los ejercicios de la forma en que te parezca mejor, ya que estos temas son solo una sugerencia para guiar la 
práctica.

También pueden utilizarse los casos de prueba para resolver los desafíos mediante "desarrollo guiado por pruebas" (en
inglés, "Test-Driven-Development" o "TDD"), de manera que las pruebas guíen el desarrollo de los algoritmos.


## Requerimientos

Solo se requiere Python 3, el cual incluye la biblioteca unittests.

El proyecto fue probado con Python 3.9, aunque también debería funcionar con otras versiones de Python 3 (superiores a 
3.4).


---
# ENGLISH

## Goal

This is a project you can use to practise programming challenges (or exercises) for beginners, using Python 3.

Exercises are mainly intended to help develop algorithmic and logical reasoning skills as well as learn how to work with
programming fundamentals. It doesn't focus on learning the perks of the Python language. That's why in most cases you're
encouraged to build your own solution without using some pre-made solutions that Python offers.

Challenges are divided into topics to help you practise with specific data types and structures, but that doesn't mean 
there can't be other possible solutions (that might even be more efficient).

### How the project is organized

The project includes a variety of functions where their body is missing, and some documentation showing how each
function should behave. Also, each function has a set of unit tests. You'll need to fill in the blanks (that is: write
the function body) without modifying anything else, to get all tests to pass.

When the project is executed, tests are run to evaluate if the functions return the expected result in each case.

Exercises are divided into topics: *numbers, strings, lists and tuples, sets and dictionaries*; meaning you're 
encouraged to solve challenges using these data types in order to practise programming fundamentals. But they can be
solved in other ways too, as long as the tests pass successfully.


## How to use the project

Python 3 needs to be installed (version 3.4+).

Assuming you'll be using the English version of the project, first go into the **ENG** folder. In there, there are two 
folders: **src** and **tests**. The [**src**](/ENG/src) folder contains files related to a specific topic (from the
ones mentioned above), and these files contain functions with an empty body (this is where you'll add your code).
The [**tests**](/ENG/tests) folder contains unit tests and should not be modified at all. After adding a function body
in one of the files in */ENG/src*, you'll be able to run its unit tests to check if your algorithm is correct.

At first, all tests are expected to fail. The goal is to add bodies to these functions (replacing the "pass" statement 
with your algorithms) to get the tests to pass. So after writing code for one or more functions, you'll need to run the
tests to see if they pass or fail. When tests pass, they will show an "ok" result; if a test fails, it will show which 
function it ran, the arguments used to call it, what it returned and what was the expected return value.


### Solutions
The **ENG** folder also contains a file called [**proposed_solutions.md**](/ENG/proposed_solutions.md) which includes
code that might be a solution for each one of the exercises. This doesn't imply those are the only or even the most
efficient solutions. It's just example code that could be useful as a starting point in case you cannot solve any of the
challenges. The file was created with [markdown](https://en.wikipedia.org/wiki/Markdown) so that the code can be hidden
from view, leaving only the function documentation visible, so you can click on the function you wish to view the code 
for. This file should be opened with a program that renders `markdown` (a web browser, for example).


### How to write the code

Fill in the body of each function in a way that makes it behave as the documentation states (remember to remove the 
"pass" statement and add your code instead), and that fulfills the unit tests for that function. Function documentation 
is included between triple quotes (""") and designates what the function goal is, what's the data type of each parameter
and what they represent, and what's the expected return value. You can also check the unit tests included in the 
**tests** folder to guide your coding task (but you're not expected to modify these tests at all). Only the function 
body needs to be added, without modifying anything else (name, parameters, documentation, etc.) in the function, the 
overall file or the unit tests file.


### Topic order

It's possible to start with any of the included topics (files), but there's a preferred order that allows to solve 
challenges with increasing difficulty:

1. Numbers
2. Strings
3. Lists and tuples
4. Sets and dictionaries

This means that exercises in the numbers.py module can be solved without using strings, lists, tuples, sets or 
dictionaries. But the challenges in strings.py module may include number as well as string manipulation. Challenges in 
the list and tuples module can include number and string manipulation. Then challenges with sets can include working 
with lists, tuples, strings and numbers. Finally, the dictionary challenges can include any of the previous types 
(numbers, strings, lists, tuples and sets).  


## Run tests

To test your code, you can either run tests for a single function (that is, all test cases for a single challenge or 
exercise), for all the functions in a category (numbers, strings, lists & tuples, sets & dictionaries) or run tests for
more than one category at once. You can use a terminal for these or create a configuration in an IDE. In case it's done
in a terminal, you'll first need to change directory ("CD") to the root project folder (e.g.: if the project was 
downloaded into C:/myusername/project that will be the folder you'll need to CD into) and then run the command. Keep in 
mind that command "python" might need to be replaced with "python3" or something else, depending on how Python is 
installed. In case of using Pycharm, configurations can be created from top menu "Run > Edit Configurations" and then 
"Add new run configuration".

### Run a test for a single function/exercise:

In terminal, enter the following command:

`python -m unittest -v path/to/test/file.py -k test_function_name`

where *path/to/test/file.py* should be replaced with the path from project root to the test file containing the function
(e.g.: **ENG/tests/tests_numbers.py**) and *test_function_name* should be replaced with the test function to be executed
(e.g.: **test_factorial**). As an example, to run tests for challenge function *factorial* in the *numbers* category:

`python -m unittest -v ENG/tests/tests_numbers.py -k test_factorial`

To do the same using a Pycharm cofiguration, select option "Module name" and then click on "..." to open a new dialog 
where you'll need to type the name of the category file (e.g.: **tests_numbers**) and select from dropdown. Then, in 
"Additional Arguments", enter "-k test_function_name" (replacing with the actual function name). Verify "Add contents to
PYTHONPATH" option is checked.


### Run all tests in a category:

In terminal, enter the following command: 

`python -m unittest -v path/to/test/file.py`

where *path/to/test/file.py* should be replaced with the path from project root to the test file containing the function
(e.g.: **ENG/tests/tests_numbers.py**). As an example, to run tests for challenges in the *numbers* category:

`python -m unittest -v ENG/tests/tests_numbers.py`

To do the same using a Pycharm cofiguration, select option "Module name" and then click on "..." to open a new dialog 
where you'll need to type the name of the category file (e.g.: **tests_numbers**) and select from dropdown. Verify "Add 
contents to PYTHONPATH" option is checked.


### Run tests in more than one category at the same time:

To run more than one category at once (or even run all categories), execute the **run_tests.py** file, which will output
the results of the unit tests. In case you'd like to usa a terminal, you'll first need to set the PYTHONPATH environment 
variable to the project folder. To avoid setting it permanently, it's also possible to set the variable temporarily, 
just for the current session (it will need to be done each time the terminal is closed and re-opened): open terminal, 
"CD" into the root project folder and then run the following command:

`export PYTHONPATH="$PWD"` if you're on Linux/Mac, or

`set PYTHONPATH=%cd%` if you're on Windows

Next, execute **run_tests.py** using this command:

`python ENG/run_tests.py` 

If Pycharm is used, you'll just need to run the **run_tests.py** (for example, by selecting it and then pressing 
Ctrl+Shift+F10 or just clicking on the "Run" button).

By default, **run_tests.py** will run tests for all categories. But it's possible to skip test categories from executing 
by commenting out (using a leading #) the related lines in the file. These lines look like this: 
`suite.addTests(loader.loadTestsFromModule(category_to_skip))`.


## Recommended approach

When writing professional code most likely many of the tasks in these challenges are solved by just using built-in 
tools. But the recommended approach here is to avoid using them and writing our own algorithms instead, to exercise 
logical reasoning and programming fundamentals. This is why some functions suggest avoiding some specific tools.

All the challenges in the project can be solved without the need of importing any libraries (so only the function bodies
should be modified).

Also, the challenge topics suggest specific data types and structures to help improve algorithmic thinking, even when 
there might be more efficient solutions. Feel free to solve the problems in any way you think best, as this is only a 
suggestion.

In addition, test cases can be used to solve the challenges in a Test-Driven-Development ("TDD") fashion, by using unit 
tests to guide development.


## Requirements

Only Python 3 is needed, which includes the unittest library.

The project has been tested under Python 3.9, although it should run with other Python 3 variants (3.4 or newer).
