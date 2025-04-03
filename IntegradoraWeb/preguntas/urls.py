from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import PreguntaViewSet

router = DefaultRouter()
router.register(r'api', PreguntaViewSet, basename='pregunta')

urlpatterns = [
    path('', include(router.urls)),
]