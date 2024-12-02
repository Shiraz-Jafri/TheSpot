from django.db import models
from user.models import User

class FriendProfile(models.Model):
    stat_choices = {
        ("online", "Online"),
        ("offline", "Offline")
    }

    # bond - score to display how strong the bond is with this friend
    # start - date to represent when user and friend became friends
    friend = models.OneToOneField(User, related_name="Friend", on_delete=models.CASCADE)
    status = models.CharField(max_length=7, default="Offline", blank=False, choices=stat_choices)
    bond = models.IntegerField(default=0, blank=False)
    start = models.DateField(auto_now=True)
    img = models.ImageField(default="friend.jpg", upload_to="friend/profile/")
    bio = models.TextField(max_length=250)
    friends = models.ManyToManyField(User, related_name="FriendFriends", blank=True)
    followers = models.ManyToManyField(User, related_name="FriendFollowers", blank=True)
    following = models.ManyToManyField(User, related_name="FriendFollowing", blank=True)

