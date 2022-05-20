from functools import wraps
from django.conf import settings
from django.contrib.auth.views import redirect_to_login as dj_redirect_to_login
from django.core.exceptions import PermissionDenied

try:
    from collections.abc import Callable
except ImportError:
    from collections import Callable


def has_permission_decorator(redirect_to_login=None):
    def request_decorator(dispatch):
        @wraps(dispatch)
        def wrapper(view_set, *args, **kwargs):
            request = args[0]
            user = request.user
            if isinstance(user.is_authenticated, Callable):
                authenticated = user.is_authenticated()
            else:
                authenticated = user.is_authenticated
            if authenticated:
                return dispatch(view_set, *args, **kwargs)

            redirect = redirect_to_login
            if redirect is None:
                redirect = getattr(
                    settings, 'ROLEPERMISSIONS_REDIRECT_TO_LOGIN', False)
            if redirect:
                return dj_redirect_to_login(request.get_full_path())
            raise PermissionDenied
        return wrapper
    return request_decorator
