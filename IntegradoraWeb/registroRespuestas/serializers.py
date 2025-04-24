from rest_framework import serializers
from .models import RegistroRespuesta

class RegistroRespuestaSerializer(serializers.ModelSerializer):
    usuario_username = serializers.CharField(source='usuario.username', read_only=True)
    class Meta:
        model = RegistroRespuesta
        model = RegistroRespuesta
        fields = ['id', 'formulario', 'usuario', 'fecha_envio', 'puntaje_automatico', 'usuario_username']        
        read_only_fields = ['fecha_envio', 'puntaje_automatico']
