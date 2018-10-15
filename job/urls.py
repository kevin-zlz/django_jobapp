from django.conf.urls import url

from . import views
app_name = 'job'
#job子路由
urlpatterns = [
    url(r'^$',views.job,name='job'),
    # 后面的/不能省略
    url(r'add/', views.add, name='add'),
    url(r'query/', views.query, name='query'),
    url(r'addall/', views.addall, name='addall'),
    url(r'^getjobs/(?P<index>\w*)/(?P<con>\w*)', views.getjobs, name='getjobs'),
    url(r'^pagecount/(?P<con>\w*)', views.pagecount, name='pagecount'),
    url(r'^searchjob\w*/', views.searchjob, name='searchjob'),
]
