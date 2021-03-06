from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^login/$', views.login_user, name = 'login_user'),
    url(r'^$', views.welcome_page, name='welcome_page'),
    url(r'^defect/list$', views.defect_list, name='defect_list'),
    url(r'^defect/(?P<pk>[0-9]+)/$', views.defect_detail, name='defect_detail'),
    url(r'^defect/new/$', views.defect_new, name='defect_new'),
    url(r'^defect/(?P<pk>[0-9]+)/edit/$', views.defect_edit, name='defect_edit'),
]
