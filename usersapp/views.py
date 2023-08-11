from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from rest_framework.viewsets import ModelViewSet
from .serializers import *


def users_list(request):
    users = User.objects.all()
    serializer = UserListSerializer(users, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)


def user_info(request, pk):
    user_object = User.objects.get(pk=pk)
    serializer = UserListSerializer(user_object)
    return JsonResponse(serializer.data, safe=False)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
