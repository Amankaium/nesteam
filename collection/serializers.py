from .models import GameCollection
from rest_framework.serializers import ModelSerializer


class CollectionSerializer(ModelSerializer):
    class Meta:
        model = GameCollection
        # exclude = ['games_list']
        fields = '__all__'
