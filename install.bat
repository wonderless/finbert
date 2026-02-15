@echo off
REM Script de instalación rápida para Windows

echo ========================================
echo Instalador de Analizador de Sentimiento
echo ========================================
echo.

REM Verificar Python
python --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Python no esta instalado
    echo Descarga Python desde: https://www.python.org/downloads/
    pause
    exit /b 1
)

echo Python encontrado
python --version
echo.

REM Crear entorno virtual
echo Creando entorno virtual...
python -m venv venv

REM Activar entorno virtual
echo Activando entorno virtual...
call venv\Scripts\activate.bat

REM Instalar dependencias
echo Instalando dependencias (esto puede tomar varios minutos)...
pip install -r requirements.txt

echo.
echo ========================================
echo Instalacion completada!
echo ========================================
echo.
echo Para ejecutar el servidor:
echo   1. Activa el entorno: venv\Scripts\activate
echo   2. Ejecuta: python app.py
echo   3. Abre index.html en tu navegador
echo.
echo Listo para usar!
echo.
pause
