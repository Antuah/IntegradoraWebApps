from rest_framework import serializers
from .models import Opcion

class OpcionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Opcion
        fields = ['id', 'pregunta', 'contenido', 'es_correcta']