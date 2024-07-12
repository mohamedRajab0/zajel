# consumers.py
import json
from channels.generic.websocket import WebsocketConsumer
import logging

logger = logging.getLogger(__name__)

class MyConsumer(WebsocketConsumer):
    def connect(self):
        if 'group_name' in self.scope['url_route']['kwargs']:
            self.group_name = self.scope['url_route']['kwargs']['group_name']
            logger.info("WebSocket connected to group: %s", self.group_name)
            self.accept()
        else:
            logger.error("No 'group_name' key found in URL route kwargs.")
            

    def disconnect(self, close_code):
        logger.info("WebSocket disconnected with code: %s", close_code)

    def receive(self, text_data):
        logger.info("Received data: %s", text_data)
        try:
            # Process the received data
            response = {"message": "Data received"}
            self.send(text_data=json.dumps(response))
        except json.JSONDecodeError as e:
            logger.error("Error decoding JSON: %s", e)
            self.send(text_data=json.dumps({"error": "Invalid JSON"}))
