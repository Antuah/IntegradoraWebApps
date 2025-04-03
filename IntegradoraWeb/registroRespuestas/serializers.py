from rest_framework import serializers
from .models import RegistroRespuesta

class RegistroRespuestaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroRespuesta
        fields = ['id', 'formulario', 'usuario', 'fecha_envio']
        read_only_fields = ['fecha_envio']