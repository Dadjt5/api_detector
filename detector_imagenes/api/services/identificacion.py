from .Cloudflare import identificar_imagen, obtener_informacion
from ..prompt.prompt_analisis import prompt_analisis
from ..prompt.prompt_animal import prompt_animal
from ..prompt.prompt_planta import prompt_planta
from ..prompt.prompt_mineral import prompt_mineral
from ..prompt.prompt_receta import prompt_receta

def analizar_imagen_completa(imagen=None, tipo=None, nombre=None):
    identificacion = None

    if imagen:
        identificacion = identificar_imagen(imagen, prompt_analisis)
        tipo = identificacion.get("tipo")

    if tipo == "animales":
        informacion = analizar_animal(identificacion, nombre, 100)

    elif tipo == "plantas":
        informacion = analizar_planta(identificacion, nombre, 100)

    elif tipo == "minerales":
        informacion = analizar_mineral(identificacion, nombre, 100)
    
    elif tipo == "recetas":
        informacion = analizar_receta(identificacion, nombre, 100)

    else:
        informacion = {}

    return informacion


def analizar_animal(identificacion=None, nombre=None, confianza=None):
    if identificacion:
        nombre = identificacion.get("name", "")
        confianza = identificacion.get("confidence", 0)

    prompt = prompt_animal.format(nombre=nombre, confianza=confianza)
    informacion = obtener_informacion(prompt)

    return informacion

def analizar_planta(identificacion=None, nombre=None, confianza=None):
    if identificacion:
        nombre = identificacion.get("name", "")
        confianza = identificacion.get("confidence", 0)

    prompt = prompt_planta.format(nombre=nombre, confianza=confianza)
    informacion = obtener_informacion(prompt)

    return informacion

def analizar_mineral(identificacion=None, nombre=None, confianza=None):
    if identificacion:
        nombre = identificacion.get("name", "")
        confianza = identificacion.get("confidence", 0)

    prompt = prompt_mineral.format(nombre=nombre, confianza=confianza)
    informacion = obtener_informacion(prompt)

    return informacion

def analizar_receta(identificacion=None, nombre=None, confianza=None):
    if identificacion:
        nombre = identificacion.get("name", "")
        confianza = identificacion.get("confidence", 0)

    prompt = prompt_receta.format(nombre=nombre, confianza=confianza)
    informacion = obtener_informacion(prompt)

    return informacion
