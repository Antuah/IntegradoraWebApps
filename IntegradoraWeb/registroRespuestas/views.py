from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import RegistroRespuesta
from .serializers import RegistroRespuestaSerializer

class RegistroRespuestaViewSet(viewsets.ModelViewSet):
    serializer_class = RegistroRespuestaSerializer
    permission_classes = [AllowAny]
    # Quitamos el queryset estático de aquí

    # Sobrescribimos el método que obtiene el queryset
    def get_queryset(self):
        """
        Este método se llama para obtener la lista de objetos.
        Aquí podemos filtrar basado en los parámetros de la URL.
        """
        queryset = RegistroRespuesta.objects.all() # Empezamos con todos

        # Buscamos si el parámetro 'formulario' vino en la URL (ej: ?formulario=1)
        formulario_id = self.request.query_params.get('formulario', None)

        if formulario_id is not None:
            # Si vino el parámetro, filtramos el queryset
            # Aseguramos que sea un número para evitar errores
            try:
                formulario_id = int(formulario_id)
                queryset = queryset.filter(formulario__id=formulario_id)
            except ValueError:
                # Si 'formulario' no es un número válido, devolvemos una lista vacía
                # o podríamos lanzar un error, pero devolver vacío es más simple.
                queryset = RegistroRespuesta.objects.none()

        return queryset # Devolvemos el queryset filtrado (o no, si no vino el param)

    def perform_create(self, serializer):
        serializer.save()