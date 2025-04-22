from django.shortcuts import redirect
from django.urls import reverse

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # URLs that don't require authentication
        public_urls = [
            '/usuarios/login/', 
            '/usuarios/recuperar-password/',
            '/usuarios/restablecer-password/'
        ]
        
        # Check if the path starts with any of the public URLs
        is_public = any(request.path.startswith(url) for url in public_urls) or request.path.startswith('/static/')
        
        if not is_public and not request.session.get('user_id'):
            return redirect('login')
        
        response = self.get_response(request)
        return response