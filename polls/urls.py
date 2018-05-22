from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_answer', views.add_answer, name='add_answer'),
    url('del_answer/(?P<answer_id>\d+)$', views.del_answer, name='del_answer'),
]

