from django.shortcuts import redirect
from django.urls import reverse

class AuthenticationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # URLs that don't require authentication
        public_urls = ['/usuarios/login/']
        
        if request.path not in public_urls and not request.path.startswith('/static/'):
            if not request.session.get('user_id'):
                return redirect('login')
        
        response = self.get_response(request)
        return response