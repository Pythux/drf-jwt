# drf-jwt
JSON Web Token plugin for Django REST Framework,
the JWT `encoded in base64` is put in the headers:

> `Authorization: Bearer <token>`


### install:

pip install django-rest-jwt


### let JWT do the authentification:

add 'drf_jwt.authentication.JSONWebTokenAuthentication' in authentication classes:
```python
'DEFAULT_AUTHENTICATION_CLASSES': [
    'drf_jwt.authentication.JSONWebTokenAuthentication',
]
```

### make endpoints to login and get the JWT:
```python
from drf_jwt.controllers import Auth

urlpatterns = [
    path('api/login', Auth.as_view()),
]
```

#### suport GET and POST

##### POST:

> { login, password }

login will be the username of the `authenticate` function of django


##### GET:

return a JWT token if you are authenticate

so, one could do a Basic Authentication to the GET endpoints to receve a JWT
