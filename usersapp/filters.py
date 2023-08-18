from django_filters import rest_framework as filters
from .models import Player


class PlayerFilter(filters.FilterSet):
    nick = filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Player
        fields = ['nick']
