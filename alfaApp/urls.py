from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.defect_list, name='defect_list'),
    url(r'^defect/(?P<pk>[0-9]+)/$', views.defect_detail, name='defect_detail'),
]
