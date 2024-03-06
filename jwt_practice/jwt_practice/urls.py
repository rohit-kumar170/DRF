from django.contrib import admin
from django.urls import path,include
from api import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView,TokenVerifyView


router=DefaultRouter()

router.register('studentapi',views.StudentModelViewSet,basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('gettoken/',TokenObtainPairView.as_view(),name='token-obtain'),
    path('refreshtoken/',TokenRefreshView.as_view(),name='token-refresh'),
    path('tokenverify/',TokenVerifyView.as_view(),name='token-verify'),
   # path('auth/',include('rest_framework.urls')),
]