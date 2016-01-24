from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.defect_list, name='defect_list'),
]
