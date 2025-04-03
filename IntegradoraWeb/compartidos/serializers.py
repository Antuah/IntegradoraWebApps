from rest_framework import serializers
from .models import Compartido
from formularios.serializers import FormularioSerializer
from usuarios.serializers import UsuarioSerializer

class CompartidoSerializer(serializers.ModelSerializer):
    formulario_details = FormularioSerializer(source='formulario', read_only=True)
    usuario_details = UsuarioSerializer(source='usuario', read_only=True)

    class Meta:
        model = Compartido
        fields = ['id', 'formulario', 'usuario', 'formulario_details', 'usuario_details']
        read_only_fields = ['id']