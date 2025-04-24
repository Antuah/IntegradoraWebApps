from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny
from .models import RegistroRespuesta
from .serializers import RegistroRespuestaSerializer

class RegistroRespuestaViewSet(viewsets.ModelViewSet):
    serializer_class = RegistroRespuestaSerializer
    permission_classes = [AllowAny] # O los permisos adecuados

    # --- Ajustar get_queryset si no lo hicimos antes ---
    def get_queryset(self):
        queryset = RegistroRespuesta.objects.all()
        formulario_id = self.request.query_params.get('formulario', None)
        if formulario_id is not None:
            try:
                queryset = queryset.filter(formulario__id=int(formulario_id))
            except (ValueError, TypeError):
                queryset = RegistroRespuesta.objects.none()
        return queryset

    def perform_create(self, serializer):
        serializer.save() # La creación normal

    # --- NUEVA ACCIÓN PERSONALIZADA ---
    @action(detail=True, methods=['post'], url_path='calcular-puntaje')
    def calcular_puntaje(self, request, pk=None):
        """
        Endpoint para calcular y guardar el puntaje automático de un RegistroRespuesta específico.
        Se accede vía POST a /registroRespuestas/api/{id_registro}/calcular-puntaje/
        """
        try:
            # Obtenemos la instancia del RegistroRespuesta usando el id (pk) de la URL
            registro = self.get_object()
            # Llamamos al método que definimos en el modelo
            puntaje = registro.calcular_puntaje_automatico()
            # Devolvemos una respuesta de éxito con el puntaje calculado
            return Response({
                'status': 'puntaje calculado con éxito',
                'puntaje_automatico': puntaje
            })
        except Exception as e:
            # Loguear el error 'e' sería bueno en un proyecto real
            print(f"Error calculando puntaje para registro {pk}: {e}")
            return Response(
                {'error': 'Ocurrió un error interno al calcular el puntaje.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR
            )
    # --- FIN NUEVA ACCIÓN ---

    @action(detail=False, methods=['get'], url_path='mis-respuestas')
    def mis_respuestas(self, request):
        user_id = request.session.get('user_id')
        if not user_id:
            return Response({'error': 'No autorizado'}, status=401)
            
        registros = RegistroRespuesta.objects.filter(
            usuario_id=user_id
        ).order_by('-fecha_envio')
        
        serializer = self.get_serializer(registros, many=True)
        return Response(serializer.data)