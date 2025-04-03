from django.db import models
from formularios.models import Formulario
from usuarios.models import Usuario

class Compartido(models.Model):
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE, related_name='compartidos')
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='formularios_compartidos')

    class Meta:
        unique_together = ('formulario', 'usuario')  # Evita compartir un formulario más de una vez con el mismo usuario

    def __str__(self):
        return f"{self.formulario.titulo} → {self.usuario.username}"
