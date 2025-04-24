from rest_framework import viewsets
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib.auth.hashers import check_password, make_password
from .models import Usuario
from rest_framework import viewsets
from .serializers import UsuarioSerializer
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.hashers import make_password
import uuid
from django.core.mail import send_mail
from django.urls import reverse
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
            
            # Verificar si la contraseña está cifrada (comienza con algoritmo de hash)
            is_hashed = user.password.startswith(('pbkdf2_sha256$', 'bcrypt$', 'argon2'))
            
            # Si está cifrada, usar check_password, si no, comparar directamente
            password_valid = check_password(password, user.password) if is_hashed else password == user.password
            
            if password_valid:
                # Si la contraseña no estaba cifrada, cifrarla ahora
                if not is_hashed:
                    user.password = make_password(password)
                    user.save()
                
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


def solicitar_recuperacion(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        try:
            usuario = Usuario.objects.get(username=email)
            # Generar token único
            token = str(uuid.uuid4())
            usuario.token_recuperacion = token
            usuario.save()
            
            # Construir URL de recuperación
            reset_url = request.build_absolute_uri(
                reverse('restablecer_password', args=[token])
            )
            
            # Enviar correo
            send_mail(
                'Recuperación de contraseña - FormSIEF',
                f'Haz clic en el siguiente enlace para restablecer tu contraseña: {reset_url}',
                EMAIL_HOST_USER,
                [email],
                fail_silently=False,
            )
            
            return render(request, 'solicitar_recuperacion.html', {
                'mensaje': 'Se ha enviado un correo con instrucciones para recuperar tu contraseña.'
            })
        except Usuario.DoesNotExist:
            return render(request, 'solicitar_recuperacion.html', {
                'error': 'No existe una cuenta con ese correo electrónico.'
            })
    
    return render(request, 'solicitar_recuperacion.html')

def restablecer_password(request, token):
    try:
        usuario = Usuario.objects.get(token_recuperacion=token)
        
        if request.method == 'POST':
            password = request.POST.get('password')
            password_confirm = request.POST.get('password_confirm')
            
            if password != password_confirm:
                return render(request, 'restablecer_password.html', {
                    'error': 'Las contraseñas no coinciden.'
                })
            
            # Actualizar contraseña y limpiar token
            usuario.password = make_password(password)
            usuario.token_recuperacion = None
            usuario.save()
            
            return redirect('login')
        
        return render(request, 'restablecer_password.html', {'token': token})
    
    except Usuario.DoesNotExist:
        return render(request, 'error.html', {
            'mensaje': 'El enlace de recuperación no es válido o ha expirado.'
        })


def logout_view(request):
    # Clear all session data
    request.session.flush()
    # Redirect to login page
    return redirect('login')


def profile_view(request):
    if not request.session.get('user_id'):
        return redirect('login')
    
    user = get_object_or_404(Usuario, id=request.session.get('user_id'))
    return render(request, 'profile.html', {'user': user})
