from django.urls import path

from .views import get_jwt_token, register_new_user

urlpatterns = [
    path('v1/auth/signup/', register_new_user, name='register_new_user'),
    path('v1/auth/token/', get_jwt_token, name='token')
]
