from functools import wraps
from django.http import HttpResponseForbidden

def is_entrenador(view_func):
    @wraps(view_func)
    def check_entrenador(request, *args, **kwargs):
        print(f"Checking if {request.user} is an Entrenador...")  # Debugging line
        if hasattr(request.user, 'entrenador') and request.user.entrenador is not None:
            print(f"{request.user} is an Entrenador.")  # Debugging line
            return view_func(request, *args, **kwargs)
        else:
            print(f"{request.user} is NOT an Entrenador.")  # Debugging line
            return HttpResponseForbidden("Access Denied")
    return check_entrenador
def is_cliente(view_func):
    """
    Decorator for restricting access to views for Cliente users.
    """
    @wraps(view_func)
    def check_cliente(request, *args, **kwargs):
        if hasattr(request.user, 'cliente') and request.user.cliente is not None:
            return view_func(request, *args, **kwargs)
        else:
            return HttpResponseForbidden("Access Denied")
    return check_cliente