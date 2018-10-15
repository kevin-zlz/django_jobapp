"""django_jobapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
# from django.urls import path,include
from django.conf.urls import url,include

from django.shortcuts import reverse,redirect
from . import views

#主路由
urlpatterns = [
    url(r'admin/', admin.site.urls),
    # 匹配空路由
    url(r'^$', views.index,name='myindex'),
    #路由部分
    url(r'^user/', include('user.urls',namespace='django_jobapp.user')),
    url(r'^job/', include('job.urls',namespace='django_jobapp.job')),

]
