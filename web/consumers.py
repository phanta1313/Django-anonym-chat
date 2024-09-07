import json
from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync
from django.db.models import F
from .models import Lobby

class ChatConsumer(WebsocketConsumer):
    def connect(self):
        try:
            to_join = Lobby.objects.filter(members__exact=1).values_list('id', flat=True)[0]
        except:
            to_join = Lobby.objects.create().id

        self.room_id = str(to_join)

        Lobby.objects.filter(id__exact=self.room_id).update(members=F('members') + 1)
        self.members = Lobby.objects.get(id=self.room_id).members

        async_to_sync(self.channel_layer.group_add)(
            self.room_id,
            self.channel_name
        )
        self.accept()
   
    def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['message']

        async_to_sync(self.channel_layer.group_send)(
            self.room_id,
            {
                'type':'chat_message',
                'message':message,
            }
        )

    def chat_message(self, event):
        message = event['message']

        self.send(text_data=json.dumps({
            'type':'chat',
            'message':message
        }))

    def disconnect(self, code):
        Lobby.objects.filter(id__exact=self.room_id).delete()
        return super().disconnect(code)
