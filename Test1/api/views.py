from django.shortcuts import render
from .serializers import StudentSerializer
from .models import Student
from rest_framework.views import APIView
from django.http import JsonResponse
from rest_framework.response import Response
# Create your views here.

class StudentAPI(APIView):
    def get(self, request, id=None):  
        
        if id is not None:  
                result = Student.objects.get(id=id) 
                serializers = StudentSerializer(result)  
                return Response(serializers.data)  
        
        else:
             result = Student.objects.all()  
             serializers = StudentSerializer(result, many=True)  
             return Response({'status': 'success', "students":serializers.data}, status=200)  
    
    def post(self,request,*args,**kwargs):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors)
    
    def put(self,request,id):
         stu=Student.objects.get(id=id)
         serializer=StudentSerializer(stu,data=request.data)
         if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
         return Response(serializer.errors)
    
    def patch(self,request,id):
        stu=Student.objects.get(id=id)
        serializer=StudentSerializer(stu,data=request.data,partial=True)
        if serializer.is_valid():
              serializer.save()
              return Response(serializer.data)
        return Response(serializer.errors)
   




