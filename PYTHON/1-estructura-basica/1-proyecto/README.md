
-----------------------------------------------------------------------------------------------
1-ESTRUCTURA

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
├── .env                      # Variables de entorno
├── .gitignore
├── requirements.txt
├── README.md
└── arrancarenwindows.ps1




-----------------------------------------------------------------------------------------------
2-EJECUTAR
cd tecnologias\PYTHON\1-estructura-basica\1-proyecto
.\arrancarenwindows.ps1









