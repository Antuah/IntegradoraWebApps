from rest_framework import serializers
from .models import Respuesta

class RespuestaSerializer(serializers.ModelSerializer):
    es_correcta = serializers.BooleanField(read_only=True)
    
    class Meta:
        model = Respuesta
        fields = ['id', 'pregunta', 'usuario', 'contenido', 'fecha_respuesta', 'validada', 'es_correcta']
        read_only_fields = ['fecha_respuesta']