from django.conf import settings
from rest_framework.settings import APISettings


USER_SETTINGS = getattr(settings, 'JWT_AUTH', None)

DEFAULTS = {
    'USER_LOGIN': 'username',
    'JWT_SECRET_KEY': settings.SECRET_KEY,
    'JWT_CONTENT': 'drf_jwt.utils.jwt_content',
    'GET_PAYLOAD_USER_ID': 'drf_jwt.utils.get_payload_user_id',
}

# List of settings that may be in string import notation.
IMPORT_STRINGS = (
    'JWT_CONTENT',
    'GET_PAYLOAD_USER_ID',
)
api_settings = APISettings(USER_SETTINGS, DEFAULTS, IMPORT_STRINGS)
