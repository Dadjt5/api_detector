from django.contrib import admin
from django.urls import path, include
from . import views


urlpatterns = [
    path("analizar/", views.analizarImagen.as_view(), name="analizar_imagen"),]