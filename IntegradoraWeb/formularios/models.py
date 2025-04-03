from django.db import models
from usuarios.models import Usuario

class Formulario(models.Model):
    titulo = models.CharField(max_length=255)
    descripcion = models.TextField(blank=True, null=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='formularios')

    def __str__(self):
        return self.titulo
