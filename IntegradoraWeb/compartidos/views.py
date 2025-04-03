from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from .models import Compartido
from .serializers import CompartidoSerializer

class CompartidoViewSet(viewsets.ModelViewSet):
    queryset = Compartido.objects.all()
    serializer_class = CompartidoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Filter compartidos based on user"""
        user = self.request.user
        if user.rol == 'admin':
            return Compartido.objects.all()
        return Compartido.objects.filter(usuario=user)