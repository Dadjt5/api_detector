
from .Cloudflare import identificar_imagen, obtener_informacion

from ..prompt.prompt_analisis import prompt_analisis

from ..prompt.prompt_animal import prompt_animal
from ..prompt.prompt_planta import prompt_planta
from ..prompt.prompt_mineral import prompt_mineral

from ..prompt.prompt_receta import prompt_receta

from ..prompt.prompt_edificio_rascacielos import prompt_edificio_rascacielos
from ..prompt.prompt_edificio_religioso import prompt_edificio_religioso
from ..prompt.prompt_edificio_otro import prompt_edificio_otro

from ..prompt.prompt_simbolo_historico import prompt_simbolo_historico
from ..prompt.prompt_escultura_historica import prompt_escultura_historica

from ..prompt.prompt_cuadro import prompt_cuadro
from ..prompt.prompt_escultura import prompt_escultura

from ..prompt.prompt_objeto import prompt_objeto


# Relación entre categorías y prompts
PROMPTS = {
    "animales": prompt_animal,
    "plantas": prompt_planta,
    "minerales": prompt_mineral,

    "recetas": prompt_receta,

    "edificio_rascacielos": prompt_edificio_rascacielos,
    "edificio_religioso": prompt_edificio_religioso,
    "edificio_otro": prompt_edificio_otro,

    "simbolo_historico": prompt_simbolo_historico,
    "escultura_historica": prompt_escultura_historica,
    
    "cuadro": prompt_cuadro,
    "escultura": prompt_escultura,
    
    "objeto": prompt_objeto
}


def analizar_imagen_completa(imagen=None, tipo=None, nombre=None):
    identificacion = None

    if imagen:
        identificacion = identificar_imagen(imagen, prompt_analisis)
        if not identificacion:
            return {}

        tipo = identificacion.get("tipo")

    if not tipo:
        return {}

    prompt_seleccionado = PROMPTS.get(tipo)
    if not prompt_seleccionado:
        return {}

    if identificacion:
        nombre = identificacion.get("name", "")
        confianza = identificacion.get("confidence", 0)
    else:
        confianza = 100

    prompt = prompt_seleccionado.format(
        nombre=nombre or "",
        confianza=confianza
    )

    informacion = obtener_informacion(prompt)

    return informacion
