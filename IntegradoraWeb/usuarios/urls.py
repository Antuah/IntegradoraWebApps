from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'api', views.UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('login/', views.login_view, name='login'),
    path('agregar/', views.index, name='usuarios_index'),
    path('', include(router.urls)),
]