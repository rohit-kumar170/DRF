from django.shortcuts import render
from rest_framework.decorators import api_view,authentication_classes,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication
from .models import Student
from .serializers import StudentSerializer
from rest_framework.response import Response

# Create your views here.

@api_view(['GET','POST','PUT','PATCH','DELETE'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def student_api(request,id=None):
    if request.method=='GET':
        if id is not None:
            stu=Student.objects.get(id=id)
            serializer=StudentSerializer(stu)
            return Response(serializer.data)
        stu=Student.objects.all()
        serializer=StudentSerializer(stu,many=True)
        return Response(serializer.data)
    
    if request.method=="POST":
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data={
                'msg':"Data Created !"
            }
            return Response(response_data)
        return Response(serializer.errors)
    
    if request.method=="PUT":
        id=request.data.get('id')
        stu=Student.objects.get(pk=id)
        serializer=StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            response_data={
                'msg':"Data Updated !."
            }
            return Response(response_data)
        return Response(serializer.errors)
    
    if request.method=="DELETE":
        stu=Student.objects.get(id=id)
        stu.delete()
        response_data={
            'msg':'Data Deleted!.'
        }
        return Response(response_data)
    
    if request.method=="PATCH":
        id=request.data.get('id')
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            response_data={
                'msg':"Data partially Updated !."
            }
            return Response(response_data)
        return Response(serializer.errors)
    
    




