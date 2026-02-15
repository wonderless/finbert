#!/bin/bash
# Script de instalación rápida para Linux/macOS

echo "🚀 Instalador de Analizador de Sentimiento"
echo "==========================================="
echo ""

# Verificar Python
if ! command -v python3 &> /dev/null
then
    echo "❌ Python 3 no está instalado"
    echo "Instala Python desde: https://www.python.org/downloads/"
    exit 1
fi

echo "✅ Python encontrado: $(python3 --version)"
echo ""

# Crear entorno virtual
echo "📦 Creando entorno virtual..."
python3 -m venv venv

# Activar entorno virtual
echo "🔧 Activando entorno virtual..."
source venv/bin/activate

# Instalar dependencias
echo "📥 Instalando dependencias (esto puede tomar varios minutos)..."
pip install -r requirements.txt

echo ""
echo "✅ ¡Instalación completada!"
echo ""
echo "Para ejecutar el servidor:"
echo "  1. Activa el entorno: source venv/bin/activate"
echo "  2. Ejecuta: python app.py"
echo "  3. Abre index.html en tu navegador"
echo ""
echo "🎉 ¡Listo para usar!"
