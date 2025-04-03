from django.contrib import admin
from django.urls import path, include
from App.views import *
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('login'), name='root'),
    path('admin/', admin.site.urls),
    path('dashboard/', dashboard, name='dashboard'),
    path('compartidos/', include('compartidos.urls')),
    path('formularios/', include('formularios.urls')),
    path('preguntas/', include('preguntas.urls')),
    path('opciones/', include('opciones.urls')),
    path('respuestas/', include('respuestas.urls')),
    path('registroRespuestas/', include('registroRespuestas.urls')),
    path('usuarios/', include('usuarios.urls')),
]
