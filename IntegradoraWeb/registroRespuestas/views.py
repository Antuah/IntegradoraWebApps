from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import RegistroRespuesta
from .serializers import RegistroRespuestaSerializer

class RegistroRespuestaViewSet(viewsets.ModelViewSet):
    serializer_class = RegistroRespuestaSerializer
    permission_classes = [AllowAny]
    queryset = RegistroRespuesta.objects.all()

    def perform_create(self, serializer):
        serializer.save()
