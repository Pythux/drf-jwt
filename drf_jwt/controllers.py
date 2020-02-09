from django.contrib.auth import authenticate
from django.contrib.auth.models import AnonymousUser
from rest_framework import status, permissions, authentication
from rest_framework.views import APIView
from rest_framework.response import Response

import jwt
from datetime import datetime

from .validators import Credentials
from .authentication import JSONWebTokenAuthentication


class Auth(APIView):
    # overide to escape permission and authentication
    permission_classes = [permissions.AllowAny]  # ⸄()⸅ works too
    authentication_classes = [authentication.BasicAuthentication, JSONWebTokenAuthentication]

    def get(self, request, format=None):
        # check for authentication:
        if isinstance(request.user, AnonymousUser):
            return Response({"detail": "Authentication credentials were not provided."},
                            status=status.HTTP_401_UNAUTHORIZED,
                            headers={'WWW-Authenticate': 'Basic realm="api"'})
        return Response(self.gen_jwt(request.user))

    def post(self, request, format=None):
        c = Credentials(data=request.data)
        if not c.is_valid():
            return Response(c.errors)

        user = authenticate(username=c.validated_data['login'],
                            password=c.validated_data['password'])
        if user is None:
            msg = 'Unable to log in with provided credentials.'
            return Response({'detail': msg}, status=status.HTTP_400_BAD_REQUEST)

        if not user.is_active:
            msg = 'User account is disabled.'
            return Response({'detail': msg}, status=status.HTTP_400_BAD_REQUEST)

        return Response(self.gen_jwt(user))

    def gen_jwt(self, user):
        payload = {'id': user.id, 'iat': datetime.utcnow()}
        encoded = jwt.encode(payload, 'secret', algorithm='HS256').decode()
        encoded = encoded.split('.', 1)[1]  # no header
        return {'jwt': encoded}  # the user.id is in the token at field "id"
        # return {'jwt': encoded, 'userId': user.id}
