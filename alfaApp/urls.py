from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.defect_list, name='defect_list'),
    url(r'^defect/(?P<pk>[0-9]+)/$', views.defect_detail, name='defect_detail'),
    url(r'^defect/new/$', views.defect_new, name='defect_new'),
    url(r'^defect/(?P<pk>[0-9]+)/edit/$', views.defect_edit, name='defect_edit'),
]
