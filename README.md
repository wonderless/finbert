# 📰 Analizador de Sentimiento de Noticias

Aplicación web que analiza el sentimiento (positivo/negativo/neutral) de noticias en español usando FinBERT y Google Translate.

## 🚀 Características

- ✨ Interfaz moderna y profesional
- 🔄 Traducción automática español → inglés
- 🤖 Análisis con FinBERT (modelo especializado en noticias financieras)
- 📊 Visualización de confianza y scores detallados
- 🎨 Diseño responsivo y animaciones fluidas

## 📁 Estructura del Proyecto

```
analizador-sentimiento/
│
├── index.html          # Frontend (interfaz web)
├── app.py             # Backend (servidor Flask)
├── requirements.txt   # Dependencias Python
└── README.md         # Este archivo
```

---

## 🛠️ OPCIÓN 1: Instalación Local (Desarrollo)

### Requisitos Previos
- Python 3.8 o superior
- pip (gestor de paquetes de Python)

### Paso 1: Crear Entorno Virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Paso 2: Instalar Dependencias

```bash
pip install -r requirements.txt
```

**Nota:** La primera vez puede tardar varios minutos en descargar el modelo FinBERT (~440 MB).

### Paso 3: Ejecutar el Servidor

```bash
python app.py
```

El servidor estará disponible en: `http://localhost:5000`

### Paso 4: Abrir el Frontend

1. Abre `index.html` con tu navegador web
2. O usa un servidor local:

```bash
# Con Python
python -m http.server 8000

# Con Node.js (si lo tienes)
npx serve .
```

Accede a: `http://localhost:8000`

---

## ☁️ OPCIÓN 2: Despliegue en PythonAnywhere (GRATIS)

PythonAnywhere ofrece hosting gratuito para aplicaciones Python.

### Paso 1: Crear Cuenta
1. Ve a [www.pythonanywhere.com](https://www.pythonanywhere.com)
2. Crea una cuenta gratuita (Beginner)

### Paso 2: Subir Archivos
1. En el dashboard, ve a **Files**
2. Crea una carpeta: `sentiment-analyzer`
3. Sube `app.py` y `requirements.txt`

### Paso 3: Crear Web App
1. Ve a **Web** → **Add a new web app**
2. Selecciona: **Flask**
3. Python version: **3.10**
4. Path: `/home/tuusuario/sentiment-analyzer/app.py`

### Paso 4: Instalar Dependencias
1. Ve a **Consoles** → **Bash**
2. Ejecuta:

```bash
cd sentiment-analyzer
pip install --user -r requirements.txt
```

### Paso 5: Configurar WSGI
1. En **Web**, edita el archivo WSGI
2. Reemplaza el contenido con:

```python
import sys
path = '/home/tuusuario/sentiment-analyzer'
if path not in sys.path:
    sys.path.append(path)

from app import app as application
```

### Paso 6: Configurar el Frontend
1. Edita `index.html`
2. Cambia la línea del `API_URL`:

```javascript
const API_URL = 'https://tuusuario.pythonanywhere.com/analyze';
```

3. Sube `index.html` a la carpeta `/home/tuusuario/mysite/`

Tu aplicación estará en: `https://tuusuario.pythonanywhere.com`

---

## 🌐 OPCIÓN 3: Despliegue en Render (GRATIS)

Render ofrece hosting gratuito con despliegue automático desde GitHub.

### Paso 1: Preparar el Proyecto

Crea un archivo `render.yaml`:

```yaml
services:
  - type: web
    name: sentiment-analyzer
    runtime: python
    buildCommand: pip install -r requirements.txt
    startCommand: gunicorn app:app
    envVars:
      - key: PYTHON_VERSION
        value: 3.11.0
```

Actualiza `requirements.txt` agregando:
```
gunicorn==21.2.0
```

### Paso 2: Subir a GitHub
1. Crea un repositorio en GitHub
2. Sube todos los archivos:

```bash
git init
git add .
git commit -m "Initial commit"
git branch -M main
git remote add origin https://github.com/tuusuario/tu-repo.git
git push -u origin main
```

### Paso 3: Conectar con Render
1. Ve a [render.com](https://render.com)
2. Crea una cuenta (puedes usar GitHub)
3. Click en **New** → **Web Service**
4. Conecta tu repositorio de GitHub
5. Render detectará automáticamente tu aplicación
6. Click en **Create Web Service**

### Paso 4: Configurar Frontend
Edita `index.html` y actualiza:

```javascript
const API_URL = 'https://tu-app.onrender.com/analyze';
```

El despliegue es automático en cada `git push`.

---

## 🚢 OPCIÓN 4: Despliegue en Railway (GRATIS)

Railway ofrece $5 de crédito mensual gratis.

### Paso 1: Preparar el Proyecto

Crea un archivo `Procfile`:
```
web: gunicorn app:app
```

Crea `runtime.txt`:
```
python-3.11.0
```

### Paso 2: Desplegar
1. Ve a [railway.app](https://railway.app)
2. Conecta con GitHub
3. Selecciona tu repositorio
4. Railway desplegará automáticamente

Tu URL será: `https://tu-app.up.railway.app`

---

## 🐳 OPCIÓN 5: Docker (Cualquier Plataforma)

Si prefieres usar Docker:

```dockerfile
# Dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python", "app.py"]
```

```bash
# Construir y ejecutar
docker build -t sentiment-analyzer .
docker run -p 5000:5000 sentiment-analyzer
```

---

## 📝 Configuración del Frontend

**IMPORTANTE:** Después de desplegar el backend, actualiza la URL en `index.html`:

```javascript
// Desarrollo local
const API_URL = 'http://localhost:5000/analyze';

// Producción (reemplaza con tu URL)
const API_URL = 'https://tu-dominio.com/analyze';
```

---

## 🔧 Solución de Problemas

### Error: "CORS policy"
- Verifica que `flask-cors` esté instalado
- Asegúrate de que el servidor permita tu dominio

### Error: "Model not found"
- La primera ejecución descarga el modelo (~440 MB)
- Puede tardar 5-10 minutos según tu conexión
- Verifica que tengas espacio en disco suficiente

### Error: "Translation failed"
- `googletrans` usa la API web de Google (sin costo)
- Si falla mucho, considera usar Google Cloud Translation API

### Servidor lento
- FinBERT requiere procesamiento pesado
- Considera usar un servidor con más RAM
- La primera petición es más lenta (carga el modelo)

---

## 🎨 Personalización

### Cambiar Colores
Edita las variables CSS en `index.html`:

```css
:root {
    --color-bg: #0a0e17;
    --color-accent: #4a9eff;
    /* ... más colores ... */
}
```

### Cambiar Modelo
Puedes usar otros modelos de Hugging Face:

```python
# En app.py
model_name = "ProsusAI/finbert"  # Actual
# model_name = "nlptown/bert-base-multilingual-uncased-sentiment"
# model_name = "cardiffnlp/twitter-roberta-base-sentiment"
```

---

## 📊 API Endpoints

### POST /analyze
Analiza el sentimiento de un texto.

**Request:**
```json
{
  "text": "La economía creció significativamente"
}
```

**Response:**
```json
{
  "label": "positive",
  "confidence": 0.89,
  "scores": {
    "positive": 0.89,
    "negative": 0.08,
    "neutral": 0.03
  },
  "original_text": "La economía creció...",
  "translated_text": "The economy grew..."
}
```

### GET /health
Verifica el estado del servidor.

---

## 🔐 Consideraciones de Producción

1. **Rate Limiting:** Implementa límites de peticiones
2. **Cache:** Cachea traducciones frecuentes
3. **Logging:** Usa un servicio de logging profesional
4. **Monitoreo:** Implementa alertas de errores
5. **HTTPS:** Usa certificados SSL en producción
6. **Variables de Entorno:** Nunca subas API keys al código

---

## 📚 Tecnologías Utilizadas

- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Backend:** Python 3, Flask
- **ML Model:** FinBERT (ProsusAI)
- **Translation:** Google Translate (googletrans)
- **Deep Learning:** PyTorch, Transformers

---

## 📄 Licencia

Este proyecto es de código abierto. Siéntete libre de usarlo y modificarlo.

---

## 🤝 Contribuciones

¡Las contribuciones son bienvenidas! Si encuentras algún bug o tienes sugerencias:

1. Abre un issue
2. Haz un fork del proyecto
3. Crea un pull request

---

## 📧 Contacto

Si tienes preguntas o necesitas ayuda, no dudes en contactar.

---

## ⭐ Próximas Características

- [ ] Análisis de múltiples textos en batch
- [ ] Exportación de resultados a PDF
- [ ] Gráficos de tendencia de sentimiento
- [ ] Soporte para más idiomas
- [ ] API key para mayor estabilidad en traducciones
- [ ] Historial de análisis

---

¡Disfruta analizando sentimientos! 🎉
