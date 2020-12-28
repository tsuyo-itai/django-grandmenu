#適宜プロジェクトごとに追加するファイル
from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('debug_storeinfo/', views.debug_storeinfo, name='debug_storeinfo'),    #debug
    path('debug_storeinfolist/', views.debug_storeinfolist, name='debug_storeinfolist'),    #debug
    path('store_setting/', views.store_setting, name='store_setting'),
    path('store_mypage/', views.store_mypage, name='store_mypage'),
    path('store_mypage/edit/', views.store_mypage_edit, name='store_mypage_edit'),
]