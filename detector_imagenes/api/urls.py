from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("analizar/", views.AnalizarImagenView.as_view(), name="analizar_imagen"),
    path("investigar/", views.ObtenerInformacion.as_view(), name="obtener_informacion"),
]
