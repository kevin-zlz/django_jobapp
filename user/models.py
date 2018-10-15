from django.db import models
import json
# Create your models here.
#用户信息表为从表
class UserInfo(models.Model):
    # id=models.AutoField(primary_key=True)
    telephone=models.CharField(unique=True,max_length=30)
    password=models.CharField(max_length=30)
    # icon=models.CharField(max_length=100,default='user.jpg')
    pub_time=models.DateTimeField(auto_now_add=True)
    email=models.CharField(max_length=50,null=True)
    field02=models.CharField(max_length=50,null=True)
    # 新建外键约束
    # 外键约束的名称:leixing_id
    leixing=models.ForeignKey(to='Type',to_field='id',on_delete=models.CASCADE,default=1)

    def __str__(self):
        user={}
        user['telephone']=self.telephone
        user['password']=self.password
        # user['pub_time']=self.pub_time.strftime()
        return json.dumps(user)


class UserAddress(models.Model):
    address=models.CharField(max_length=100)
    add_time=models.DateTimeField(auto_now_add=True)
    yonghu=models.ForeignKey(to='UserInfo',to_field='id',on_delete=models.CASCADE)

# 类型表为主表
class Type(models.Model):
    name=models.CharField(unique=True,max_length=50)

