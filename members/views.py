from django.shortcuts import render
from django.http import HttpResponse

from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny  # 👈 this fixes the error
from .serializers import RegisterSerializer
from django.contrib.auth.models import User


@api_view(['GET'])
@permission_classes([AllowAny])
def members(request):
    return HttpResponse("Hello world ghdfgdfgdf!")


class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
