from rest_framework import viewsets
from .models import Formulario
from .serializers import FormularioSerializer
from usuarios.models import Usuario
from django.shortcuts import render, get_object_or_404, redirect
from rest_framework.exceptions import ValidationError

class FormularioViewSet(viewsets.ModelViewSet):
    serializer_class = FormularioSerializer
    queryset = Formulario.objects.all()

    def perform_create(self, serializer):
        # Get the current user from the session
        user_id = self.request.session.get('user_id')
        if user_id:
            usuario = Usuario.objects.get(id=user_id)
            serializer.save(usuario=usuario)
        else:
            raise ValidationError("No user is logged in")

def index(request):
    return render(request, 'indexForm.html')

def view_form(request, form_id):
    formulario = get_object_or_404(Formulario, id=form_id)
    context = {
        'formulario': formulario,
        'user_id': request.session.get('user_id')  # Add this line
    }
    return render(request, 'viewForm.html', context)

def view_responses(request, form_id):
    formulario = get_object_or_404(Formulario, id=form_id)
    return render(request, 'viewResponses.html', {'formulario': formulario})

def manage_questions(request, form_id):
    formulario = get_object_or_404(Formulario, id=form_id)
    return render(request, 'manageQuestions.html', {'formulario': formulario})

def grade_responses(request, form_id):
    formulario = get_object_or_404(Formulario, id=form_id)
    # Verify ownership
    if formulario.usuario.id != request.session.get('user_id'):
        return redirect('dashboard')
    return render(request, 'gradeResponses.html', {'formulario': formulario})

def my_responses(request):
    if not request.session.get('user_id'):
        return redirect('login')
    return render(request, 'myResponses.html')
