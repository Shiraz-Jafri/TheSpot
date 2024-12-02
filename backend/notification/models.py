from django.db import models
from user.models import User

class Notification(models.Model):
    message = models.CharField(max_length=150, blank=False)
    reciever = models.OneToOneField(User, related_name="NotificationReciever", on_delete=models.CASCADE)
    posted = models.DateTimeField(auto_now_add=True)
