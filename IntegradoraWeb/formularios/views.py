from rest_framework import viewsets
from .models import Formulario
from .serializers import FormularioSerializer
from usuarios.models import Usuario
from django.shortcuts import render, get_object_or_404

class FormularioViewSet(viewsets.ModelViewSet):
    serializer_class = FormularioSerializer
    queryset = Formulario.objects.all()

    def perform_create(self, serializer):
        # Temporarily assign to the first user in the system
        default_user = Usuario.objects.first()
        if default_user:
            serializer.save(usuario=default_user)
        else:
            # Create a default user if none exists
            default_user = Usuario.objects.create(
                username="default@example.com",
                password="default",
                rol="admin"
            )
            serializer.save(usuario=default_user)

def index(request):
    return render(request, 'indexForm.html')

def view_form(request, form_id):
    formulario = get_object_or_404(Formulario, id=form_id)  # Verifica que existe el formulario
    return render(request, 'viewForm.html', {'formulario': formulario})

def view_responses(request, form_id):
    formulario = get_object_or_404(Formulario, id=form_id)
    return render(request, 'viewResponses.html', {'formulario': formulario})

def manage_questions(request, form_id):
    formulario = get_object_or_404(Formulario, id=form_id)
    return render(request, 'manageQuestions.html', {'formulario': formulario})
