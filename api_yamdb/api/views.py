from rest_framework import viewsets, permissions

from .mixins import GetCreateDeleteViewSet
from reviews.models import Titles, Categories, Genres
from .serializers import CategoriesSerializer, TitleReadSerializer, TitleWriteSerializer, GenresSerializer
from .permissions import IsAdminOrReadOnly 


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Titles.objects.all()
    serializer_class = TitleReadSerializer
    permission_classes = (IsAdminOrReadOnly,)

    def get_serializer_class(self):
        if self.request.method in ['POST', 'PATCH']:
            return TitleWriteSerializer
        return TitleReadSerializer


class CategoryViewSet(GetCreateDeleteViewSet):
    queryset = Categories.objects.all()
    serializer_class = CategoriesSerializer 
    permission_classes = (IsAdminOrReadOnly,)


class GenreViewSet(GetCreateDeleteViewSet):
    queryset = Genres.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (IsAdminOrReadOnly,)
