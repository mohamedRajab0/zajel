import json
from channels.generic.websocket import WebsocketConsumer
import logging
from .models import ZajelGroup, ZajelMessage
from django.shortcuts import get_object_or_404
from django.template.loader import render_to_string
from asgiref.sync import async_to_sync

logger = logging.getLogger(__name__)

class MyConsumer(WebsocketConsumer):
    
    def connect(self):
        self.user = self.scope['user']
        self.group_name = self.scope['url_route']['kwargs']['uri']
        self.chatroom = get_object_or_404(ZajelGroup, group_name=self.group_name)
        logger.info(f"Connecting to chatroom: {self.chatroom}")
        async_to_sync(self.channel_layer.group_add)(
            self.group_name,
            self.channel_name
        )
        self.accept()

    def disconnect(self, close_code):
        logger.info(f"Disconnecting from chatroom: {self.chatroom}")
        async_to_sync(self.channel_layer.group_discard)(
            self.group_name,
            self.channel_name
        )

    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        body = text_data_json['body']
        logger.info(f"Received message: {body} from user: {self.user}")
        message = ZajelMessage.objects.create(author=self.user, body=body, group_name=self.chatroom)
       
        event = {
            'type': 'message_handler',
            'message_id': message.id,
        }
       
        async_to_sync(self.channel_layer.group_send)(
            self.group_name, event
        )
    
    def message_handler(self, event):  # Corrected method name
        message_id = event['message_id']
        message = ZajelMessage.objects.get(id=message_id)
        context = {
            'message': message,
            'user': self.user,
            'group_name': self.group_name,
        }
        logger.info(f"Handling message: {message} in chatroom: {self.chatroom}")
        html = render_to_string('chat_messages.html', context=context)
        self.send(text_data=json.dumps({'html': html}))
