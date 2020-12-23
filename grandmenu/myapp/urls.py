#適宜プロジェクトごとに追加するファイル
from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path, include

app_name = 'myapp'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
]