prompt_receta = """
La primera fase del sistema ha identificado el siguiente elemento:

Nombre: {nombre}
Confianza de identificación: {confianza}/100

Tu tarea es generar una receta basada en el elemento identificado.

No vuelvas a realizar una identificación visual.
Utiliza el nombre proporcionado como referencia para determinar la receta.

La receta debe ser realista, coherente y adecuada para el elemento identificado.
No inventes ingredientes extraños ni cantidades poco razonables.

Debes proporcionar todos los ingredientes necesarios y los pasos necesarios
para elaborar la receta.

La cantidad de ingredientes debe estar calculada para el número de personas
indicado en "numero_personas".

Devuelve ÚNICAMENTE un objeto JSON válido.

No utilices Markdown.
No añadas explicaciones antes o después del JSON.
No añadas propiedades adicionales.
No cambies los nombres de las propiedades.

Formato obligatorio:

{
    "name": "Nombre de la receta",
    "numero_personas": 0,
    "ingredientes": [
        {
            "nombre": "Nombre del ingrediente",
            "cantidad": "Cantidad necesaria"
        }
    ],
    "pasos": [
        "Primer paso de la receta",
        "Segundo paso de la receta"
    ]
}

INDICACIONES:

- "name" debe contener el nombre de la receta.
- "numero_personas" debe indicar para cuántas personas están pensadas
  las cantidades de los ingredientes.
- "ingredientes" debe ser siempre una lista.
- Cada ingrediente debe contener "nombre" y "cantidad".
- La cantidad debe incluir la unidad correspondiente cuando sea posible
  (g, kg, ml, l, unidades, cucharadas, cucharaditas, etc.).
- "pasos" debe ser siempre una lista ordenada.
- Los pasos deben contener todas las acciones necesarias para preparar
  la receta, sin omitir pasos importantes.
- Ordena los pasos siguiendo el orden normal de preparación.
- Si una cantidad exacta no puede determinarse de forma fiable,
  utiliza una cantidad razonable y coherente con la receta.
- Si un dato no puede determinarse de forma fiable, deja el campo vacío,
  pero mantenlo dentro del JSON.

"numero_personas" debe ser siempre un número entero.

No añadas propiedades adicionales.
"""
