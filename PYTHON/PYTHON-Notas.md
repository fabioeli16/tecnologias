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












<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
## Fundamentos


<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
### Archivos_principales

PROMPT:
Python.
¿Que son los módulos, paquetes, los archivos compilados y  los archivos "__init__.py"?
¿Cual es la diferencia entre un script y un aplicativo en python?.

<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
### Paquetes

Se debe marcar un directorio como un paquete (package) y para controlar cómo se inicializa ese paquete cuando se importa, Para esto se usa _init.py

<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
### Modulos

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
<!-- +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++ -->
### Variables








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

<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
## Dudas


- Expresion generadoras
  Estas expresiones reducen el espacio ocupado en memoria?

- Existe una forma de calcular el espacio en memoria que ocupa un script
