from rest_framework import viewsets, permissions, status


from .mixins import GetCreateDeleteViewSet
from reviews.models import Titles, Categories, Genres, User
from .serializers import (RegisterNewUserSerializer, TokenSerializer,
                        UserEditSerializer, UserSerializer, 
                        CategoriesSerializer, TitleReadSerializer,
                        TitleWriteSerializer, GenresSerializer)
from .permissions import IsAdminOrReadOnly, IsAdmin 

from api_yamdb.settings import DEFAULT_FROM_EMAIL
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404

from rest_framework.decorators import action, api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def register_new_user(request):
    serializer = RegisterNewUserSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    user = get_object_or_404(
        User,
        username=serializer.validated_data["username"]
    )
    confirmation_code = default_token_generator.make_token(user)
    send_mail(
        subject="Регистрация в сервисе YaMDb",
        message=f"Ваш код подтверждения: {confirmation_code}",
        from_email=DEFAULT_FROM_EMAIL,
        recipient_list=[user.email],
    )

    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(["POST"])
@permission_classes([permissions.AllowAny])
def get_jwt_token(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    user = get_object_or_404(
        User,
        username=serializer.validated_data["username"]
    )

    if default_token_generator.check_token(
        user, serializer.validated_data["confirmation_code"]
    ):
        token = AccessToken.for_user(user)
        return Response({"token": str(token)}, status=status.HTTP_200_OK)

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserViewSet(viewsets.ModelViewSet):
    lookup_field = "username"
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = PageNumberPagination
    permission_classes = (IsAdmin,)

    @action(
        methods=[
            "get",
            "patch",
        ],
        detail=False,
        url_path="me",
        permission_classes=(permissions.IsAuthenticated,),
        serializer_class=UserEditSerializer,
    )
    def user_edit_profile(self, request):
        user = request.user
        if request.method == "GET":
            serializer = self.get_serializer(user)
            return Response(serializer.data, status=status.HTTP_200_OK)
        if request.method == "PATCH":
            serializer = self.get_serializer(
                user,
                data=request.data,
                partial=True
            )
            serializer.is_valid(raise_exception=True)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)


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
