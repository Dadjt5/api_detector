# TFG_Polideportivo

Aplicación web desarrollada como portfolio de Woaida Interactive, dedicada a mostrar los diferentes juegos y aplicaciones Android desarrollados por el estudio.

El proyecto está compuesto por un frontend y un backend, que se comunican mediante una API para obtener y mostrar dinámicamente la información de los diferentes proyectos.

## Demo

**Aplicación en producción:** https://woaida.onrender.com

## Tecnologías

**Frontend-React**

* React
* JavaScript
* HTML / CSS

**Backend**

* Python
* Django
* Django REST Framework

**Base de datos**

* PostgreSQL
* Neon

**Deployment**

* Render

## Funcionalidades

* Mostrar las diferentes aplicaciones y juegos desarrolladas
* Comunicación entre frontend y backend mediante API REST
* Persistencia de datos mediante PostgreSQL
* Despliegue de la aplicación en producción

## Arquitectura

```text
┌──────────────────┐
│   React          │
│    Frontend      │
└────────┬─────────┘
         │
      REST API
         │
┌────────▼─────────┐
│ Django + DRF     │
│     Backend      │
└────────┬─────────┘
         │
┌────────▼─────────┐
│   PostgreSQL     │
│      Neon        │
└──────────────────┘
```

## Estructura del proyecto

```text
WoAiDa-Interactive/
├── frontend-react/
├── backend/
└── README.md
```

## Sobre el proyecto

Este proyecto fue desarrollado para dar un rápido y cómodo acceso a todas las aplicaciones desarrolladas, aplicando conocimientos de desarrollo web full-stack, diseño de APIs REST y despliegue de aplicaciones.

## Autor

Desarrollado por **David Juzgado Torell**.
