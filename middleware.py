from django.http import JsonResponse
from django.http import HttpResponseForbidden

from core.settings import CORS_ALLOWED_ORIGINS


class CorsMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        self.allowed_origins = CORS_ALLOWED_ORIGINS

    def __call__(self, request):
        if not len(self.allowed_origins):
            response = self.get_response(request)
            return response

        protocol = request.scheme
        host = request.META.get('REMOTE_ADDR')
        origin = f'{protocol}://{host}'
        if origin in self.allowed_origins:
            response = self.get_response(request)
            return response
        else:
            # Return an error in JSON format
            error_response_data = {
                "status_code": 403,
                "message": f"Origin is not allowed to access: {origin}",
                "data": {}
            }
            return JsonResponse(error_response_data, status=403)
