from rest_framework.routers import SimpleRouter
from django.urls import include, path

from . import views

router = SimpleRouter()
router.register('titles', views.TitlesViewSet, basename = 'title')
router.register('categories', views.CategoriesViewSet, basename = 'category')
router.register('genres', views.GenresViewSet, basename = 'genre')

urlpatterns = [
    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path('', include(router.urls)),
]