from django.db import models
import uuid
from user.models import User

class VideoRoom(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    creator = models.OneToOneField(User, related_name="VideoCallAuthor", on_delete=models.CASCADE)
    members = models.ManyToManyField(User, related_name="VideoRoomMembers")

    def __str__(self):
        return "Room ID: " + str(id) + " Created By: " + self.creator
    
