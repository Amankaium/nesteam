from django.urls import path, include
from .views import users_list, user_info, UserViewSet
from rest_framework import routers


router = routers.DefaultRouter()
router.register(r'api-users', UserViewSet)

urlpatterns = [
    path('list/', users_list, name='users-list'),
    path('detail/<int:pk>/', user_info, name='users-info'),
    path('user-router/', include(router.urls)),
]
