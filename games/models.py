from django.db import models


class Genre(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()


class Game(models.Model):
    name = models.CharField(max_length=255)
    year = models.PositiveIntegerField()
    genre = models.ForeignKey(
        to=Genre,
        on_delete=models.PROTECT,
        null=True,
    )
    studio = models.ForeignKey(
        to='Studio',
        on_delete=models.PROTECT,
        null=True,
        blank=False,
    )

    def __str__(self):
        return self.name


class Studio(models.Model):
    name = models.CharField(max_length=55)
    workers_count = models.IntegerField(default=0)
    games_count = models.IntegerField(default=0)


    def __str__(self):
        return self.name

