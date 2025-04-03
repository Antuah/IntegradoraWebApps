from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import OpcionViewSet

router = DefaultRouter()
router.register(r'api', OpcionViewSet, basename='opcion')

urlpatterns = [
    path('', include(router.urls)),
]