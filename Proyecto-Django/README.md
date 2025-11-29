## Tarea Final: Proyecto Web con Django

## Descripción y Objetivo
Este proyecto es la Tarea Final de desarrollo web, cuyo objetivo es demostrar la comprensión y aplicación completa del framework Django bajo el patrón Model-View-Template (MVT).

El proyecto implementa una aplicación base con:

Configuración de entorno virtual.

Estructura de proyecto y aplicación modular.

Dos vistas funcionales (/ y /acerca/).

Templates (.html) con inyección de datos dinámicos.

Uso de Tailwind CSS para un estilo limpio y responsivo.

## Estructura del Proyecto
El repositorio contiene la configuración estándar de un proyecto Django con una aplicación única:

mi_proyecto/: Carpeta de configuración principal, incluyendo el archivo urls.py maestro.

principal/: La aplicación Django implementada, que contiene la lógica de negocio.

views.py: Funciones que manejan las peticiones.

urls.py: Rutas específicas de la aplicación.

templates/: Almacena inicio.html y acerca.html.

manage.py: Utilidad de línea de comandos de Django.

## Vistas Implementadas y Funcionalidades
El proyecto expone dos rutas principales, demostrando la correcta conexión entre URL, View y Template.

## 1. Página de Inicio
Ruta (URL): / (Raíz del sitio)

Función (View): views.inicio

Template: principal/templates/inicio.html

Propósito: Muestra el mensaje de bienvenida y el título dinámico. Incluye un enlace de navegación a la vista "Acerca de".

## 2. Página "Acerca de" (Implementación Opcional)
Ruta (URL): /acerca/

Función (View): views.acerca

Template: principal/templates/acerca.html

Propósito: Muestra el nombre completo del autor (Gerson Enrique Rivera Ramos) y la descripción del proyecto, cumpliendo con el requisito opcional. Incluye un enlace para volver al inicio.

Ambos templates (inicio.html y acerca.html) están estilizados usando Tailwind CSS para una presentación moderna y profesional.

## Guía de Instalación y Ejecución
Sigue estos pasos para poner en marcha el proyecto en tu entorno local.

Prerrequisitos
Python 3.x

Git
## 1. Clonar el Repositorio

# Reemplaza la URL con la de tu repositorio si es diferente.
git clone https://github.com/gersonrv/Proyecto-Django.git

# Entra a la carpeta raíz de tu proyecto
cd PythonProject

## 2. Crear y Activar el Entorno Virtual

Se recomienda enfáticamente el uso de un entorno virtual para aislar las dependencias.

En Linux o Mac:

Bash

python3 -m venv .venv
source .venv/bin/activate

En Windows (PowerShell/CMD):

Bash

python -m venv .venv
.venv\Scripts\activate

## 3. Instalar Dependencias

Instala el framework Django:

pip install django

## 4. Ejecutar el Servidor de Desarrollo

Una vez instalado, inicia el servidor local de Django:

python manage.py runserver

## 5. Acceso

Abre tu navegador y navega a: http://127.0.0.1:8000


![Django1](https://github.com/user-attachments/assets/a521e0e7-482a-423f-b58c-34e14c076529)





![Django2](https://github.com/user-attachments/assets/eab7af5e-8241-4f9b-aa74-720a2a1f8693)



## Autor
## Nombre: Gerson Enrique Rivera Ramos

## Proyecto: Tarea Final - Desarrollo Web con Django

## Propósito: Desarrollar una aplicación web con Django que integre vistas, rutas y templates con estilos usando Tailwind CSS, demostrando el manejo básico del desarrollo web en Python.
