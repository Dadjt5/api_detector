# API Enciclopedia

API REST desarrollada con **Django** como backend para una aplicación Android de reconocimiento y catalogación mediante fotografías.

El proyecto nace como backend para una aplicación inicialmente orientada al reconocimiento de animales. Sin embargo, la arquitectura está planteada con una visión más amplia, permitiendo incorporar en el futuro diferentes tipos de elementos y objetos.

Actualmente, la API se encuentra en fase de desarrollo y cuenta con la estructura inicial del backend y una base de datos PostgreSQL alojada en **Neon**.

## Estado del proyecto

**En desarrollo**

La API se encuentra actualmente en una fase inicial de desarrollo. La estructura del proyecto y la conexión con la base de datos están preparadas, mientras que las funcionalidades y endpoints se irán implementando progresivamente.

Ahora mismo solo esta pensada para el análisis de animales pero se busca que sea mas general.

## Tecnologías

**Backend**

* Python
* Django
* Django REST Framework

**Base de datos**

* PostgreSQL
* Neon

**Cliente**

* Android (Java)

## Arquitectura

```text
┌──────────────────────┐
│  Aplicación Android  │
│        Java          │
└──────────┬───────────┘
           │
        HTTP / JSON
           │
┌──────────▼───────────┐
│        Django        │
│      REST API        │
└──────────┬───────────┘
           │
┌──────────▼───────────┐
│      PostgreSQL      │
│        Neon          │
└──────────────────────┘
```

## Concepto

La API servirá como backend para una enciclopedia digital generada a partir de los elementos reconocidos por la aplicación Android.

La primera implementación estará centrada en **animales**, permitiendo almacenar y consultar la información obtenida durante el proceso de reconocimiento.

A largo plazo, el objetivo es evolucionar hacia un sistema de reconocimiento más general, capaz de trabajar con diferentes categorías de elementos y objetos.

## Evolución futura

El proyecto está planteado para crecer progresivamente mediante nuevas funcionalidades, entre ellas:

* Implementación de los primeros endpoints REST
* Gestión de animales identificados
* Consulta y organización de la enciclopedia
* Incorporación de nuevas categorías
* Reconocimiento de otros tipos de elementos y objetos
* Integración con nuevos modelos de inteligencia artificial

## Propósito

El objetivo de esta API es proporcionar una base backend escalable para la aplicación de reconocimiento visual y su enciclopedia.


El proyecto permite poner en práctica el desarrollo de **APIs REST con Django, comunicación entre un cliente Android y un servidor y comunicación con un agente de IA**, dejando preparada la infraestructura para futuras funcionalidades de reconocimiento y catalogación.

## Desarrollador

Desarrollado por **David Juzgado Torell**.

🔗 [LinkedIn](AÑADIR_URL) · 🔗 [Portfolio](AÑADIR_URL)
