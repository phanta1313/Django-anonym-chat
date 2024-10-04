from django.db import models
import uuid
from mongoengine import StringField, Document


class TestMongo(Document):
    test_txt = StringField(max_length=200, required=True)


class Lobby(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    members = models.IntegerField(default=0, editable=False)
