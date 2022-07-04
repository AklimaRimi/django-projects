import json

from channels.generic.websocket import WebsocketConsumer

from asgiref.sync import async_to_sync,sync_to_async
from .models import message,room


class chatconsumer(WebsocketConsumer):
    def connect(self):
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = '%s'%self.room_name
        
        
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,
            self.channel_name,
        )
        
        self.accept()

        self.send(text_data=json.dumps({
            'type':'connection',
            'message':'ready'
        }))
        
    def receive(self, text_data):
        data = json.loads(text_data)
        message = data['message']
        user = data['user']
        room_name = data['room_name']
        print(f'{user}-{message}')
        self.save_message(room_name,user,message)
        
        
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name,
            {
                'type':'chat_message',
                'message':message,
                'user':user,
                'room_name':room_name
            }
        )
    def chat_message(self,event):
        message=event['message']
        user = event['user']
        room_name = event['room_name']
        
        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message,
            'user':user,
            'room_name':room_name,
        }))
        
    def save_message(self,room_name,name,msg):
        x = room.objects.get(name=room_name)
        message.objects.create(room = x,name=name,msg=msg)
        print('created')
        
