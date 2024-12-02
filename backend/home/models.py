from django.db import models
from user.models import User

class Spot(models.Model):
    name = models.CharField(max_length=150, blank=False)
    location = models.CharField(max_length=150, blank=False)
    hours = models.CharField(max_length=150, blank=True)
    followers = models.ManyToManyField(User, related_name="SpotFollowers")
    status = models.CharField(max_length=10, blank=False)

class CustomSpot(models.Model):
    name = models.CharField(max_length=150, blank=False)
    location = models.CharField(max_length=150, blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name="SpotCreator")
    created = models.DateField(auto_now=True)
    followers = models.ManyToManyField(User, related_name="CustomSpotFollowers")

    def __str__(self):
        return "Name: " + self.name + " Created BY: " + self.creator

