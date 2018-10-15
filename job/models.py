from django.db import models

from user.models import UserInfo
# {
#     "title": "Python开发工程师",
#     "job_url": "https://jobs.51job.com/shanghai-pdxq/107197064.html?s=01&t=0",
#     "job_id": "107197064",
#     "com_name": "上海威志信息科技有限公司",
#     "com_url": "https://jobs.51job.com/all/co2964606.html",
#     "com_address": "上海-浦东新区",
#     "salary": [
#       "1.5-2万/月"
#     ],
#     "date": "09-29",
#     "com_id": "2964606",
#     "date_stamp": 1538150400,
#     "salary_min": 15000.0,
#     "salary_max": 20000.0
#   },
class job(models.Model):
    # id=models.AutoField()
    title=models.CharField(max_length=50)
    job_id=models.CharField(max_length=50,primary_key=True)
    job_url=models.CharField(max_length=100)
    com_name=models.CharField(max_length=50)
    com_url=models.CharField(max_length=100)
    com_id=models.CharField(max_length=100)
    com_address=models.CharField(max_length=100)
    salary=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    date_stamp=models.FloatField(null=False)
    salary_min=models.FloatField()
    salary_max=models.FloatField()

    apply=models.ManyToManyField(UserInfo)

class toudi(models.Model):

    apply_time=models.DateTimeField(auto_now_add=True)
    kw=models.ForeignKey(to=job,to_field='job_id',on_delete=models.CASCADE)
    yh=models.ForeignKey(to=UserInfo,to_field='id',on_delete=models.CASCADE)


