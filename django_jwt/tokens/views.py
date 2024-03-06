from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens  import RefreshToken
from django.http import JsonResponse
from rest_framework.permissions import IsAuthenticated
# Create your views here.

class LoginView(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')
        user=authenticate(username=username,password=password)
        refresh=RefreshToken.for_user(user)
        response={
            'refresh':str(refresh),
            'access':str(refresh.access_token)
        }
        return JsonResponse(response)
class RestrictedView(APIView):
    permission_classes=[IsAuthenticated]
    def get(self,request,format=None):
        return JsonResponse({"response":"You are allowed here"})



