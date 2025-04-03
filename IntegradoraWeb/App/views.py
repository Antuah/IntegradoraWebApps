from django.shortcuts import render
from formularios.models import Formulario

def dashboard(request):
    context = {
        'forms': Formulario.objects.all().order_by('-fecha_creacion'),
        'total_responses': Formulario.objects.count(),
        'shared_forms': 0,  # We'll implement this later with user authentication
        'recent_activity': [
            {'description': 'Nuevo formulario creado: Encuesta de Satisfacción'},
            {'description': 'Formulario actualizado: Evaluación de Curso'},
            {'description': 'Nueva respuesta recibida'},
        ]
    }
    return render(request, 'dashboard.html', context)