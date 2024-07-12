from django.urls import path
from .consumer import *

websocket_urlpatterns = [
    path('ws/<str:uri>/', MyConsumer.as_asgi()),
]