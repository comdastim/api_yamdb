from api.validators import year_validator
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class User(AbstractUser):
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('username',)
    ADMIN = 'admin'
    MODERATOR = 'moderator'
    USER = 'user'
    ROLES = [
        (ADMIN, 'Administrator'),
        (MODERATOR, 'Moderator'),
        (USER, 'User'),
    ]

    email = models.EmailField(
        verbose_name='Адрес электронной почты',
        unique=True,
    )
    role = models.CharField(
        verbose_name='Роль',
        max_length=50,
        choices=ROLES,
        default=USER
    )
    bio = models.TextField(
        verbose_name='О себе',
        null=True,
        blank=True
    )

    class Meta:
        ordering = ('id',)
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

        constraints = [
            models.CheckConstraint(
                check=~models.Q(username__iexact="me"),
                name="Использовать имя 'me' в качестве username запрещено!"
            )
        ]

    @property
    def is_moderator(self):
        return self.role == self.MODERATOR

    @property
    def is_admin(self):
        return self.role == self.ADMIN


class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField(max_length=200)
    genre = models.ManyToManyField(
        Genres,
        related_name='titles',
    )
    category = models.ForeignKey(
        Categories,
        related_name='titles',
        on_delete=models.SET_NULL,
        blank=True,
        null=True
    )
    description = models.TextField(max_length=200)
    year = models.PositiveSmallIntegerField(
        blank=True,
        null=True,
        validators=[year_validator, ]
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    text = models.TextField()
    title = models.ForeignKey(
        Title, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='reviews')
    score = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(10)]
    )
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('title', 'author',),
                name='unique_review'
            ),
        ]


class Comment(models.Model):
    text = models.TextField()
    review = models.ForeignKey(
        Review, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField(
        'Дата добавления', auto_now_add=True, db_index=True)
