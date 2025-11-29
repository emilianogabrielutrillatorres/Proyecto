📝 Descripción del Proyecto

Este proyecto consiste en una aplicación web básica desarrollada con el framework Django, ideal para comprender el ciclo completo de creación de un sitio web. Incluye desde la preparación del entorno, la creación del proyecto y una aplicación interna, hasta la creación de vistas, rutas (URLs), templates y la ejecución del servidor local.
El sitio muestra una página de inicio simple que utiliza un template HTML estilizado con TailwindCSS para demostrar cómo Django renderiza contenido dinámico desde el backend hacia la interfaz.

⚙️ Pasos de Instalación y Ejecución
1. Crear y activar un entorno virtual

Linux / Mac:

python -m venv venv
source venv/bin/activate


Windows:

python -m venv venv
venv\Scripts\activate

2. Instalar Django
pip install django

3. Verificar la instalación
django-admin --version

4. Crear el proyecto principal
django-admin startproject mi_proyecto
cd mi_proyecto

5. Ejecutar el servidor inicial
python manage.py runserver


Abrir en el navegador:
👉 http://127.0.0.1:8000

6. Crear la aplicación "principal"
python manage.py startapp principal

7. Registrar la app en settings.py

Agregar en INSTALLED_APPS:

'principal',

8. Crear la vista

Archivo: principal/views.py

from django.shortcuts import render

def inicio(request):
    return render(request, 'inicio.html', {'titulo': 'Bienvenido a mi proyecto Django'})

9. Crear archivo de URLs de la app

Archivo: principal/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
]

10. Conectar las URLs en el proyecto principal

Archivo: mi_proyecto/urls.py

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('principal.urls')),
]

11. Crear el template

Ruta: principal/templates/inicio.html

<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <title>{{ titulo }}</title>
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css">
</head>
<body class="bg-gray-100 text-center p-8">
    <h1 class="text-3xl font-bold text-blue-600 mb-4">{{ titulo }}</h1>
    <p>Este es tu primer template en Django 🎉</p>
</body>
</html>

🎯 Propósito del Proyecto

El propósito de este proyecto es introducir al estudiante al flujo completo de desarrollo con Django, permitiéndole:

Crear un entorno de trabajo profesional con entorno virtual.

Comprender la estructura de un proyecto Django.

Crear aplicaciones internas (apps) dentro del proyecto.

Definir vistas, URLs y templates.

Renderizar HTML dinámico desde el backend.

Ejecutar y probar un servidor web de forma local.

Este proyecto sirve como base para proyectos más complejos, como gestores de datos, sistemas con bases de datos, paneles administrativos, blogs o APIs.
