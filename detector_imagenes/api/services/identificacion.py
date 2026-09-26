from Cloudflare import identificar_imagen, obtener_informacion
from prompt import prompt_analisis, prompt_animal, prompt_planta, prompt_mineral, prompt_receta

def analizar_imagen_completa(imagen=None, tipo=None, nombre=None):
    identificacion = None

    if imagen:
        identificacion = identificar_imagen(imagen, prompt_analisis)
        tipo = identificacion.get("tipo")

    if tipo == "animal":
        informacion = analizar_animal(identificacion, nombre, 100)

    elif tipo == "planta":
        informacion = analizar_planta(identificacion, nombre, 100)

    elif tipo == "mineral":
        informacion = analizar_mineral(identificacion, nombre, 100)
    
    elif tipo == "receta":
        informacion = analizar_receta(identificacion, nombre, 100)

    else:
        informacion = {}

    return {**identificacion, "informacion": informacion}


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
