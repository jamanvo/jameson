from django.db import models

from users.models import User


class Movie(models.Model):
    title = models.CharField(max_length=64, db_index=True)
    released_at = models.DateField(null=True)
    image_url = models.TextField(null=True)

    objects = models.Manager()

    def get_reviews(self, args):
        return Review.objects.filter(movie=self, score__range=(args['score_min'], args['score_max'])) \
            .order_by(f'{"-" if args["direction"] == "desc" else ""}{args["order"]}')


class Review(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.FloatField(default=0.0)
    content = models.TextField()

    objects = models.Manager()
