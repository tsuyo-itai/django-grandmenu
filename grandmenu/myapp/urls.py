#適宜プロジェクトごとに追加するファイル
from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('store_setting/', views.store_setting, name='store_setting'),
    path('store_mypage/', views.store_mypage, name='store_mypage'),
    path('store_mypage/edit/', views.store_mypage_edit, name='store_mypage_edit'),
    path('debug_websocket/', views.debug_websocket, name='debug_websocket'),    #debug
    path('debug_websocket/<slug:room_name>/', views.debug_websocket_room, name='debug_websocket_room'),     #debug
]