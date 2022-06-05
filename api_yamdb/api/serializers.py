from rest_framework import serializers

from reviews.models import Categories, Genres, Titles, User
from rest_framework.validators import UniqueValidator


class RegisterNewUserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    def validate_username(self, value):
        if value.lower() == "me":
            raise serializers.ValidationError(
                "Имя пользователя не может быть 'me'!"
            )
        return value

    class Meta:
        fields = ("username", "email")
        model = User


class TokenSerializer(serializers.Serializer):
    username = serializers.CharField()
    confirmation_code = serializers.CharField()


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ],
        required=True,
    )
    email = serializers.EmailField(
        validators=[
            UniqueValidator(queryset=User.objects.all())
        ]
    )

    class Meta:
        fields = ("username", "email", "first_name",
                  "last_name", "bio", "role")
        model = User


class UserEditSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("username", "email", "first_name",
                  "last_name", "bio", "role")
        model = User
        read_only_fields = ('role',)


class CategoriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = '__all__'

class GenresSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genres
        fields = '__all__'


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

