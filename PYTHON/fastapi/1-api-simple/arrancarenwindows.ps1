# ================================
# Script de arranque para Windows
# ================================

# VARIABLES POWER SHELL
$VENV_NAME = "venvwindows"
$PYTHON_EXE = "python"
$PROJECT_ROOT = Split-Path -Parent $MyInvocation.MyCommand.Path
$VENV_PATH = Join-Path $PROJECT_ROOT $VENV_NAME
$ACTIVATE_SCRIPT = Join-Path $VENV_PATH "Scripts\Activate.ps1"
$REQUIREMENTS = Join-Path $PROJECT_ROOT "requirements.txt"
$MAIN_APP = Join-Path $PROJECT_ROOT "app\main.py"
$ENV_FILE = Join-Path $PROJECT_ROOT ".env"

# VARIABLES DE ENTORNO TEMPORALES
$env:PROJECT_ROOT_ENV = $PROJECT_ROOT


# 0- VALIDA EXISTENCIA DE .ENV
if (-not (Test-Path $ENV_FILE)) {
    Write-Host "ERROR: No existe el archivo .env" -ForegroundColor Red
    Write-Host "Copia .env.example y configúralo antes de continuar"
    exit 1
}

# 1️- Crear entorno virtual si no existe
if (-Not (Test-Path $VENV_PATH)) {
    Write-Host "Creando entorno virtual..."
    & $PYTHON_EXE -m venv $VENV_NAME
} else {
    Write-Host "Entorno virtual ya existe"
}

# 2️ - Activar entorno virtual
Write-Host "Activando entorno virtual..."
& $ACTIVATE_SCRIPT

# 3️ - Instalar dependencias
if (Test-Path $REQUIREMENTS) {
    Write-Host "Instalando dependencias desde requirements.txt..."
    python -m pip install --upgrade pip *> $null
    python -m pip install -r $REQUIREMENTS *> $null
} else {
    Write-Host "No se encontró requirements.txt"
}

# 4️ - Ejecutar aplicación
if (Test-Path $MAIN_APP) {
    Write-Host "Ejecutando aplicación..."
    uvicorn app.main:app --reload

} else {
    Write-Host "No se encontró app/main.py"
}

#Desactivar entorno
deactivate
