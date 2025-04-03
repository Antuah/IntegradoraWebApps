from rest_framework import serializers
from .models import Formulario

class FormularioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formulario
        fields = ['id', 'titulo', 'descripcion', 'fecha_creacion', 'usuario']
        read_only_fields = ['fecha_creacion']
        extra_kwargs = {
            'usuario': {'required': False}  # Make usuario field optional
        }