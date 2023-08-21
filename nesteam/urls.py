"""
URL configuration for nesteam project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from games.views import *
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'genre', GenreViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('games/', games_list, name='games'),
    # path('create-game/', CreateGameAPIView.as_view(), name='create-game'),
    path('games/', GamesView.as_view(), name='games'),
    path('games-search/', GamesSearchView.as_view(), name='games-search'),
    path('game-create/', GameCreateAPIView.as_view(), name='games'),
    path('studios/', StudiosListAPIView.as_view(), name='games'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('users/', include('usersapp.urls')),
    path('collections/', include('collection.urls')),
    path('', include(router.urls)),
]
