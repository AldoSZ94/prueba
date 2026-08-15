from django.urls import path
from . import views

app_name = "usuarios"

urlpatterns = [
    path("registro/", views.registro, name="registro"),
    path("iniciar_sesion/", views.iniciar_sesion, name="iniciar_sesion"),
    path("cerrar_sesion/", views.cerrar_sesion, name="cerrar_sesion"),
]
