from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views
from. views import FormularioViewSet
from. views import view_form

router = DefaultRouter()
router.register(r'api', FormularioViewSet, basename='formulario')

urlpatterns = [
    path('agregar/', views.index, name='formularios_index'),
    path('', include(router.urls)),
    path('view/<int:form_id>/', view_form, name='view_form'),
    path('responses/<int:form_id>/', views.view_responses, name='view_responses'),
    path('mis-respuestas/', views.my_responses, name='my_responses'),
    path('<int:form_id>/preguntas/', views.manage_questions, name='manage_questions'),
    path('<int:form_id>/calificar/', views.grade_responses, name='grade_responses'),
]