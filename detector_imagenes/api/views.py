import base64
import json
import os
import re
import requests

from dotenv import load_dotenv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

load_dotenv()


class AnalizarImagenView(APIView):

    def post(self, request):
        imagen = request.FILES.get("imagen")

        if not imagen:
            return Response(
                {"error": "No se ha enviado ninguna imagen"},
                status=status.HTTP_400_BAD_REQUEST
            )

        try:
            image_bytes = imagen.read()
            image_b64 = base64.b64encode(image_bytes).decode('utf-8')

            account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID")
            auth_token = os.getenv("CLOUDFLARE_AUTH_TOKEN")

            if not account_id or not auth_token:
                return Response(
                    {"error": "Faltan las credenciales de Cloudflare"},
                    status=status.HTTP_500_INTERNAL_SERVER_ERROR
                )

            # URL de Workers AI
            url = (
                f"https://api.cloudflare.com/client/v4/accounts/"
                f"{account_id}/ai/run/"
                f"@cf/meta/llama-4-scout-17b-16e-instruct"
            )

            # Prompt para el modelo
            prompt = """
prompt = """
Tu tarea es analizar la imagen, identificar el elemento principal y generar una ficha
de enciclopedia basada en una identificación visual lo más fiable posible.

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
2. CATEGORÍA
========================

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

Plantas:
- Árbol
- Arbusto
- Planta herbácea
- Helecho
- Musgo
- Planta acuática

Minerales:
- Silicato
- Sulfuro
- Óxido
- Carbonato
- Haluro
- Elemento nativo

Estas categorías son solo ejemplos. Puedes utilizar otra categoría cuando sea
más apropiada para el elemento identificado.

La categoría debe ser coherente con el "tipo".

Si no existe suficiente información para determinar una categoría concreta,
utiliza una categoría más general.

========================
3. IDENTIFICACIÓN
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

El campo "scientific_name" debe corresponder exactamente al nivel de identificación.

Si identificas una especie, utiliza el nombre científico de esa especie.

Si identificas únicamente un género, utiliza el nombre científico del género.

Si no puedes proporcionar un nombre científico fiable, deja "scientific_name" vacío.

El nombre común y el nombre científico deben referirse al mismo organismo o elemento.

========================
4. INFORMACIÓN
========================

Genera información breve, factual y útil para una enciclopedia.

La información adicional NO tiene que aparecer visualmente en la imagen.
Una vez realizada una identificación suficientemente fiable, puedes utilizar conocimiento
general sobre el elemento identificado.

No inventes datos.

Si un dato no puede determinarse de forma fiable a partir de la identificación,
deja ese campo vacío.

ANIMALES:

"habitat":
Indica el hábitat habitual del animal identificado.

"venenoso":
Utiliza únicamente:
- "si"
- "no"
- ""

Utiliza "si" únicamente cuando el animal sea conocido por producir veneno o toxinas.
No confundas "venenoso" con "peligroso", "agresivo" o "mordedor".

PLANTAS:

"habitat":
Indica el hábitat habitual de la planta identificada.

"venenoso":
Utiliza únicamente:
- "si"
- "no"
- ""

Utiliza "si" cuando la planta sea conocida por presentar toxicidad relevante.
No confundas toxicidad con que la planta sea simplemente no comestible.

MINERALES:

"habitat":
Indica donde se suele encontrar el mineral identificado.

"venenoso":
Déjalo vacío.

"dureza":
Indica la dureza aproximada en la escala de Mohs del mineral identificado.

Si no puedes determinarla de forma fiable, deja el campo vacío.

OTROS:

Si "tipo" es "otro", proporciona únicamente información que sea relevante y fiable
para el elemento identificado.

========================
5. DESCRIPCIÓN
========================

"descripcion" debe ser una descripción breve, factual y útil para una enciclopedia.

Debe describir qué es el elemento y sus características principales.

No menciones la imagen, la cámara, la fotografía ni el proceso de identificación.

No incluyas información especulativa.

========================
6. CONFIANZA
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
7. REGLAS DE CONSISTENCIA
========================

- "tipo" debe ser exactamente: animal, planta, mineral u otro.
- "category" debe ser coherente con "tipo".
- "name" y "scientific_name" deben referirse al mismo elemento.
- No inventes especies.
- No inventes nombres científicos.
- No inventes características.
- Si no puedes determinar un dato de forma fiable, utiliza "".
- "confidence" debe ser siempre un número entero entre 0 y 100.
- "venenoso" solo puede ser "si", "no" o "".
- "dureza" solo debe utilizarse para minerales.
- "habitat" debe quedar vacío para minerales.
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
  "scientific_name": "Nombre científico",
  "descripcion": "Breve descripción factual",
  "category": "Categoría",
  "habitat": "Hábitat",
  "venenoso": "si",
  "dureza": "",
  "confidence": 0
}
"""

            payload = {
                "messages": [
                    {
                        "role": "user",
                        "content": [
                            {
                                "type": "text", 
                                "text": prompt
                            },
                            {
                                "type": "image_url", 
                                "image_url": {
                                    "url": f"data:image/jpeg;base64,{image_b64}"
                                }
                            }
                        ]
                    }
                ]
            }

            # Petición a Cloudflare
            response = requests.post(
                url,
                headers={
                    "Authorization": f"Bearer {auth_token}",
                    "Content-Type": "application/json"
                },
                json=payload,
                timeout=60
            )

            if not response.ok:
                return Response(
                    {
                        "error": "Error de Cloudflare",
                        "detalle": response.text
                    },
                    status=status.HTTP_502_BAD_GATEWAY
                )

            datos = response.json()
            
            resultado_ai = datos.get("result", {})
            
            texto_ia = resultado_ai.get("response") or resultado_ai.get("text") or ""

            if isinstance(texto_ia, dict):
                resultado_json = texto_ia
            else:
                texto_limpio = re.sub(r"```json\s*|```", "", str(texto_ia)).strip()
                try:
                    resultado_json = json.loads(texto_limpio)
                except json.JSONDecodeError:
                    resultado_json = {"resultado_texto": texto_limpio}

            return Response({"resultado": resultado_json})

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
