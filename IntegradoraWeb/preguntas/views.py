from rest_framework import viewsets
from .models import Pregunta
from .serializers import PreguntaSerializer
from rest_framework.response import Response
from django.core.exceptions import ObjectDoesNotExist
import logging

logger = logging.getLogger(__name__)

class PreguntaViewSet(viewsets.ModelViewSet):
    serializer_class = PreguntaSerializer

    def get_queryset(self):
        queryset = Pregunta.objects.all()
        logger.info(f"Total questions in DB: {queryset.count()}")
        
        formulario_id = self.request.query_params.get('formulario')
        logger.info(f"Requested form ID: {formulario_id}")
        
        if formulario_id:
            try:
                form_id = int(formulario_id)
                queryset = queryset.filter(formulario_id=form_id)
                count = queryset.count()
                logger.info(f"Found {count} questions for form {form_id}")
                
                if count == 0:
                    logger.warning(f"No questions found for form {form_id}")
                else:
                    logger.info(f"Questions found: {[{q.id: q.contenido} for q in queryset]}")
                    
            except ValueError:
                logger.error(f"Invalid form ID format: {formulario_id}")
                return Pregunta.objects.none()
            except ObjectDoesNotExist:
                logger.error(f"Form {form_id} not found")
                return Pregunta.objects.none()
        
        return queryset

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        data = serializer.data
        logger.info(f"Returning {len(data)} serialized questions")
        return Response(data)
