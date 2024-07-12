from django.urls import path
from .models import *
from zajel.views import index
urlpatterns = [
    path('', index, name='index'),
    path('ws/<str:room_name>/', name='ws'),
    
]
