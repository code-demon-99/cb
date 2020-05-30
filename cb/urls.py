"""cb URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path
from model.views import home_view, ResultOneViewSet, task2_view, task3_view, ResultThreeViewSet, CovidDataViewSet, ResultTwoViewSet
from django.conf.urls import url,include
from rest_framework import routers
from . import views
router = routers.DefaultRouter()
router.register(r'model_data',CovidDataViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',home_view,name='home'),
    path('task2/',task2_view,name='task2'),
    path('task3/',task3_view,name='task3'),
    path('api/get_data/res1',ResultOneViewSet.as_view({'get': 'list'}),name='res1'),
    path('api/get_data/res3',ResultThreeViewSet.as_view({'get': 'list'}),name='res2'),
    path('api/get_data/res2',ResultTwoViewSet.as_view({'get': 'list'}),name='res3'),
    url(r'^api-auth/', include('rest_framework.urls')),
    path('api/get_data/',include(router.urls)),

]
handler404 = views.handler404
handler500 = views.handler500
