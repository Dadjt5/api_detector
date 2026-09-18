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
Analiza la imagen con mucho cuidado.

Primero determina qué tipo de elemento aparece de entre estos:
animal, planta, mineral u otro.

Determina primero la categoria, esto va a ser su clase, por ejemplo los animales pueden ser ave, mamifero, insecto, pez, etc.
Las plantas pueden ser planta herbácea, y los minealres igual, pueden ser silicatos, sulfuros, oxidos, etc.

Después intenta identificar la especie.

IMPORTANTE:
- No inventes una especie.
- Si no puedes identificarlo con suficiente seguridad,
  indica una identificación más general.
- La confianza debe reflejar realmente la calidad de la evidencia visual.

Finalmente en el caso de animales y plantas indica su habitat y si es venenoso o no. En el caso de los minerales estos campos dejalos vacios e indica la dureza aproximada.

Devuelve UNICAMENTE el objeto JSON puro, sin bloques de código Markdown (```json) ni explicaciones adicionales:

{
  "tipo": "Tipo de entre los especificados (planta, animal, persona, mineral u otro)",
  "name": "Nombre común",
  "scientific_name": "Nombre científico",
  "descripcion": "Breve descripción real sobre el elemento",
  "category": "Categoría",
  "habitat": "Habitat o habitats",
  "venenoso": "Responde solo si o no",
  "dureza": "Solo para la dureza de los minerales",
  "confidence": 0
}

Recuerda que las palabras y oraciones comienzan con mayuscula, pero no las etiquetas, esas tal cual estan.
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
