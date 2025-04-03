from django.db import models
from preguntas.models import Pregunta  # Changed import
from formularios.models import Formulario  # Changed import
from usuarios.models import Usuario  # Added missing import
from opciones.models import Opcion  # Added missing import

class Respuesta(models.Model):
    pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE, related_name='respuestas')
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    contenido = models.TextField()
    fecha_respuesta = models.DateTimeField(auto_now_add=True)
    validada = models.BooleanField(null=True, blank=True)  # Para preguntas abiertas (None = No revisada)

    def es_correcta(self):
        """Determina si la respuesta es correcta"""
        if self.pregunta.tipo == 'opcion_multiple':
            return Opcion.objects.filter(pregunta=self.pregunta, contenido=self.contenido, es_correcta=True).exists()
        return self.validada  # Para preguntas abiertas, el dueño del formulario la valida

    def __str__(self):
        estado = "Sin validar" if self.validada is None else ("Correcta" if self.validada else "Incorrecta")
        return f"Respuesta: {self.contenido} - {estado}"

