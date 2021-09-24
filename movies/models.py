from django.contrib.auth.models import User
from django.db import models


class Movie(models.Model):
    title = models.CharField(max_length=64, db_index=True)
    released_at = models.DateField(null=True)
    image_url = models.TextField(null=True)


class Score(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
