from django.conf.urls import url

from . import views
app_name = 'user'
#user子路由
urlpatterns = [
    url(r'^$',views.personal,name='personal'),
    # 后面的/不能省略
    url(r'login/', views.login, name='login'),
    url(r'add/', views.add, name='add'),
    url(r'query/', views.query, name='query'),
    url(r'regist/', views.regist, name='regist'),
    url(r'^getuser\w*/(?P<id>\d*)', views.getuserbyid, name='getuser'),

]
