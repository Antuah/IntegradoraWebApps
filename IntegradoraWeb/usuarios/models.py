from django.db import models

class Usuario(models.Model):
    ROLES = (
        ('admin', 'Administrador'),
        ('normal', 'Usuario Normal')
    )
    username = models.EmailField(unique=True)  # Correo como nombre de usuario
    password = models.CharField(max_length=255)
    token_recuperacion = models.CharField(max_length=255, blank=True, null=True)
    rol = models.CharField(max_length=10, choices=ROLES, default='normal')

    def __str__(self):
        return self.username
