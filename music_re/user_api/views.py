from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from django.contrib.auth.models import User as DjangoUser

import response_code

from logger import get_logger
logger = get_logger()


class UserViewSet(viewsets.ModelViewSet):

    @action(methods=['post'], url_path='create', detail=False)
    def create_user(self, request):
        data = request.data
        username = data['username']
        password = data['password']

        try:
            user_model = DjangoUser.objects.create_user(username=username, password=password)
            return_code = response_code.SUCCESS
        except Exception as ex:
            logger.error(f'error in create_user: {ex}')
            return_code = response_code.UNEXPECTED_ERROR

        return Response({
            'RETURN_CODE': return_code
        })
