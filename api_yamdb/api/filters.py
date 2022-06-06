from reviews.models import Titles
from django_filters import rest_framework as filters


class TitlesFilter(filters.FilterSet):
    name = filters.CharFilter(
        field_name="name", lookup_expr='icontains'
    )
    category = filters.CharFilter(
        field_name="category_slug", lookup_expr='icontains'
    )
    genre = filters.CharFilter(
        field_name="genre_slug", lookup_expr='icontains'
    )
    year = filters.NumberFilter(
        field_name="year", lookup_expr='exact'
    )

    class Meta:
        model = Titles
        fields = ['name', 'category', 'genre', 'year']
