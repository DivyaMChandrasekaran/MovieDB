from django.db import models

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
# Create your models here.
class Movies(models.Model):
    name = models.CharField(max_length=255, blank=False, unique = True, default="")
    genre = models.CharField(choices=GENRES, max_length=50, blank=False)
    release_date = models.DateField(blank=False)
    up_votes = models.PositiveSmallIntegerField(default=0)
    down_votes = models.SmallIntegerField(default=0)
    reviews = models.TextField(blank=False, default="")
    created_time = models.DateTimeField(auto_now_add=True, null=True)
    modified_time = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        ordering = ['-up_votes', '-down_votes', '-release_date']