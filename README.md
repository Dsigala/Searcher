# 🔍 Searcher - Auto-Setup v2.1

**Herramienta avanzada de búsqueda con dorks para múltiples motores de búsqueda**

## 🚀 Características

- ✅ **Auto-Setup completo**: Crea entorno virtual e instala dependencias automáticamente
- 🔍 **Múltiples motores de búsqueda**: DuckDuckGo, Bing, Google, Brave, Yandex
- 📁 **Modo masivo**: Procesa miles de dorks desde archivos
- 🎨 **Interfaz colorida**: Salida organizada y fácil de leer
- 💾 **Guardado automático**: Exporta resultados a archivos .txt
- ⚡ **Caché inteligente**: Evita búsquedas duplicadas
- 🛡️ **Manejo de errores**: Recuperación automática de fallos

## 📦 Instalación Rápida

### Método 1: Auto-Setup (Recomendado)

# Clonar repositorio
git clone https://github.com/Dsigala/Searcher.git

cd Searcher

# Crear entorno virtual
python3 -m venv venv

# Activar entorno (Linux/Mac)
source venv/bin/activate

# Activar entorno (Windows)
venv\Scripts\activate

# Instalar dependencias
pip install -r requirements.txt

# Ejecutar
python searcher.py

📊 Rendimiento
Modo	Dorks/minuto	Memoria	Notas

-Simple	10-20	~50MB	Ideal para pruebas

-Masivo	100-500	~100MB	Usar batches

-ALL Engines	5-10	~150MB	Muy lento            


# examples/dorks.txt

site:example.com intitle:"admin"

inurl:admin/login.php

"admin panel" site:com

filetype:sql intext:"password"

filetype:pdf "confidential"

"index of" "/backup"

"login" "password" site:edu

inurl:login.aspx

"sign in" "forgot password"

intitle:"index of" "/wp-content"

"parent directory" "mp3"

inurl:/backup/ site:org

"database password" filetype:env

"api_key" "password" filetype:txt

"config" "password" site:github.com

intitle:"webcam 7" "anybody there?"

inurl:"/view/view.shtml"

"axis" "camera" "login"

filetype:doc "confidential"

filetype:xls "username" "password"

"private" filetype:pdf

inurl:/wp-admin/admin-ajax.php

"wordpress" "wp-content" "admin"

"wp-login.php" "action=lostpassword"





⚠️ Aviso Legal
Esta herramienta es para fines educativos y de prueba de seguridad autorizada únicamente. El autor no se hace responsable del uso indebido.

✨ Créditos
Autor: CR4CK3N
Mantenedor: Dsigala
Versión: 2.1 Auto-Setup


⭐ Si te gusta este proyecto, dale una estrella en GitHub!
