# 📦 ARCHIVOS DEL PROYECTO

## Archivos Principales (OBLIGATORIOS)

### 1. **index.html**
- **Descripción:** Interfaz web del usuario (frontend)
- **Uso:** Abre este archivo en tu navegador para usar la aplicación
- **Personalización:** Cambia `API_URL` con la URL de tu servidor backend

### 2. **app.py**
- **Descripción:** Servidor backend en Python con Flask
- **Uso:** Ejecuta con `python app.py` para iniciar el servidor
- **Puerto:** Por defecto usa el puerto 5000

### 3. **requirements.txt**
- **Descripción:** Lista de dependencias Python necesarias
- **Uso:** Instala con `pip install -r requirements.txt`
- **Contenido:** Flask, FinBERT, Google Translate, etc.

---

## Documentación

### 4. **README.md**
- **Descripción:** Documentación completa del proyecto
- **Contenido:**
  - Instrucciones detalladas de instalación
  - Múltiples opciones de despliegue
  - Solución de problemas
  - Personalización
  - API endpoints

### 5. **INICIO_RAPIDO.md** (este archivo)
- **Descripción:** Guía rápida para empezar en 5 minutos
- **Contenido:**
  - Comparación de plataformas
  - Pasos básicos de instalación
  - Problemas comunes
  - Checklist de despliegue

---

## Archivos de Despliegue (OPCIONALES)

### 6. **Procfile**
- **Descripción:** Configuración para Heroku, Railway
- **Uso:** Automático en estas plataformas
- **Contenido:** Comando para ejecutar con Gunicorn

### 7. **runtime.txt**
- **Descripción:** Especifica versión de Python
- **Uso:** Automático en Heroku, Railway, Render
- **Contenido:** `python-3.11.0`

### 8. **Dockerfile**
- **Descripción:** Configuración para Docker
- **Uso:** `docker build -t sentiment-analyzer .`
- **Para:** Despliegue en contenedores

### 9. **gitignore.txt**
- **Descripción:** Archivos a ignorar en Git
- **Uso:** Renombrar a `.gitignore` antes de hacer commit
- **Contenido:** venv/, cache, logs, etc.

---

## Scripts de Instalación (OPCIONALES)

### 10. **install.sh**
- **Descripción:** Instalador automático para Linux/macOS
- **Uso:** 
  ```bash
  chmod +x install.sh
  ./install.sh
  ```
- **Función:** Crea entorno virtual e instala dependencias

### 11. **install.bat**
- **Descripción:** Instalador automático para Windows
- **Uso:** Doble click en el archivo
- **Función:** Crea entorno virtual e instala dependencias

---

## 🚀 ¿Por dónde empiezo?

### Para probar LOCALMENTE (recomendado):
1. Instala Python 3.8+
2. Ejecuta `install.sh` (Linux/Mac) o `install.bat` (Windows)
   O manualmente: `pip install -r requirements.txt`
3. Ejecuta: `python app.py`
4. Abre `index.html` en tu navegador

### Para DESPLEGAR en internet:
1. Lee **README.md** para ver todas las opciones
2. Lee **INICIO_RAPIDO.md** para comenzar rápidamente
3. Recomendado: Render.com (gratis y fácil)

---

## 🎯 Archivos Mínimos Necesarios

Para que la aplicación funcione, solo necesitas:
- ✅ `index.html`
- ✅ `app.py`
- ✅ `requirements.txt`

Los demás archivos son opcionales y facilitan el despliegue.

---

## 📋 Estructura Recomendada de Carpetas

```
mi-proyecto-sentimiento/
│
├── index.html              ← Frontend
├── app.py                  ← Backend
├── requirements.txt        ← Dependencias
│
├── README.md              ← Documentación completa
├── INICIO_RAPIDO.md       ← Guía rápida
│
├── .gitignore             ← Para Git
├── Procfile               ← Para Render/Railway/Heroku
├── runtime.txt            ← Para especificar Python version
├── Dockerfile             ← Para Docker
│
└── scripts/               ← Scripts opcionales
    ├── install.sh
    └── install.bat
```

---

## 🔄 Flujo de Trabajo Típico

```
1. Descargar archivos
   ↓
2. Instalar dependencias (requirements.txt)
   ↓
3. Ejecutar servidor (app.py)
   ↓
4. Abrir interfaz (index.html)
   ↓
5. ¡Usar la aplicación!
```

---

## 💡 Consejos

- **Primera vez:** Usa el instalador automático (`install.sh` o `install.bat`)
- **Desarrollo:** Mantén el servidor corriendo con `python app.py`
- **Producción:** Sigue las instrucciones del README.md
- **Problemas:** Consulta la sección de solución de problemas en README.md

---

## 📞 ¿Necesitas ayuda?

1. Lee **INICIO_RAPIDO.md** para soluciones rápidas
2. Consulta **README.md** para información detallada
3. Revisa la sección "Solución de Problemas" en README.md

---

¡Éxito con tu proyecto! 🎉
