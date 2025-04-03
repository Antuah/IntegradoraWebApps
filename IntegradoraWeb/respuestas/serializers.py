# serializers.py (para Respuesta)

from rest_framework import serializers
from .models import Respuesta
# Asegúrate de importar RegistroRespuesta si es necesario para validación, aunque no explícito aquí
# from .models import RegistroRespuesta

class RespuestaSerializer(serializers.ModelSerializer):
    es_correcta = serializers.BooleanField(read_only=True)

    # Opcional: Si quieres mostrar detalles del registro al leer una respuesta
    # registro_details = RegistroRespuestaSerializer(source='registro', read_only=True)

    class Meta:
        model = Respuesta
        # --- AÑADIR 'registro' A LA LISTA ---
        fields = [
            'id',
            'pregunta',
            'usuario',
            'contenido',
            'fecha_respuesta',
            'validada',
            'es_correcta',
            'registro' # <-- AÑADIDO AQUÍ
            # 'registro_details' # Descomenta si añadiste la línea opcional de arriba
        ]
        read_only_fields = ['fecha_respuesta']
        # 'registro' por defecto será escribible (espera un ID)