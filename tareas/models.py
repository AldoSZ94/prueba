from datetime import date

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models


class Tarea(models.Model):

    class Prioridad(models.TextChoices):
        BAJA = "baja", "Baja"
        MEDIA = "media", "Media"
        ALTA = "alta", "Alta"

    titulo = models.CharField("Título", max_length=100)
    descripcion = models.TextField("Descripción", blank=True)
    prioridad = models.CharField(
        "Prioridad", max_length=10, choices=Prioridad.choices, default=Prioridad.BAJA
    )
    fecha_limite = models.DateField("Fecha límite", blank=True, null=True)
    completado = models.BooleanField("Completado", default=False)
    fecha_creacion = models.DateTimeField("Fecha de creación", auto_now_add=True)
    fecha_actualizacion = models.DateTimeField("Última actualización", auto_now=True)
    usuario = models.ForeignKey(
        User, verbose_name="Usuario", on_delete=models.CASCADE, related_name="tareas"
    )

    def __str__(self):
        return f"{self.titulo} - {self.usuario}"
