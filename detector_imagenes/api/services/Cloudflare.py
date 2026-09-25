import base64
import json
import os
import re
import requests



from dotenv import load_dotenv
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

def identificar_imagen(imagen, prompt):
    try:
        image_bytes = imagen.read()
        image_b64 = base64.b64encode(image_bytes).decode('utf-8')
    
        account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID")
        auth_token = os.getenv("CLOUDFLARE_AUTH_TOKEN")
    
        if not account_id or not auth_token:
            raise Exception("Faltan las credenciales de Cloudflare")
    
        # URL de Workers AI
        url = (
            f"https://api.cloudflare.com/client/v4/accounts/"
            f"{account_id}/ai/run/"
            f"@cf/meta/llama-4-scout-17b-16e-instruct"
        )
    
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
            raise Exception("Error de Cloudflare")
            
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
            
        return resultado_json
    
    except Exception as e:
        raise Exception(f"Error al obtener información: {str(e)}")


def obtener_informacion(prompt):
    try:
        account_id = os.getenv("CLOUDFLARE_ACCOUNT_ID")
        auth_token = os.getenv("CLOUDFLARE_AUTH_TOKEN")
    
        if not account_id or not auth_token:
            raise Exception("Faltan las credenciales de Cloudflare")
    
        # URL de Workers AI
        url = (
            f"https://api.cloudflare.com/client/v4/accounts/"
            f"{account_id}/ai/run/"
            f"@cf/meta/llama-4-scout-17b-16e-instruct"
        )
    
        payload = {
               "messages": [
                {
                    "role": "user",
                    "content": [
                    {
                        "type": "text", 
                        "text": prompt
                    },
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
            raise Exception("Error de Cloudflare")
            
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
            
        return resultado_json
    
    except Exception as e:
        raise Exception(f"Error al obtener información: {str(e)}")
