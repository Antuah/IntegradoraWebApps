from django.db import models
from formularios.models import Formulario
from usuarios.models import Usuario

class RegistroRespuesta(models.Model):
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE, related_name='registros')
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)  # Puede ser anónimo
    fecha_envio = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Registro en {self.formulario.titulo} ({self.fecha_envio})"
