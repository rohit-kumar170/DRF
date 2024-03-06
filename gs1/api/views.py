from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
# Create your views here.

def student_detail(request,pk):
    stu=Student.objects.get(id=pk)
    serializer=StudentSerializer(stu)
    #json_data=JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data)

#Queruy set-All Studentb Data
def student_list(request):
    stu=Student.objects.all()
    serializer=StudentSerializer(stu,many=True)
    #json_data=JSONRenderer().render(serializer.data)
    #return HttpResponse(json_data,content_type='application/json')
    return JsonResponse(serializer.data,safe=False)


