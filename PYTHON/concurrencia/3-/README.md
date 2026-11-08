<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->

# BASE
## Índice

- [Descripcion](#Descripcion)
- [Estructura](#Estructura)
- [Ejecucion](#Ejecucion)
- [Prompts](#Prompts)
- [Dudas](#Dudas)
- [Conclusiones](#Conclusiones)





<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
# Descripcion

- Compatible solo con windows

- Ejercicios para entender la concurrencia

- 


<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
# ESTRUCTURA

-Sugerida

proyecto/
│
│
├── app/                    # Código fuente principal
│   ├── __init__.py
│   ├── main.py             # Punto de entrada de la aplicación
│   │
│   ├── config/             # Configuraciones
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   ├── services/           # Lógica de negocio
│   │   ├── __init__.py
│   │   └── servicio.py
│   │
│   ├── utils/              # Funciones auxiliares
│   │   ├── __init__.py
│   │   └── helpers.py
│   │
│   └── models/             # Modelos (clases, entidades, esquemas)
│       ├── __init__.py
│       └── modelo.py
│
│
├── venvwindows/                     # Entorno virtual (NO se versiona)
├── .env                             # Variables de entorno
├── .gitignore
├── requirements.txt
├── README.md
└── arrancarenwindows.ps1





<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
## Ejecucion

- Preparacion inicial: SE CREA EL ARCHIVO .env con las mismas variables definidas en (.env.example) y asignandoles valor
C:\1-Yo\Programacion\repositorios\tecnologias\PYTHON\concurrencia\3-\.env

- SE INGRESA A LA RUTA (SE DEBE CAMBIAR DEPENDIENDO DE LA MAQUINA DONDE SE EJECUTA) 
cd PYTHON\concurrencia\3-
cd C:\1-Yo\Programacion\repositorios\tecnologias\PYTHON\concurrencia\3-

- SE EJECUTA LA SHELL
.\arrancarenwindows.ps1




<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
# Prompts

- CHATGPT   
python. Como funciona la concurrencia en python. script de ejemplo simple y util donde se pueda usar la concurrencia.


python. 
Como funciona la concurrencia en python. 
Cuales son las librerias o metodos que existen en python para usar concurreencia.
script de ejemplo simple y util donde se pueda usar la concurrencia por cada metodo.

Python.
Como valido que mi version de python tiene o no activo el GIL.




<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
# Dudas 






<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
<!-- ******************************************************************************************************************************-->
# Conclusiones

En builds free-threaded, el GIL se puede forzar a encender/apagar con la variable de entorno PYTHON_GIL o el flag -X gil:


| Método           | Librería                              | Ideal para               |
| ---------------- | ------------------------------------- | ------------------------ |
| Hilos            | threading                             | I/O (red, archivos, BD)  |
| Pool de hilos    | concurrent.futures.ThreadPoolExecutor | Muchas tareas I/O        |
| Async/Await      | asyncio                               | Miles de operaciones I/O |
| Procesos         | multiprocessing                       | CPU intensiva            |
