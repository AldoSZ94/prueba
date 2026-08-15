from django.urls import path
from . import views

app_name = "tareas"

urlpatterns = [
    path("", views.lista_tareas, name="lista_tareas"),
    path("nueva_tarea/", views.nueva_tarea, name="nueva_tarea"),
    path("editar_tarea/<int:tarea_id>/", views.editar_tarea, name="editar_tarea"),
    path("eliminar_tarea/<int:tarea_id>/", views.eliminar_tarea, name="eliminar_tarea"),
]
