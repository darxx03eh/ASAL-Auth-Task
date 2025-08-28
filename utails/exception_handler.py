from http import HTTPStatus

from rest_framework.views import exception_handler
def custom_exception_handler(exc, context):
    handlers={
        'ValidationError': _handle_generic_error,
        'Http404': _handle_generic_error,
        'PermissionDenied': _handle_generic_error,
        'NotAuthenticated': _handle_authentication_error,
        'AuthenticationFailed': _handle_authentication_failed,
        'InvalidToken': _handle_authentication_failed,
    }
    response = exception_handler(exc, context)
    exception_class = exc.__class__.__name__
    if exception_class in handlers:
        return handlers[exception_class](exc, context, response)
    return response
def _handle_authentication_failed(exc, context, response):
    print('test')
    response.status_code = HTTPStatus.UNAUTHORIZED
    response.data = {
        'message': 'Authentication failed or Invalid credentials.',
        'status_code': HTTPStatus.UNAUTHORIZED
    }
    return response
def _handle_authentication_error(exc, context, response):
    response.status_code = HTTPStatus.UNAUTHORIZED
    response.data = {
        'error': 'please login first',
        'status_code': HTTPStatus.UNAUTHORIZED
    }
    return response
def _handle_generic_error(exc, context, response):
    return response