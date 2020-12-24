#適宜プロジェクトごとに追加するファイル
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path, include

app_name = 'myapp'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('debug_storeinfo/', views.debug_storeinfo, name='debug_storeinfo'),    #debug
    path('debug_storeinfolist/', views.debug_storeinfolist, name='debug_storeinfolist'),    #debug
    path('store_setting/', views.store_setting, name='store_setting'),
]