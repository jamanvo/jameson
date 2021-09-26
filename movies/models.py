from django.db import models

from users.models import User


class Movie(models.Model):
    title = models.CharField(max_length=64, db_index=True)
    released_at = models.DateField(null=True)
    image_url = models.TextField(null=True)

    objects = models.Manager()


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)
    content = models.TextField()

    objects = models.Manager()
