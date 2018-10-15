from django.http import JsonResponse,HttpResponse
import json
from . import models

from django.db.models import Q

from django.db.models import Count, Min, Max, Sum , Avg
def job(request):
    return JsonResponse({"code": "job"})


def searchjob(request):
    try:
        qid=request.GET.get('id')
        # print(qid)
        # jobs=models.job.objects.filter(job_id=qid,title='RPA软件售前工程师（Python）').values()

        # return HttpResponse(json.dumps(list(jobs),ensure_ascii=False))
    #     删除
        affected_rows=models.job.objects.filter(job_id=qid).delete()

        print(affected_rows[0])

        if affected_rows[0]:
            return JsonResponse({"code": "808"})
        else:
            return JsonResponse({"code": "410"})
    except Exception as ex:
        return JsonResponse({"code": "409"})


def add(request):
    if request.method=='POST':
        try:
            job=json.loads(request.body)
            # print(job)
            # res就是正在插入的对象
            # res = models.job.objects.create(**job)
            # print(res.id)
            res=models.job(**job).save(force_update=True)

            print(res)
            return JsonResponse({"code": "808"})
        except Exception as ex:
            return JsonResponse({"code": "408"})

    else:
        return JsonResponse({"code": "408"})

def addall(request):
    if request.method=='POST':
        try:
            # 读取本地文件
            with open('job51python.json','r',encoding='utf-8') as fp:
                jobs=json.load(fp)
                print('****************************')
                print(len(jobs))
                for job in jobs:
                    res = models.job(**job).save()
            return JsonResponse({"code": "808"})
        except Exception as ex:
            return JsonResponse({"code": "408"})

    else:
        return JsonResponse({"code": "408"})
def getjobs(request,index,con):
    try:
        # 1. 这个时候返回的是对象集合（job对象集合）
        # jobs=models.job.objects.all()
        # for job in jobs:
        #     print(job.title)
        index=int(index)
        pagesize=20
        # 2. 获取部分列
        # jobs = models.job.objects.all().values() #取所有列
        # jobs = models.job.objects.filter(~Q(salary_min=10000)).values('title','com_name','salary_min')
        # jobs = models.job.objects.filter(com_name__in=['梅花网','上海每联每信息技术有限公司大连分公司']).values('title','com_name','salary_min')
        # jobs = models.job.objects.exclude(com_name__in=['梅花网','上海每联每信息技术有限公司大连分公司']).values('title','com_name','salary_min')
        # jobs = models.job.objects.filter(title__icontains='Python').values('title','com_name','salary_min')
        # jobs = models.job.objects.all().values('date').annotate(m=Max('salary_min'))
        if con:
            jobs = models.job.objects.filter(title__regex=con)[pagesize*(index-1):pagesize*index].values('job_id', 'title', 'com_name', 'com_address', 'date', 'salary')
        else:
            jobs = models.job.objects.all()[pagesize*(index-1):pagesize*index].values('job_id', 'title', 'com_name', 'com_address', 'date', 'salary')



        # select date, max(salary_min) as m from job group by date
        print(len(jobs))
        # 3. 获取部分列
        # jobs = models.job.objects.all().values_list('title', 'com_name')
        # print(jobs)
        return HttpResponse(json.dumps(list(jobs),ensure_ascii=False))
    except Exception as ex:
        return JsonResponse({"code": "409"})
def pagecount(request,con):
    try:
        if con:
            jobs = models.job.objects.filter(title__regex=con).values('job_id', 'title', 'com_name', 'com_address', 'date', 'salary')
        else:
            jobs = models.job.objects.all().values('job_id', 'title', 'com_name', 'com_address', 'date', 'salary')

        print(len(jobs))
        # 3. 获取部分列
        # jobs = models.job.objects.all().values_list('title', 'com_name')
        # print(jobs)
        result={
            "count":len(jobs)
        }
        return HttpResponse(json.dumps(result,ensure_ascii=False))
    except Exception as ex:
        return JsonResponse({"code": "409"})
    # pass
def query(request):
    if request.method == 'POST':
        try:
            #多对多查询
            # info={
            #     "yh_id":"138",
            #     "kw_id":"100261076"
            # }
            # res=models.toudi.objects.create(**info)
            # print(res)

            # user_id=models.toudi.objects.filter(kw_id='100261076').values('yh__id')

            # work=models.job.objects.get(job_id='100261076')
            # print(job)

            # list=[3,4,5]
            # obj=job.apply.add(*list)
            # #
            # print(obj)
            # print(work)
            # # users=work.apply.all().values('job__apply__telephone')
            # users=work.apply.all()
            #
            # print(users)

            #1. 查询3号用户投递了哪些岗位

            obj=models.toudi.objects.filter(yh_id=3).values('kw__title','kw__com_name')
            print(obj)
            return JsonResponse({"code": "808"})
        except Exception as ex:
            return JsonResponse({"code": "408"})

    else:
        return JsonResponse({"code": "408"})

# MVC model view controller
