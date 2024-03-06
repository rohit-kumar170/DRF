"""
URL configuration for gs7 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('studentapi',views.StudentViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls),)
    #path('studentapi/',views.StudentList.as_view(),name='StuList'),
   # path('studentapi/',views.StudentCreate.as_view(),name='StuCreate'),
    #path('studentapi/<int:pk>/',views.StudentRetrieve.as_view())
    #path('studentapi/<int:pk>/',views.StudentUpdate.as_view()),
   # path('studentapi/<int:pk>/',views.StudentDestroy.as_view()),
   # path('studentapi/',views.StudentListCreate.as_view(),name='StuList'),

]