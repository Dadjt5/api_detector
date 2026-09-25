prompt_animal = """
La primera fase de análisis visual ha identificado el siguiente elemento:

Nombre: {nombre}
Confianza de identificación visual: {confianza}/100

Tu tarea es generar exclusivamente la información enciclopédica
específica para este animal.

No vuelvas a realizar una identificación visual.
Utiliza el nombre proporcionado como referencia.

Genera información factual y fiable.

========================
CATEGORÍA
========================
Ten en cuenta lo siguiente para la categoria:

Determina el grupo o categoría general al que pertenece el elemento.

Ejemplos:

Animales:
- Mamífero
- Ave
- Reptil
- Anfibio
- Pez
- Insecto
- Arácnido
- Molusco
- Crustáceo


Estas categorías son solo ejemplos. Puedes utilizar otra categoría cuando sea
más apropiada para el elemento identificado.


Si no existe suficiente información para determinar una categoría concreta,
utiliza una categoría más general.



Devuelve ÚNICAMENTE un objeto JSON válido:

{
    "name": "Nombre común",
    "scientific_name": "Nombre científico",
    "descripcion": "Breve descripción factual",
    "category": "Categoría",
    "habitat": "Hábitat",
    "venenoso": "si o no",
    "alimentacion": "",
    "tamano": "",
    "peso": "",
    "esperanza_vida": "",
    "comportamiento": "",
    "reproduccion": "",
    "estado_conservacion": "",
    "dato_interesante": ""
}

Si un dato no puede determinarse de forma fiable,
deja el campo vacío pero incluyelo en el JSON a pesar de estar vacio.

No añadas propiedades adicionales.
"""
