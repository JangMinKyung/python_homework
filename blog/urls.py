<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list)
=======
from django.urls import re_path
from . import views
from . import views_cbv

urlpatterns = [
    re_path(r'^sum/(?P<numbers>[\d/]+)/$', views.mysum),
    re_path(r'^hello/(?P<name>[ㄱ-힣]+)/(?P<age>\d+)/$', views.hello),
    re_path(r'^list1/$', views.post_list1),
    re_path(r'^list2/$', views.post_list2),
    re_path(r'^list3/$', views.post_list3),
    re_path(r'^excel/$', views.excel_download),
    re_path(r'^cbv/list1/$', views_cbv.post_list1),
    re_path(r'^cbv/list2/$', views_cbv.post_list2),
    # re_path(r'^cbvlist3/$', views_cbv.post_list3),
    # re_path(r'^cbv/excel/$', views_cbv.excel_download),
>>>>>>> ee11ec72aebd03d0ab7433fbaa43232a51451322
]
