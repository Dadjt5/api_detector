from services.identificacion import analizar_imagen_completa
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
            resultado = analizar_imagen_completa(imagen)

            return Response(resultado, status=status.HTTP_200_OK)

        except Exception as e:
            return Response(
                {"error": str(e)},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
