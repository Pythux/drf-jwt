from datetime import datetime
from .settings import api_settings
import jwt


def gen_jwt(user):
    """given a user, return the jwt"""
    return gen_jwt_with_content(api_settings.JWT_CONTENT(user))


def gen_jwt_with_content(content):
    if 'iat' in content:
        raise ValueError("iat can't be in content, this key is used bye drf_jwt")
    payload = {**content, 'iat': datetime.utcnow()}
    encoded = jwt.encode(payload, api_settings.JWT_SECRET_KEY, algorithm='HS256').decode()
    encoded = encoded.split('.', 1)[1]  # no header
    return encoded  # the user.id is in the token at field "id"


def jwt_content(user):
    return {'id': user.id}


def get_payload_user_id(payload):
    return payload['id']
