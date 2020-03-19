import jwt
from django.contrib.auth import get_user_model, user_logged_in
from django.http import Http404
from rest_framework import permissions, generics
from rest_framework import response, decorators, permissions, status
from rest_framework.decorators import api_view, permission_classes, action
from rest_framework.generics import RetrieveAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_jwt.serializers import jwt_payload_handler

from datawizT3 import settings
from .serializers import UserCreateSerializer, UserSerializer

User = get_user_model()



@decorators.api_view(["POST"])
@decorators.permission_classes([permissions.AllowAny])

def registration(request):
    serializer = UserCreateSerializer(data=request.data)
    if not serializer.is_valid():
        return response.Response(serializer.errors, status.HTTP_400_BAD_REQUEST)
    user = serializer.save()

    return response.Response(status.HTTP_201_CREATED)


# class UserList(generics.ListAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     permission_classes = [IsAuthenticated]
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
