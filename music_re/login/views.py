from django.http import HttpResponseForbidden, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from django.contrib.auth import authenticate, login as django_login

import response_code
import json

from logger import get_logger
logger = get_logger()


@require_POST
@csrf_exempt
def login(request):
    try:
        request_data = json.loads(request.body)
        username = request_data.get('username').strip()
        password = request_data.get('password')
    except Exception as ex:
        logger.error(f'Error in login while parsing the parameters: {ex}')
        return HttpResponseForbidden('MESSAGE_INVALID_LOGIN_PARAMS')

    if username and password:
        django_user = authenticate(username=username, password=password)
    else:
        django_user = None

    if django_user:
        django_login(request, django_user)
        return HttpResponse(response_code.SUCCESS)
    else:
        return HttpResponseForbidden('MESSAGE_INVALID_LOGIN')
