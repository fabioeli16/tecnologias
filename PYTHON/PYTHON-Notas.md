# PYTHON



<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
## Índice

- [Fundamentos](#Fundamentos)
  - [Archivos_principales](#Archivos_principales)
  - [Paquetes](#Paquetes)
  - [Modulos](#Modulos)
  - [Variables](#Variables)
  - [Operadores](#Operadores)
  - [Estructuras_datos](#Estructuras_datos)
  - [Contexto_Controlado](#Contexto_Controlado)
  - [Funciones](#Funciones)
  - [POO](#POO)

- [Ejercicios](#Ejercicios)
  - [importacion](#importacion)
  - [Funciones_uso](#Funciones_uso)
  - [Otros](#Otros)

- [Normalizacion](#Normalizacion)
  - [Objetivo normalizacion](#Objetivo)

- [Pendientes](#Pendientes)

- [Dudas](#Dudas)

- [Plan](#Plan)











<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
## Fundamentos


<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
### Archivos_principales

<!-- ---------------------------------------------------- -->

Concepto	  Qué es	                        Ejemplo
Módulo	    Un archivo .py	                texto.py
Paquete	    Una carpeta con módulos	        utilidades/
__init__.py	Marca e inicializa un paquete	  utilidades/__init__.py
.pyc	      Bytecode compilado en caché	    __pycache__/texto.cpython-312.pyc

<!-- ---------------------------------------------------- -->
PROMPT:
Python.
¿Que son los módulos, paquetes, los archivos compilados y  los archivos "__init__.py"?
¿Cual es la diferencia entre un script y un aplicativo en python?.


<!-- ---------------------------------------------------- -->
Estandar para nombrar modulos y otros elementos:

| Elemento  | Convención recomendada | Nota                   |
|---        |------------------------|------------------------|
| Paquete   | snake_case             | No empezar con numero  |
| Módulos   | snake_case             |
| Funciones | snake_case             |
| Variables | snake_case             |
| Clases    | PascalCase             |Eje: PersonaUnica

Nota: **No usar camel case en python**




<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
### Modulos

Un módulo es un archivo .py que contiene código: funciones, clases y variables. Cualquier archivo de Python ya es un módulo.


<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
### Paquetes

Se debe marcar un directorio como un paquete (package) y para controlar cómo se inicializa ese paquete cuando se importa, Para esto se usa _init.py




<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
### Variables


<!-- ---------------------------------------------------------- -->
SCOPE

A diferencia de C o Java, en Python los bloques if, for, while, with y try no crean un scope nuevo. Solo lo crean las funciones, las clases, los módulos y las comprensiones.

Resumen
Scope	          ¿Cuándo usarlo?
Local	          Siempre que puedas (es la opción por defecto)
Enclosing       (closure)	Estado pequeño y privado, o funciones que fabrican funciones
Global	        Solo constantes en MAYÚSCULAS, configuración e imports
Built-in	       No los sobrescribas: evita llamar a tus variables list, sum, id, input…

La idea central: datos que entran por parámetros, resultados que salen con return, y el estado compartido encapsulado en una clase.







<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
### Operadores


┌──────────┬────────────────────────────────────────┬─────────┬───────────┐
│ Operador │ Nombre                                 │ Ejemplo │ Resultado │
├──────────┼────────────────────────────────────────┼─────────┼───────────┤
│ +        │ Suma                                   │ 7 + 3   │ 10        │
├──────────┼────────────────────────────────────────┼─────────┼───────────┤
│ -        │ Resta                                  │ 7 - 3   │ 4         │
├──────────┼────────────────────────────────────────┼─────────┼───────────┤
│ *        │ Multiplicación                         │ 7 * 3   │ 21        │
├──────────┼────────────────────────────────────────┼─────────┼───────────┤
│ /        │ División (siempre da float)            │ 7 / 2   │ 3.5       │
├──────────┼────────────────────────────────────────┼─────────┼───────────┤
│ //       │ División entera (redondea hacia abajo) │ 7 // 2  │ 3         │
├──────────┼────────────────────────────────────────┼─────────┼───────────┤
│ %        │ Módulo (residuo de la división)        │ 7 % 2   │ 1         │
├──────────┼────────────────────────────────────────┼─────────┼───────────┤
│ **       │ Potencia                               │ 2 ** 3  │ 8         │
└──────────┴────────────────────────────────────────┴─────────┴───────────┘



<!-- ---------------------------------------------------------- -->

3. Ejercicio práctico: calculadora de notas

Enunciado: escribe un programa que:

Pida al usuario 3 notas (de 0.0 a 5.0).
Calcule el promedio y lo muestre con 2 decimales.
Revise que cada nota esté en el rango válido (0 <= nota <= 5).
Diga si el estudiante aprobó (promedio >= 3.0) o reprobó.
Muestre cuánto le falta para llegar a 3.0 si reprobó.
Bonus: use % y // para decir si la parte entera del promedio es par o impar, y calcule qué nota mínima necesitaría en un cuarto examen para que el promedio de las 4 notas sea 3.0.


























<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->

### Contexto_Controlado












<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
### Funciones


Dudas:
    .Los argumentos y retornos se pasan por referencia?














<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
### POO
<!-- -------------------------------------------------------- -->
-Todo es un objeto






























<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
## Ejercicios

<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
### importacion

- Ver ejercicios (3-importacion-entre-paquetes-definitiva) y (2-importacion-entre-paquetes)

- Las importaciones son objetos (2-importacion-entre-paquetes/main.py)

- Ejecutar siempre desde la raiz del proyecto (VER 3-importacion-entre-paquetes-definitiva/3-notas-importacion.md ## Ejecucion)

- Usar importacion absoluta a la raiz del proyecto (ver 3-importacion-entre-paquetes-definitiva/main.py)

- En proyectos medianos y grandes usar import porque hace el código más claro y evita conflictos de nombres.

- No usar * Porque no sabes qué nombres fueron importados


<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
### Funciones_uso

- Conclusiones
  1. Si se retorna varios valores definir explicitamente la tupla. ver tecnologias\PYTHON\funciones\1-basico\paquete_funciones\funciones.py



<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
### Otros
-Funcion all y any

-Funcion isInstance y sus argumentos

-Expresion generadora





















<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
## Normalizacion

<!-- ------------------------------------------------------ -->
### Objetivo

-Se trata de aprender Python utilizando los elementos del lenguaje que tiene en comun con los otros lenguajes, como por ejemplo los conceptos que comparte con: JAVA, JAVASCRIPT.

-Ejemplo:
  .En vez de usar WITH para controlar el uso apropiado de recursos en un contexto, se usaria los metodos propios del objeto del recurso y estructuras de manejo de excepciones.










<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
## Pendientes

- Comprensiones y generadores
  .En resumen, la principal ventaja de las comprensiones es la legibilidad, y la velocidad es un beneficio extra. Úsalas cuando el código quede más claro, no solo para ganar milisegundos.
  .Si la expresión es costosa, la diferencia desaparece. Por ejemplo, si cada elemento llama a una función pesada o consulta una base de datos, el tiempo lo consume esa operación y no el ciclo.
  .No gastan menos memoria. Una comprensión de lista crea la lista completa igual que el for.
  .Para ahorrar memoria, usa generadores ( ), que producen los valores uno a uno sin guardarlos todos:

- Objetos:
  .Que son los objetos mutables e inmutables
  .Como eliminar de memoria un objeto que ya cumplio su funcion

- DUDA SOBRE HILOS:
  .Cada vez que creo un hilo para jecutar una funcion se crea un objeto que duplica el codigo de esa funcion? Si es asi, es mas conveniente conservar un mismo hilo y ejecutarlo y detenerlo?

- Funcion all

- Funcion isInstance y sus argumentos

- Expresion generadora
  Estas expresiones reducen el espacio ocupado en memoria?

- Expresiones generadoras vs compresiones de listas

- Existe una forma de calcular el espacio en memoria que ocupa un script

- Uso de dataclass para tipado estricto

- Uso de * para variables. EJE: 
  mi_tupla: Tuple = (1,2,3)
  *mi_tupla


- HERRAMIENTAS DE MEDICION DE EJECUCION DE CODIGO
  import timeit

<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
## Dudas


- Expresion generadoras
  Estas expresiones reducen el espacio ocupado en memoria?

- Existe una forma de calcular el espacio en memoria que ocupa un script



<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
## Plan



<!-- ------------------------------------------------------ -->
-Módulo 1 · Fundamentos (1 HORA X DIARA X 1 SEMANA)		11 AL 15 DE NOVIEMBRE		DE 07 A 08 DE LA NOCHE

.Variables y tipos básicos: int, float, str, bool, None
.Type hints y mypy
.Operadores aritméticos, de comparación y lógicos
.Entrada y salida con input(), print() y f-strings
.ESTRUCTURAS DE CONTROL
	Condicionales: if / elif / else y match
	Bucles: for, while, range, break y continue
.Comprensiones

.Práctica: calculadora, adivina el número, tabla de multiplicar

<!-- ------------------------------------------------------ -->

Módulo 2 · Estructuras de datos (1 semana)
.Listas, tuplas, diccionarios y conjuntos
.Indexación y slicing
.Métodos comunes de cada estructura
.Comprensiones de listas y de diccionarios
.Cuándo conviene usar cada estructura
.Práctica: agenda de contactos, contador de palabras en un texto

<!-- ------------------------------------------------------ -->

Módulo 3 · Funciones y modularidad (1 semana)
Definir funciones, parámetros, return y valores por defecto
*args, **kwargs y alcance de variables
Funciones lambda, map, filter y sorted con key
Módulos, paquetes e import
La biblioteca estándar: math, random, datetime, os, pathlib
Práctica: separar un programa anterior en varios módulos


<!-- ------------------------------------------------------ -->

Módulo 4 · Archivos y errores (1 semana)
Leer y escribir archivos de texto con with open(...)
Trabajar con CSV y JSON
Excepciones: try / except / else / finally y lanzar las tuyas con raise
Depuración con print, el debugger de VS Code y logging
Práctica: gestor de gastos que guarda los datos en JSON

<!-- ------------------------------------------------------ -->

Módulo 5 · Programación orientada a objetos (2 semanas)
Clases, objetos, __init__ y self
Atributos y métodos de instancia y de clase
Herencia, polimorfismo y composición
Métodos especiales: __str__, __repr__, __eq__, __len__
@property y dataclasses
Práctica: sistema de inventario o de biblioteca

<!-- ------------------------------------------------------ -->

Módulo 6 · Python intermedio (2 semanas)
Iteradores y generadores (yield)
Decoradores
Context managers
Type hints y mypy
Módulos collections (Counter, defaultdict, deque) e itertools
Expresiones regulares (re)

<!-- ------------------------------------------------------ -->

Módulo 7 · Buenas prácticas (1 semana, en paralelo)
Estilo de código con PEP 8, y las herramientas ruff y black
Pruebas automáticas con pytest
Control de versiones con Git y GitHub
Estructura de un proyecto y el archivo requirements.txt o pyproject.toml

<!-- ------------------------------------------------------ -->

Módulo 8 · Especialización (elige una o dos ramas)
Rama	Qué aprender
Datos	NumPy, pandas, matplotlib/seaborn, SQL con sqlite3 o SQLAlchemy
Matemáticas y ciencia	NumPy, SymPy, SciPy, gráficas 3D
Web / APIs	requests, FastAPI o Flask, bases de datos
Automatización	Scripts de sistema, web scraping (BeautifulSoup), Excel con openpyxl
