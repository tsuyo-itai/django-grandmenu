from django.urls import path
from . import consumers


websocket_urlpatterns = [
    path('ws/debug_websocket/<slug:room_name>/', consumers.WSConsumer.as_asgi()),
]