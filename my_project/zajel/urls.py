from django.urls import path
from .models import *
from .views import *

urlpatterns = [
    path('', index, name='index')
]
