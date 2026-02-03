





Bloques de código
<pre> ```bash pip install -r requirements.txt ``` </pre>



Título

Descripción

Estructura del proyecto

Requisitos

Instalación

Uso

Notas importantes



## 📑 Contenido
- [Instalación](#-instalación)
- [Uso](#-uso)




**********************************************************************************************************************************************************************
1-ESTRUCTURA

proyecto/
│
│
├── app/                    # Código fuente principal
│   ├── __init__.py         #Archivo de modulo
│   ├── main.py             # Punto de entrada de la aplicación
│   │
│   ├── config/             # Configuraciones
│   │   ├── __init__.py
│   │   └── settings.py
│   │
│   └── models/             # Modelos (clases, entidades, esquemas)
│       ├── __init__.py
│       └── modelo.py
│
│
├── venvwindows/                     # Entorno virtual (NO se versiona)
├── .env                      # Variables de entorno
├── .gitignore
├── requirements.txt
├── README.md
└── arrancarenwindows.ps1





**********************************************************************************************************************************************************************
2-EJECUCION

---------------------------------------------------------------
EJECUTAR WINDOWS
#SE CREA EL ARCHIVO .env con las mismas variables definidas en (.env.example) y asignandoles valor
tecnologias\PYTHON\1-estructura-basica\1-proyecto\.env

# SE INGRESA A LA RUTA (SE DEBE CAMBIAR DEPENDIENDO DE LA MAQUINA DONDE SE EJECUTA) 
cd tecnologias\PYTHON\1-estructura-basica\1-proyecto
cd C:\1-Yo\Programacion\repositorios\tecnologias\PYTHON\1-estructura-basica\1-proyecto

#SE EJECUTA LA SHELL
.\arrancarenwindows.ps1





---------------------------------------------------------------




