
from django.db import models
from api.validators import year_validator


class Categories(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name


class Genres(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(
        Categories,
        related_name='genres',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name


class Titles(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    genre = models.ManyToManyField(
        Genres,
        related_name='titles',
    )
    category = models.ForeignKey(
        Categories,
        related_name='titles',
        on_delete=models.SET_NULL,
        blank = True,
        null=True
    )
    description = models.TextField(max_length=200)
    year = models.IntegerField(
        blank = True,
        null = True,
        validators = [year_validator,] 
    )

    def __str__(self):
        return self.name
