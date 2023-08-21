from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from .serializers import *
from .models import Player
from .filters import PlayerFilter


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


class PlayerListAPIView(ListAPIView):
    queryset = Player.objects.all()
    serializer_class = PlayerSerializer
    filterset_class = PlayerFilter


    # def get(self, request):
    #     players = Player.objects.all()
    #     filter_backends = (filters.DjangoFilterBackend,)
    #     filterset_class = ProductFilter
    #     serializer = PlayerSerializer(instance=players, many=True)
    #     return Response(data=serializer.data)
        

class RegistrationAPIView(APIView):
    def post(self, request):
        data = request.data
        serializer = UserRegistrationSerializer(data=data)
        if serializer.is_valid():
            new_user = serializer.save()
            password = serializer.validated_data["password"]
            new_user.set_password(password)
            new_user.save()
            return Response("Пользователь успешно создан", 201)
        else:
            return Response("Not valid", 400)


class AuthorizationAPIView(APIView):
    def post(self, request):
        serializer = UserLoginSerializer(data=request.data)
        if serializer.is_valid():
            user_object = authenticate(
                request=request,
                username=request.data["username"],
                password=request.data["password"]
            )
            if user_object:
                token, created = Token.objects.get_or_create(user=user_object)
                return Response(data=token.key, status=200)
            else:
                return Response("Неверный логин или пароль", 400)
        else:
            return Response(serializer.errors, 400)


class AuthDRFAPIView(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
            'user_id': user.pk,
            'email': user.email
        })