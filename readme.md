# 📋 Agenda - Gestor de Tareas

**Agenda** es una aplicación web desarrollada con Django que permite a los usuarios organizar y administrar sus tareas de forma sencilla. La aplicación cuenta con autenticación de usuarios y un sistema CRUD para crear, consultar, editar y eliminar tareas, además de permitir establecer prioridades, fechas límite y estados de completado.

## 🌐 Demo

[Visitar Agenda](https://mi-agenda-i1yz.onrender.com)

## 🛠️ Tecnologías

- **Backend:** Python.
- **Frontend:** HTML5 / CSS3 / Tailwind CSS.
- **Base de datos:** PostgreSQL.
- **Despliegue:** Render.

## ✨ Funcionalidades principales

### 👤 Autenticación de usuarios

- Registro de nuevos usuarios.
- Inicio y cierre de sesión.
- Validaciones de contraseña mediante `UserCreationForm`.
- Autenticación mediante el sistema integrado de Django.
- Acceso protegido a la gestión de tareas mediante `login_required`.
- Cada usuario puede consultar y administrar únicamente sus propias tareas.

### 📋 Gestión de tareas

- Crear nuevas tareas.
- Consultar las tareas del usuario autenticado.
- Editar tareas existentes.
- Eliminar tareas mediante una pantalla de confirmación.
- Definir una prioridad para cada tarea:
  - Baja.
  - Media.
  - Alta.
- Establecer una fecha límite opcional.
- Marcar tareas como completadas o pendientes.
- Registrar automáticamente la fecha de creación.
- Registrar automáticamente la última actualización.
- Mostrar un estado visual para diferenciar tareas completadas y pendientes.
- Mostrar un estado vacío cuando el usuario todavía no tiene tareas.

### 📝 Formularios

- Formularios construidos mediante `ModelForm`.
- Campos personalizados con widgets de Django.
- Inputs estilizados con Tailwind CSS.
- Validación y visualización de errores por campo.
- Campo de fecha con selección mediante calendario.
- Restricción de la fecha mínima desde el formulario.
- Formulario reutilizable para crear y editar tareas.

### 🗑️ Eliminación de tareas

Antes de eliminar una tarea se muestra una pantalla de confirmación.

La aplicación informa al usuario que la acción no puede deshacerse y permite cancelar la operación antes de realizar la eliminación.

### 🎨 Interfaz

- Diseño responsive.
- Interfaz clara y minimalista.
- Componentes construidos con Tailwind CSS.
- Tarjetas para representar las tareas.
- Estados visuales para tareas completadas y pendientes.
- Estados `hover` y `focus`.
- Formularios personalizados.
- Navegación adaptada al estado de autenticación del usuario.
- Diseño consistente entre las diferentes vistas.
- Manejo de estados vacíos cuando no existen tareas.

### 🔐 Seguridad y control de acceso

- Protección de vistas mediante `login_required`.
- Uso de `get_object_or_404` junto con el usuario autenticado para editar y eliminar tareas.
- Cada tarea está relacionada con un usuario mediante una relación `ForeignKey`.
- Protección CSRF en los formularios mediante `{% csrf_token %}`.
- Uso del sistema de autenticación integrado de Django.
- Validaciones de contraseña proporcionadas por Django.

## 📚 Lo que aprendí

Con este proyecto practiqué y reforcé conceptos como:

- Creación de modelos en Django.
- Relaciones entre modelos mediante `ForeignKey`.
- Uso del modelo `User` integrado de Django.
- Sistema de autenticación de Django.
- `UserCreationForm` y `AuthenticationForm`.
- Creación y personalización de `ModelForm`.
- Personalización de widgets.
- Operaciones CRUD.
- Protección de vistas mediante `login_required`.
- Filtrado de información según el usuario autenticado.
- Uso de `get_object_or_404`.
- Uso de `TextChoices` para definir opciones en los modelos.
- Uso de `auto_now_add` y `auto_now`.
- Manejo de formularios y errores de validación.
- Protección CSRF.
- Herencia de plantillas mediante `{% extends %}` y `{% block %}`.
- Manejo de archivos estáticos mediante `{% load static %}`.
- Diseño responsive con Tailwind CSS.
- Manejo de estados vacíos en las plantillas.
- Preparación de una aplicación Django para producción.
- Configuración de PostgreSQL mediante `dj-database-url`.
- Configuración de archivos estáticos con WhiteNoise.
- Despliegue de una aplicación Django en Render.
- Uso de Gunicorn como servidor de producción.

## 🚀 Despliegue

La aplicación está desplegada en **Render** y utiliza PostgreSQL como base de datos en producción.

Para el entorno de producción se configuraron:

- Variables de entorno para información sensible.
- `DATABASE_URL` para la conexión con PostgreSQL.
- Gunicorn para ejecutar la aplicación Django.
- WhiteNoise para servir archivos estáticos.
- `collectstatic` durante el proceso de construcción.
- Configuración de `ALLOWED_HOSTS` mediante el hostname proporcionado por Render.

## 🎯 Objetivo del proyecto

El proyecto fue creado como una práctica para llevar los conocimientos de Django más allá de ejemplos básicos, construyendo una aplicación completa con **autenticación, control de acceso, persistencia de datos, operaciones CRUD, formularios personalizados, diseño responsive y despliegue en producción**.

El objetivo principal fue practicar cómo estructurar una aplicación Django funcional y preparada para ser utilizada desde un entorno real.

## 👨‍💻 Autor

**Aldo Sandoval Zepeda**

Proyecto desarrollado como parte de mi aprendizaje y práctica en desarrollo web con Python y Django.
