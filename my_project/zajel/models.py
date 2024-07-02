from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class ZajelMessage(models.Model):
    group_name = models.ForeignKey('ZajelGroup', on_delete=models.CASCADE, related_name='chat_messages', blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

   

class ZajelGroup(models.Model):
    group_name = models.CharField(max_length=50)
    members = models.ManyToManyField(User, related_name='chat_groups', blank=True)
    admin = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='admin', blank=True, null=True)
    is_private = models.BooleanField(default=False)