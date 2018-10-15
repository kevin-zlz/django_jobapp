from django.shortcuts import render
import json

from django.http import HttpResponse, response, JsonResponse

from django.shortcuts import redirect, reverse
from datetime import datetime, timedelta
from django.core import serializers
from datetime import datetime

from . import models
# Create your views here.
def personal(request):
    return HttpResponse('i am personal')
def login_bak(request):
    # resp=HttpResponse()
    if request.method == 'POST':
        user = json.dumps(request.body)
        # 异常，要在settings文件中，放行
        mytoken = request.META.get('HTTP_TOKEN')
        print(mytoken)
        result = {
            "code": "800"
        }
        # data body部分
        resp = response.HttpResponse(json.dumps(result), status=200, charset='utf-8', content_type='application/json')
        date_int = datetime.utcnow() + timedelta(hours=1)
        # resp.set_cookie('token','1234567890',expires=date_int)

        # 把token放在header中传给客户端
        # data header部分
        resp['token'] = '888888888888888888888888888'
        resp['Access-Control-Expose-Headers'] = 'token'
        return resp
    else:
        # return HttpResponse('{"code":"404"}')
        result = {
            "code": "800"
        }
        resp = JsonResponse(result, status=200, charset='utf-8', content_type='application/json')
        date_int = datetime.utcnow() + timedelta(hours=1)
        resp.set_cookie('token', '1234567890'.encode('utf-8'), expires=date_int)
        return resp
def getuserbyid(request, id):
    try:
        uu = models.UserInfo.objects.filter(id=id).first()
        # uu = models.UserInfo.objects.filter(id=id)
        # uu = models.UserInfo.objects.get(id=id)
        print(uu)
        return HttpResponse(str(uu))
    except Exception as ex:
        return JsonResponse({"code": "408"})


def regist(request):
    user = {
        "telephone": "13812790420",
        "password": "123456",
        "pub_time": datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    }
    if request.method == 'POST':
        try:
            uu = models.UserInfo.objects.create(**user)
            print(uu.id)
            return JsonResponse({"code": "808"})
        except Exception as ex:
            return JsonResponse({"code": "408"})
    else:
        return JsonResponse({"code": "408"})


def login(request):
    if request.method == 'POST':
        print(request.body)
        user = json.loads(request.body)
        print(user)
        # result=models.UserInfo.objects.filter(telephone=user['telephone'],password=user['password'])
        num = models.UserInfo.objects.filter(telephone=user['telephone'], password=user['password']).count()
        if num:
            return JsonResponse({"code": "808"})
        else:
            return JsonResponse({"code": "408"})
    else:
        return JsonResponse({"code": "408"})


def add(request):
    if request.method == 'POST':
        try:
            #此处添加数据

            # t={
            #     "name":"vip"
            # }
            #
            # obj_t=models.Type.objects.create(**t)
            # return JsonResponse({"code": "808"})
            # 要求：添加一个VIP用户，188

            # # vip=models.Type.objects.filter(name='vip').first()
            vip=models.Type.objects.get(name='vip')

            #用户信息
            u={
                "telephone":"188",
                "password":"111",
                "leixing":vip
            }
            obj_u=models.UserInfo.objects.create(**u)
            return JsonResponse({"code": "808","tel":u['telephone']})

        except Exception as ex:
            return JsonResponse({"code": "408"})

    else:
        return JsonResponse({"code": "408"})

#表连接查询：一对多
def query(request):
    if request.method == 'GET':
        try:
            # 此处查询数据

            #1. 正向查询
            # u=models.UserInfo.objects.filter(telephone='188').values('id','telephone','pub_time','leixing__name').first()
            #
            # print(u)

            #2. 逆向查询
            # t=models.Type.objects.get(name='vip')
            # users=t.userinfo_set.filter(telephone='110').values('id','telephone','password')
            # print(users)
            #

            #3. 利用双下划线查询
            # u = models.UserInfo.objects.filter(leixing__name='vip').values('id', 'telephone', 'pub_time','leixing__name')
            #
            # print(u)


            # 三张表连接查询

            # u=models.UserInfo.objects.all().values('id','telephone','leixing__name','dizhi__')

            # adds=models.UserAddress.objects.filter(id=1).values('address','dizhi__id','dizhi__telephone','dizhi__leixing__name')
            adds=models.UserAddress.objects.filter(id=1,dizhi__telephone='188',yonghu__leixing__name='vip').\
                values('address','yonghu__id','yonghu__telephone','yonghu__leixing__name')
            # print(u)
            return JsonResponse({"code": "808"})
        except Exception as ex:
            return JsonResponse({"code": "408"})

    else:
        return JsonResponse({"code": "408"})

