from django.db import models
from users.models import MovieUser, GENRES

# Create your models here.

class MovieReview(models.Model):
    review = models.TextField(max_length=500)

    def __str__(self):
        return self.review

class Movies(models.Model):
    name = models.CharField(max_length=255, blank=False, unique = True, default="")
    genre = models.CharField(choices=GENRES, max_length=50, blank=False)
    release_date = models.DateField(blank=False)
    up_votes = models.PositiveSmallIntegerField(default=0)
    down_votes = models.SmallIntegerField(default=0)
    reviews = models.ManyToManyField(MovieReview, blank=False, default="")
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    modified_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['up_votes', 'down_votes', 'release_date']