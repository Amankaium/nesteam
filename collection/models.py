from django.db import models
from games.models import Game
from django.contrib.auth.models import User


class GameCollection(models.Model):
    name = models.CharField(max_length=55)
    games_list = models.ManyToManyField(
        to=Game,
        blank=True,
        related_name='game_collection_list'
    )
    author = models.ForeignKey(
        to=User,
        related_name='game_collection',
        verbose_name='автор',
        on_delete=models.PROTECT,
    )
    likes = models.ManyToManyField(
        to=User,
        related_name='liked_collection',
        blank=True,
    )

    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['id']