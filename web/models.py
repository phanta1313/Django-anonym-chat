from django.db import models
import uuid

class Lobby(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, 
                          primary_key=True, editable=False)
    members = models.IntegerField(default=0, editable=False)
