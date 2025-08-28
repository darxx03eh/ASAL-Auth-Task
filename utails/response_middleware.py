import json

from Scripts.bottle import response
from django.utils.deprecation import MiddlewareMixin
from django.http import JsonResponse
from rest_framework.response import Response as DRFResponse

class ResponseFormattingMiddleware:
    EXCLUDED_PATHS = [
        "/admin",  # Django admin
        "/api/schema",  # drf-spectacular schema
        "/api/schema/swagger-ui",  # Swagger UI
        "/api/schema/redoc",  # Redoc
    ]
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        path = request.path

        if any(path.startswith(p) for p in self.EXCLUDED_PATHS):
            return self.get_response(request)
        response = self.get_response(request)
        if isinstance(response, (JsonResponse, DRFResponse)):
            return self.format_response(response)
        return response

    def format_response(self, response):
        status_code = response.status_code
        succeeded = 200 <= status_code < 400

        # Extract DRF data
        if isinstance(response, DRFResponse):
            data = response.data
        else:
            try:
                data = json.loads(response.content.decode())
            except Exception:
                data = response.content.decode()

        formatted = {
            "statusCode": status_code,
            "meta": None,
            "succeeded": succeeded,
            "message": (data.pop("message", None) if isinstance(data, dict) else None) or (
                "Success" if succeeded else "Error"
            ),
            "errors": data.pop("errors", None) if isinstance(data, dict) else None,
            "data": data,
        }

        return JsonResponse(formatted, status=status_code, safe=False)