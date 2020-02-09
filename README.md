# drf-jwt
JSON Web Token plugin for Django REST Framework


### install:

pip install .


### let jwt do the authentification:

add 'drf_jwt.authentication.JSONWebTokenAuthentication' in authentication classes:
```python
'DEFAULT_AUTHENTICATION_CLASSES': [
    'drf_jwt.authentication.JSONWebTokenAuthentication',
]
```

### make endpoints to login, get the jwt:
```python
from drf_jwt.controllers import Auth

urlpatterns = [
    path('api/login', Auth.as_view()),
]
```

#### suport GET and POST

##### POST:
> { login, password }

login will be the username of the "authenticate" function


##### GET:
return a JWT token, given the fact that you are authenticate

so, one could do a Basic Authentication to the GET endpoints to receve a JWT
