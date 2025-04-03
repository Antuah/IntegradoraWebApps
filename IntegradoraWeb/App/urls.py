from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FormularioViewSet, dashboard

router = DefaultRouter()
router.register(r'formularios', FormularioViewSet, basename='formulario')

urlpatterns = [
    path('dashboard/', dashboard, name='dashboard'),
    path('api/', include(router.urls)),
]