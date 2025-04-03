from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import RegistroRespuestaViewSet

router = DefaultRouter()
router.register(r'api', RegistroRespuestaViewSet, basename='registrorespuesta')

urlpatterns = [
    path('', include(router.urls)),
]