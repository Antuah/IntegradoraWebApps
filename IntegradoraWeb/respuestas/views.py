from rest_framework import viewsets
from rest_framework.permissions import AllowAny
from .models import Respuesta
from .serializers import RespuestaSerializer

class RespuestaViewSet(viewsets.ModelViewSet):
    serializer_class = RespuestaSerializer
    permission_classes = [AllowAny]
    queryset = Respuesta.objects.all()

    def perform_create(self, serializer):
        serializer.save()
