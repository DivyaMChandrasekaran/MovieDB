from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

GENRES = [
    (1, 'Comedy'),
    (2, 'Sci-fi'),
    (3, 'Horror'),
    (4, 'Romance'),
    (5, 'Action'),
    (6, 'Thriller'),
    (7, 'Drama'),
    (8, 'Mystery'),
    (9, 'Crime'),
    (10, 'Animation'),
    (11, 'Adventure'),
    (12, 'Fantasy')
]


class MovieUser(AbstractUser):
    fav_genre = models.CharField(blank=True, choices=GENRES, max_length=50)
    last_login = models.DateTimeField(auto_now=True, null=True)