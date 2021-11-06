from django.db import models
from django.contrib.auth.models import AbstractUser
from movies.models import GENRES

# Create your models here.
class MovieUser(AbstractUser):
    fav_genre = models.CharField(blank=True, choices=GENRES, max_length=50)
    last_login = models.DateTimeField(auto_now=True, null=True)