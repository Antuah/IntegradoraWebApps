from django.db import models
from preguntas.models import Pregunta

class Opcion(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='opciones')
    contenido = models.CharField(max_length=255)
    es_correcta = models.BooleanField(default=False)  # Define si es la opción correcta

    def __str__(self):
        return f"{self.contenido} (Correcta: {self.es_correcta})"
