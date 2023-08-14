from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import GameCollection
from .serializers import CollectionSerializer


class CollectionViewSet(ModelViewSet):
    queryset = GameCollection.objects.all()
    serializer_class = CollectionSerializer
