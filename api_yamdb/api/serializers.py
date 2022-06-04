from rest_framework import serializers
from .serializers import CategoriesSerializer, GenresSerializer

from reviews.models import Categories, Genres, Titles


class TitlesReadSerializer(serializers.ModelSerializer):
    category = CategoriesSerializer(many = False)
    genre = GenresSerializer (many = True)
    rating = serializers.IntegerField()

    class Meta:
        model = Titles
        fields = '__all__'

class TitlesWriteSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many = False,
        queryset = Categories.objects.all()
    )
    genre = serializers.SlugRelatedField(
        many = False,
        queryset = Genres.objects.all()
    )
    year = serializers.IntegerField()
    class Meta:
        model = Titles
        fields = '__all__'

class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'