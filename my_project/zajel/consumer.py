# consumers.py
import json
from channels.generic.websocket import WebsocketConsumer
import logging
from .models import ZajelGroup, ZajelMessage
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string

logger = logging.getLogger(__name__)

class MyConsumer(WebsocketConsumer):
    
    def connect(self):
        self.user = self.scope['user']
        self.group_name = self.scope['url_route']['kwargs']['uri']
        self.chatroom = get_object_or_404(ZajelGroup, group_name=self.group_name)
        self.accept()


    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        body = text_data_json['body']
        message = ZajelMessage.objects.create(author=self.user, body=body, group_name=self.chatroom)
        context = {
            'message': message,
            'user': self.user,
        }
        html = render_to_string('chat_messages.html', context)
        self.send(text_data=html)
            