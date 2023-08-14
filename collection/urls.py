from rest_framework import routers
from django.urls import path, include
from .views import CollectionViewSet


collection_router = routers.DefaultRouter()
collection_router.register(r'', CollectionViewSet)


urlpatterns = [
    path('', include(collection_router.urls))
]
