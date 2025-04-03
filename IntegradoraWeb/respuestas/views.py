from rest_framework import viewsets
from rest_framework.permissions import AllowAny # O los permisos que necesites
from .models import Respuesta
from .serializers import RespuestaSerializer

class RespuestaViewSet(viewsets.ModelViewSet):
    serializer_class = RespuestaSerializer
    permission_classes = [AllowAny]
    # Quitamos el queryset estático de aquí

    # Sobrescribimos el método que obtiene el queryset
    def get_queryset(self):
        """
        Filtra el queryset para devolver solo las respuestas
        asociadas con un 'registro' específico, si se proporciona
        el parámetro en la URL.
        """
        # Empezamos con el queryset base que incluye todas las respuestas
        queryset = Respuesta.objects.all()

        # Buscamos si el parámetro 'registro' vino en la URL (ej: ?registro=1)
        registro_id = self.request.query_params.get('registro', None)

        if registro_id is not None:
            # Si vino el parámetro 'registro', filtramos el queryset
            try:
                # Filtramos donde el campo 'registro' (ForeignKey) tenga el ID proporcionado
                queryset = queryset.filter(registro__id=int(registro_id))
            except (ValueError, TypeError):
                # Si 'registro' no es un número válido, devolvemos lista vacía
                queryset = Respuesta.objects.none()

        # Devolvemos el queryset filtrado (o el original si no vino 'registro')
        return queryset

    def perform_create(self, serializer):
        # Esto está bien para guardar nuevas respuestas (POST)
        # Asegúrate que el serializer maneje bien el campo 'registro' que recibe
        serializer.save()