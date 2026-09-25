prompt_analisis = """
Tu tarea es analizar la imagen, identificar el elemento principal y generar una pequeña ficha con informacioón basada en una
identificación visual lo más fiable posible.

IMPORTANTE:
La identificación debe basarse principalmente en las características visibles de la imagen.
La información adicional de la ficha puede utilizar conocimiento general fiable sobre el
elemento identificado.

No inventes identificaciones ni datos. Cuando no exista suficiente información, utiliza
una identificación más general o deja el campo vacío.

========================
1. TIPO
========================

Determina qué aparece principalmente en la imagen.

El campo "tipo" SOLO puede contener uno de estos valores:

- animal
- planta
- mineral
- otro

Si el elemento no puede clasificarse claramente como animal, planta o mineral, utiliza "otro".

No utilices otros valores para "tipo".

========================
2. IDENTIFICACIÓN
========================

Intenta identificar el elemento hasta el nivel más específico que permita la evidencia.

No estás obligado a identificar una especie.

Utiliza el nivel de identificación que realmente puedas justificar:

- especie
- género
- familia
- grupo
- categoría general

Si no puedes determinar la especie con suficiente seguridad, NO inventes una especie
para completar el campo.

Ejemplo:

Si la imagen permite identificar claramente un zorro pero no permite determinar
la especie exacta, utiliza:

"name": "Zorro"

y no inventes una especie concreta.

========================
3. CONFIANZA
========================

"confidence" representa exclusivamente la confianza en la IDENTIFICACIÓN VISUAL.

Debe ser un número entero entre 0 y 100.

Orientación:

90-100:
Identificación muy clara. Existen características visuales distintivas suficientes.

70-89:
Identificación bastante probable, aunque existen algunas alternativas.

40-69:
Identificación posible, pero existen dudas importantes.

1-39:
La identificación es muy incierta.

0:
No existe información suficiente para realizar una identificación útil.

Reduce la confianza cuando:
- la imagen está borrosa
- el elemento aparece parcialmente
- hay poca iluminación
- el elemento es demasiado pequeño
- faltan características distintivas
- existen varias especies visualmente similares
- la imagen no permite distinguir entre categorías cercanas

IMPORTANTE:
Una confianza alta NO significa que la especie sea visualmente parecida.
Debe existir evidencia visual suficiente para justificarla.

========================
4. REGLAS DE CONSISTENCIA
========================

- "tipo" debe ser exactamente: animal, planta, mineral u otro.
- "name" deben referirse al mismo elemento.
- No inventes especies.
- Si no puedes determinar un dato de forma fiable, utiliza "".
- "confidence" debe ser siempre un número entero entre 0 y 100.
- Mantén exactamente las etiquetas JSON indicadas a continuación.

========================
8. FORMATO DE RESPUESTA
========================

Devuelve ÚNICAMENTE JSON válido.

No utilices bloques Markdown.
No añadas explicaciones antes o después del JSON.
No añadas comentarios.
No añadas propiedades adicionales.
No cambies los nombres de las propiedades.

Formato obligatorio:

{
  "tipo": "animal",
  "name": "Nombre común",
  "confidence": 0
}
"""