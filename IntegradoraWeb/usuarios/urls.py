from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api', views.UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('agregar/', views.index, name='usuarios_index'),
    path('recuperar-password/', views.solicitar_recuperacion, name='solicitar_recuperacion'),
    path('restablecer-password/<str:token>/', views.restablecer_password, name='restablecer_password'),
    path('', include(router.urls)),
]