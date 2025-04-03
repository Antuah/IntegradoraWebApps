from django.db import models
from formularios.models import Formulario

class Pregunta(models.Model):
    TIPO_PREGUNTA = (
        ('abierta', 'Pregunta Abierta'),
        ('opcion_multiple', 'Opción Múltiple')
    )
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE, related_name='preguntas')
    tipo = models.CharField(max_length=15, choices=TIPO_PREGUNTA)
    contenido = models.TextField()

    def __str__(self):
        return self.contenido
