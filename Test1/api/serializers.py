from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import Student

class StudentSerializer(ModelSerializer):
    class Meta:
        model=Student
        fields=['id','first_name','last_name','roll','city']

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.first_name=validated_data.get("first_name", instance.first_name)
        instance.last_name=validated_data.get("last_name", instance.last_name)
        instance.roll=validated_data.get("roll", instance.roll)
        instance.city=validated_data.get("city", instance.city)
        instance.save()
    
        return instance