from django.http import HttpResponse,response,JsonResponse
from django.shortcuts import render,redirect
from django.urls import reverse
def index(request):
    # return HttpResponse('HELLO WORLD')
    # return HttpResponse('<h1>hello world</h1>')
    # getdata...
    return render(request,'index.html')


    #跨模块路由跳转
    # reverse("模块名:路由名") 注意中间的冒号
    # myurl=reverse('user:login')

    # myurl=reverse('user:getuser',kwargs={"id":12})
    # print(myurl)
    #
    # return redirect(myurl)

