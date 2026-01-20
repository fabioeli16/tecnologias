# ================================ ================================ ================================ ================================
# Script de arranque para Windows
# ================================ ================================ ================================ ================================

# ----------------------------------------------------------------
# 1- DEFINIR VARIABLES
# ----------------------------------------------------------------
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


# ----------------------------------------------------------------
# 2- VALIDA EXISTENCIA DE .ENV
# ----------------------------------------------------------------
if (-not (Test-Path $ENV_FILE)) {
    Write-Host "ERROR: No existe el archivo .env" -ForegroundColor Red
    Write-Host "Copia .env.example y configúralo antes de continuar"
    exit 1
}

# ----------------------------------------------------------------
# 3 - Crear entorno virtual si no existe
# ----------------------------------------------------------------
if (-Not (Test-Path $VENV_PATH)) {
    Write-Host "Creando entorno virtual..."
    & $PYTHON_EXE -m venv $VENV_NAME
} else {
    Write-Host "Entorno virtual ya existe"
}

# ----------------------------------------------------------------
# 4 - Activar entorno virtual
# ----------------------------------------------------------------
Write-Host $ACTIVATE_SCRIPT
Write-Host "Activando entorno virtual..."
& $ACTIVATE_SCRIPT


# ----------------------------------------------------------------
# 5 - Validar e instalar dependencias
# ----------------------------------------------------------------
if (Test-Path $REQUIREMENTS) {

    Write-Host "Verificando dependencias..."

    python -m pip install --upgrade pip *> $null

    $required  = Get-Content $REQUIREMENTS | Where-Object { $_.Trim() -ne "" }
    $installed = python -m pip freeze

    if (-not $required) {
        Write-Host "requirements.txt está vacío, no hay dependencias que instalar"
    }
    elseif (-not $installed) {
        Write-Host "No hay paquetes instalados, instalando dependencias..."
        python -m pip install -r $REQUIREMENTS
    }
    else {
        $missing = Compare-Object `
            ($required  | Sort-Object) `
            ($installed | Sort-Object) `
            | Where-Object { $_.SideIndicator -eq "<=" }

        if ($missing) {
            Write-Host "Instalando librerías faltantes..."
            python -m pip install -r $REQUIREMENTS
        }
        else {
            Write-Host "Dependencias ya instaladas ✔"
        }
    }

} else {
    Write-Host "No se encontró requirements.txt" -ForegroundColor Yellow
}


# ----------------------------------------------------------------
# 6 - Ejecutar aplicación
# ----------------------------------------------------------------
if (Test-Path $MAIN_APP) {
    Write-Host "Ejecutando aplicación..."
    python -m app.main
} else {
    Write-Host "No se encontró app/main.py"
}


# ----------------------------------------------------------------
# 7 - Desactivar entorno virtual
# ----------------------------------------------------------------
deactivate