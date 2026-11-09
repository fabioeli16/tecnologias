# Mi Documento

## Índice

- [Introducción](#introducción)
- [Instalación](#instalación-Ejecucion)
- [Prompts](#Prompts)
- [Dudas](#Dudas)
- [Conclusiones](#Conclusiones)




<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
## Introducción

-El objetivo es aprender sobre el alcance de las variables dentro de un mismo modulo 

-el scope (alcance) define desde qué partes del código se puede ver y usar una variable. Python resuelve los nombres con la regla LEGB, buscando en este orden:
L – Local: dentro de la función actual.
E – Enclosing: en las funciones que envuelven a la actual (funciones anidadas).
G – Global: a nivel del módulo (el archivo .py).
B – Built-in: nombres predefinidos de Python (len, print, range…).

<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
## Instalación-Ejecucion


- Preparacion inicial: SE CREA EL ARCHIVO .env con las mismas variables definidas en (.env.example) y asignandoles valor
tecnologias\PYTHON\1-estructura-basica\1-proyecto\.env

- SE INGRESA A LA RUTA (SE DEBE CAMBIAR DEPENDIENDO DE LA MAQUINA DONDE SE EJECUTA) 
cd tecnologias\PYTHON\1-estructura-basica\1-proyecto
cd C:\1-Yo\Programacion\repositorios\tecnologias\PYTHON\3-variables\2-scope\2-1-SCOPE

- SE EJECUTA LA SHELL
.\arrancarenwindows.ps1





<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
# Prompts











<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
# Dudas 






<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
# Conclusiones


Resumen
Scope	        ¿Cuándo usarlo?
Local	        Siempre que puedas (es la opción por defecto)
Enclosing       (closure)	Estado pequeño y privado, o funciones que fabrican funciones
Global	        Solo constantes en MAYÚSCULAS, configuración e imports
Built-in	       No los sobrescribas: evita llamar a tus variables list, sum, id, input…

La idea central: datos que entran por parámetros, resultados que salen con return, y el estado compartido encapsulado en una clase.