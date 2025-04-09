import os
import django
import sys

# Configurar Django
sys.path.append('c:\\Users\\aleja\\Documents\\Apps\\SIEF\\IntegradoraWebApps\\IntegradoraWeb')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'IntegradoraWeb.settings')
django.setup()

# Importar después de configurar Django
from django.core.mail import send_mail

try:
    print("Intentando enviar correo de prueba...")
    result = send_mail(
        'Prueba de correo SMTP',
        'Este es un mensaje de prueba para verificar la configuración de correo SMTP.',
        '20223tn058@utez.edu.mx',  # Remitente (tu correo institucional)
        ['20223tn053@utez.edu.mx'],  # Reemplaza con tu correo personal para verificar
        fail_silently=False,
    )
    print(f"Resultado del envío: {result}")
    print("Correo enviado correctamente.")
except Exception as e:
    print(f"Error al enviar correo: {e}")
    print(f"Tipo de error: {type(e).__name__}")