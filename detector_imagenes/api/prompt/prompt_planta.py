prompt_planta = """
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

Plantas:
- Árbol
- Arbusto
- Planta herbácea
- Helecho
- Musgo
- Planta acuática


Estas categorías son solo ejemplos. Puedes utilizar otra categoría cuando sea
más apropiada para el elemento identificado.


Si no existe suficiente información para determinar una categoría concreta,
utiliza una categoría más general.



Devuelve ÚNICAMENTE un objeto JSON válido:

{
  "name": "Nombre común",
  "scientific_name": "Nombre científico",
  "descripcion": "descripción breve de la planta",
  "category": "Categoría",
  "habitat": "",
  "venenoso": "si o no",
  "distribucion": "",
  "tamano": "",
  "floracion": "",
  "reproduccion": "",
  "usos": "",
  "estado_conservacion": "",
  "dato_interesante": ""
}

Indicaciones:

- "habitat": ambientes donde suele crecer.
- "distribucion": regiones o zonas donde se encuentra de forma natural.
- "tamano": tamaño habitual aproximado.
- "floracion": información sobre su floración, si corresponde.
- "reproduccion": forma principal de reproducción.
- "usos": usos conocidos, por ejemplo ornamentales, alimentarios, medicinales o industriales.
- "estado_conservacion": estado de conservación conocido. Si no existe información fiable, deja el campo vacío.
- "dato_interesante": un dato curioso o relevante sobre la planta.

Si un dato no puede determinarse de forma fiable,
deja el campo vacío pero incluyelo en el JSON a pesar de estar vacio.

No añadas propiedades adicionales.
"""
