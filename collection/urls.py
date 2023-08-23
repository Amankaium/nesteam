from rest_framework import routers
from django.urls import path, include
from .views import *


collection_router = routers.DefaultRouter()
collection_router.register(r'', CollectionViewSet)


urlpatterns = [
    path('user-collection/', UserCollectionAPIView.as_view(), name='user-collection'),
    path('', include(collection_router.urls)),
]
