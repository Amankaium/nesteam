from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from .serializers import UserListSerializer


def users_list(request):
    users = User.objects.all()
    serializer = UserListSerializer(users, many=True)
    data = serializer.data
    return JsonResponse(data, safe=False)


def user_info(request, pk):
    user_object = User.objects.get(pk=pk)
    serializer = UserListSerializer(user_object)
    return JsonResponse(serializer.data, safe=False)
