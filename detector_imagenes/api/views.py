import base64
import os
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
            # Leer la imagen
            imagen_bytes = imagen.read()

            # Convertir imagen a Base64
            base64_image = base64.b64encode(imagen_bytes).decode("utf-8")

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
                f"@cf/meta/llama-3.2-11b-vision-instruct"
            )

            # Prompt para el modelo
            prompt = """
Identifica el elemento principal de esta imagen.

Responde únicamente con JSON válido usando exactamente este formato:

{
    "name": "nombre del elemento",
    "category": "animal, planta, objeto, lugar, alimento u otra categoría",
    "confidence": 0
}

confidence debe ser un número entre 0 y 100.
"""

            # Petición a Cloudflare
            response = requests.post(
                url,
                headers={
                    "Authorization": f"Bearer {auth_token}",
                    "Content-Type": "application/json"
                },
                json={
                    "prompt": prompt,
                    "image": base64_image
                },
                timeout=60
            )

            # Si Cloudflare devuelve error
            if not response.ok:
                return Response(
                    {
                        "error": "Error de Cloudflare",
                        "detalle": response.text
                    },
                    status=status.HTTP_502_BAD_GATEWAY
                )

            datos = response.json()

            # De momento devolvemos la respuesta de Cloudflare
            return Response({"resultado": datos})

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )