from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
# Create your views here.
from rest_framework.authentication import SessionAuthentication,TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly,IsAuthenticated

class StudentModelViewSet(viewsets.ModelViewSet):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer
    authentication_classes=[TokenAuthentication]
    permission_classes=[IsAuthenticated]
    
    
'''
class StudentCreate(CreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentRetrieve(RetrieveAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentUpdate(UpdateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentDestroy(DestroyAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

class StudentListCreate(ListCreateAPIView):
    queryset=Student.objects.all()
    serializer_class=StudentSerializer

'''