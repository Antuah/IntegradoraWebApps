from rest_framework import viewsets
from django.shortcuts import render
from .models import Usuario
from .serializers import UsuarioSerializer

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

def index(request):
    return render(request, 'index.html')
