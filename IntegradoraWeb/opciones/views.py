from rest_framework import viewsets
from .models import Opcion
from .serializers import OpcionSerializer

class OpcionViewSet(viewsets.ModelViewSet):
    serializer_class = OpcionSerializer

    def get_queryset(self):
        pregunta_id = self.request.query_params.get('pregunta', None)
        if pregunta_id:
            return Opcion.objects.filter(pregunta_id=pregunta_id)
        return Opcion.objects.all()
