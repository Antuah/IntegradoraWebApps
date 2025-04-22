from django.db import models
from formularios.models import Formulario
from usuarios.models import Usuario

class RegistroRespuesta(models.Model):
    formulario = models.ForeignKey(Formulario, on_delete=models.CASCADE, related_name='registros')
    usuario = models.ForeignKey(Usuario, on_delete=models.SET_NULL, null=True, blank=True)
    fecha_envio = models.DateTimeField(auto_now_add=True)

    # --- NUEVO CAMPO ---
    puntaje_automatico = models.IntegerField(
        null=True, # Permite que esté vacío al inicio
        blank=True, # Permite que sea opcional
        verbose_name="Puntaje Automático", # Nombre legible en el admin
        help_text="Puntaje obtenido de preguntas de opción múltiple calificadas automáticamente."
    )
    # --- FIN NUEVO CAMPO ---

    def __str__(self):
        # Podemos añadir el puntaje al string si queremos
        # puntaje_str = f" - Puntaje: {self.puntaje_automatico}" if self.puntaje_automatico is not None else ""
        # return f"Registro en {self.formulario.titulo} ({self.fecha_envio}){puntaje_str}"
        return f"Registro para Formulario ID {self.formulario.id} ({self.fecha_envio})" # Versión segura

    # --- NUEVO MÉTODO PARA CALCULAR ---
    def calcular_puntaje_automatico(self):
        """
        Calcula el puntaje basado en las respuestas a preguntas de opción múltiple
        y lo guarda en el campo 'puntaje_automatico'.
        """
        puntaje_actual = 0
        # Obtenemos las respuestas asociadas a este registro, pero SOLO las que
        # corresponden a preguntas de tipo 'opcion_multiple'.
        # Usamos el related_name que definimos en Respuesta: 'respuestas_individuales'
        respuestas_calificables = self.respuestas_individuales.filter(
            pregunta__tipo='opcion_multiple'
        )

        for respuesta in respuestas_calificables:
            # Usamos el método que ya existe en el modelo Respuesta
            if respuesta.es_correcta():
                puntaje_actual += 1 # Sumamos 1 punto por cada correcta

        self.puntaje_automatico = puntaje_actual
        # Guardamos solo este campo para eficiencia y evitar efectos secundarios
        self.save(update_fields=['puntaje_automatico'])
        print(f"Puntaje calculado para Registro {self.id}: {puntaje_actual}") # Log para el servidor
        return puntaje_actual
    # --- FIN NUEVO MÉTODO ---