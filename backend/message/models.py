from django.db import models
import uuid
from user.models import User

class ChatRoom(models.Model):
    def limit_population(population):
        if population > 100:
            raise ValueError("Room is currently full!")

    id = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4)
    population = models.IntegerField(validators=[limit_population], default=1, blank=False)
    author = models.OneToOneField(User, related_name="author", blank=False, on_delete=models.CASCADE)
    visitors = models.ManyToManyField(User, related_name="visitors", blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Room: " + str(self.id) + " Created by: " + self.author
    
class Text(models.Model):
    text_choices = {
        ("Delivered", "Delivered"),
        ("Read", "Read")
    }
    chatroom_id = models.ForeignKey(ChatRoom, related_name="Text", on_delete=models.CASCADE)
    text = models.TextField(max_length=350, default="")
    author = models.ForeignKey(User, related_name="TextAuthor", on_delete=models.CASCADE)
    reciever = models.ForeignKey(User, related_name="TextReciever", on_delete=models.CASCADE)
    status = models.CharField(blank=False, choices=text_choices, max_length=10)
    time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.text

