from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import check_password
from .models import Usuario
from rest_framework import viewsets
from .serializers import UsuarioSerializer

from django.contrib.auth.hashers import make_password

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

    def perform_create(self, serializer):
        # Hash password before saving
        password = serializer.validated_data.get('password')
        if password:
            serializer.validated_data['password'] = make_password(password)
        serializer.save()

    def perform_update(self, serializer):
        # Hash password only if it's being updated
        password = serializer.validated_data.get('password')
        if password:
            serializer.validated_data['password'] = make_password(password)
        serializer.save()

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        try:
            user = Usuario.objects.get(username=username)
            # Temporary: Direct password comparison since passwords aren't hashed yet
            if password == user.password:
                request.session['user_id'] = user.id
                request.session['user_role'] = user.rol
                return redirect('dashboard')
            else:
                return render(request, 'login.html', {'error': 'Credenciales inválidas'})
        except Usuario.DoesNotExist:
            return render(request, 'login.html', {'error': 'Usuario no encontrado'})
    
    return render(request, 'login.html')

def index(request):
    return render(request, 'index.html')
