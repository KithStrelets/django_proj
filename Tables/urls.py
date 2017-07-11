from django.conf.urls import url
from . import views

app_name = 'Tables'

urlpatterns = [

    url(r'^/index$', views.index),
    url(r'^/jobs$', views.jobs),
    url(r'^/workers$', views.workers),
    url(r'^/storage$', views.storage),
    url(r'^/menu$', views.menu),
    url(r'^/order$', views.order),
    url(r'^/personneldep$', views.personneldep),
    url(r'^/restmenu$', views.restmenu),
    url(r'^/orderqueue$', views.orderqueue)
    #url(r'/^jobs/all/$/', views.jobs),
    #url(r'/^/get/(?P<job_id>\d+)$/', views.job),
]