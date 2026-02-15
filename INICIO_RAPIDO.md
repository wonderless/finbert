# 🚀 GUÍA DE INICIO RÁPIDO

## ¿Qué elegir? Comparación de Plataformas

| Plataforma | Gratuito | Fácil | Velocidad | Límites |
|------------|----------|-------|-----------|---------|
| **Local** | ✅ | ✅✅✅ | ⚡⚡⚡ | Ninguno |
| **PythonAnywhere** | ✅ | ✅✅ | ⚡ | 1 app, CPU limitado |
| **Render** | ✅ | ✅✅ | ⚡⚡ | 750h/mes gratis |
| **Railway** | ✅* | ✅✅✅ | ⚡⚡ | $5 crédito/mes |
| **Heroku** | ❌ | ✅✅ | ⚡⚡ | Ya no tiene plan gratis |

*Railway ofrece $5/mes de crédito gratis

---

## OPCIÓN RECOMENDADA #1: Probar LOCALMENTE (5 minutos)

La forma más rápida de probar la aplicación:

```bash
# 1. Instalar dependencias (solo la primera vez)
pip install -r requirements.txt

# 2. Ejecutar el servidor
python app.py

# 3. Abrir index.html en tu navegador
# (arrastra el archivo a Chrome/Firefox)
```

**Primera ejecución:** Tomará ~5-10 minutos descargando el modelo FinBERT (440 MB).
**Siguientes ejecuciones:** Iniciará en segundos.

---

## OPCIÓN RECOMENDADA #2: Desplegar GRATIS en Render (20 minutos)

La mejor opción para producción gratuita:

### Paso 1: Crear cuenta en GitHub (si no tienes)
1. Ve a github.com
2. Crea una cuenta gratuita

### Paso 2: Subir el código a GitHub
```bash
# En la carpeta del proyecto
git init
git add .
git commit -m "Initial commit"

# Crea un repositorio en GitHub y luego:
git remote add origin https://github.com/TUUSUARIO/TUNOMBRE-REPO.git
git push -u origin main
```

### Paso 3: Desplegar en Render
1. Ve a render.com y crea cuenta (usa tu cuenta de GitHub)
2. Click en "New +" → "Web Service"
3. Conecta tu repositorio de GitHub
4. Render detectará automáticamente Flask
5. Click en "Create Web Service"
6. ¡Espera 10-15 minutos mientras se construye!

### Paso 4: Actualizar el Frontend
Una vez que Render te dé tu URL (ej: `https://tu-app.onrender.com`):

1. Abre `index.html`
2. Busca la línea `const API_URL = 'http://localhost:5000/analyze';`
3. Cámbiala a: `const API_URL = 'https://tu-app.onrender.com/analyze';`
4. Sube el index.html actualizado a GitHub Pages o ábrelo localmente

### Paso 5: (Opcional) Desplegar el Frontend en GitHub Pages
```bash
# Crear rama gh-pages
git checkout -b gh-pages
git add index.html
git commit -m "Deploy frontend"
git push origin gh-pages
```

Tu frontend estará en: `https://TUUSUARIO.github.io/TUNOMBRE-REPO/`

---

## OPCIÓN RECOMENDADA #3: PythonAnywhere (15 minutos)

Si no quieres usar GitHub:

1. **Crear cuenta:** pythonanywhere.com (plan Beginner - gratis)

2. **Subir archivos:**
   - Files → Upload → Subir `app.py` y `requirements.txt`

3. **Instalar dependencias:**
   - Consoles → Bash
   - `pip install --user -r requirements.txt` (toma ~10 minutos)

4. **Crear Web App:**
   - Web → Add new web app → Flask → Python 3.10
   - WSGI file: apunta a tu `app.py`

5. **Actualizar index.html:**
   - Cambiar `API_URL` a `https://TUUSUARIO.pythonanywhere.com/analyze`
   - Subir a `/home/TUUSUARIO/mysite/`

Tu app estará en: `https://TUUSUARIO.pythonanywhere.com`

---

## 🆘 Problemas Comunes

### "No module named 'flask'"
```bash
pip install -r requirements.txt
```

### "Address already in use"
Otro programa usa el puerto 5000:
```bash
# En app.py, cambia el puerto:
app.run(host='0.0.0.0', port=5001)

# En index.html, actualiza:
const API_URL = 'http://localhost:5001/analyze';
```

### "CORS error" en el navegador
Asegúrate de que:
1. El servidor esté corriendo (`python app.py`)
2. La URL en `index.html` sea correcta
3. Tengas instalado `flask-cors`

### El servidor es muy lento
- Primera petición siempre es lenta (carga el modelo en RAM)
- Considera usar un servidor con más memoria RAM
- FinBERT requiere ~2GB de RAM

### "Translation failed"
La librería `googletrans` a veces falla:
```bash
# Reinstalar:
pip uninstall googletrans
pip install googletrans==4.0.0rc1
```

---

## 📱 ¿Necesitas Ayuda?

Lee el README.md completo para instrucciones detalladas de cada plataforma.

---

## ✅ Checklist de Despliegue

- [ ] Instalé Python 3.8+
- [ ] Instalé las dependencias (`pip install -r requirements.txt`)
- [ ] Ejecuté el servidor (`python app.py`)
- [ ] El servidor inició sin errores
- [ ] Abrí `index.html` en el navegador
- [ ] Actualicé la URL del API en `index.html`
- [ ] Probé analizar un texto
- [ ] Funcionó correctamente

Si completaste todos los pasos, ¡felicidades! 🎉

---

**Siguiente paso:** Lee el README.md para opciones de despliegue en producción.
