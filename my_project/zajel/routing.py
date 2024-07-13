from django.urls import path
from .consumer import MyConsumer

websocket_urlpatterns = [
    path('ws/chat/<str:uri>/', MyConsumer.as_asgi()),
]
