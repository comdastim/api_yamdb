from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (CategoriesViewSet, CommentViewSet, GenresViewSet,
                    ReviewViewSet, TitlesViewSet, UserViewSet, get_jwt_token,
                    register_new_user)

v1_router = DefaultRouter()
v1_router.register('users', UserViewSet)
v1_router.register('titles', TitlesViewSet, basename='title')
v1_router.register('categories', CategoriesViewSet, basename='category')
v1_router.register('genres', GenresViewSet, basename='genre')
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='reviews'
)
v1_router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments'
)

app_name = 'api'

urlpatterns = [
    path('v1/', include(v1_router.urls)),
    path('v1/auth/signup/', register_new_user, name='register_new_user'),
    path('v1/auth/token/', get_jwt_token, name='token')
]
