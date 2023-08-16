from django_filters import rest_framework as filters
from .models import Player


class PlayerFilter(filters.FilterSet):
    class Meta:
        model = Player
        fields = ['nick']
