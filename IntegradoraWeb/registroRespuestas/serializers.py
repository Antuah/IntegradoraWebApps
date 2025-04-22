from rest_framework import serializers
from .models import RegistroRespuesta

class RegistroRespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroRespuesta
        # --- AÑADIR 'puntaje_automatico' ---
        fields = ['id', 'formulario', 'usuario', 'fecha_envio', 'puntaje_automatico']
        # --- Hacerlo de solo lectura para evitar que se modifique directamente ---
        read_only_fields = ['fecha_envio', 'puntaje_automatico']