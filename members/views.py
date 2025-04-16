from django.shortcuts import render
from django.http import HttpResponse
from rest_framework_simplejwt.views import TokenObtainPairView 
from rest_framework import generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny  # 👈 this fixes the error
from .serializers import RegisterSerializer, CustomTokenObtainPairSerializer
from django.contrib.auth.models import User
# from .serializers import CustomTokenObtainPairSerializer


@api_view(['GET'])
@permission_classes([AllowAny])
def members(request):
    return HttpResponse("Hello world ghdfgdfgdf!")

class CustomLoginView(TokenObtainPairView):
    serializer_class = CustomTokenObtainPairSerializer

class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
