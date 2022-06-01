from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import UserViewSet, get_jwt_token, register_new_user

v1_router = DefaultRouter()
v1_router.register(r'users', UserViewSet)

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', register_new_user, name='register_new_user'),
    path('v1/auth/token/', get_jwt_token, name='token')
]
