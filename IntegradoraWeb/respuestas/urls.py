from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RespuestaViewSet

router = DefaultRouter()
router.register(r'api', RespuestaViewSet, basename='respuesta')

urlpatterns = [
    path('', include(router.urls)),
]