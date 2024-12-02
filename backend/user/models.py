from django.db import models


# Models to make:
# - User (A model to represent user)
# - Profile (A model to represent user's profile)

class User(models.Model):
    firstName = models.CharField(max_length=100, blank=False)
    lastName = models.CharField(max_length=100, blank=False, null=False)
    email = models.EmailField(max_length=100, blank=False)
    # todo: Figure out hash algorithm for storing passwords.
    password = models.CharField(max_length=150, blank=False, unique=True)

    def __str__(self):
        return f"{self.firstName} {self.lastName}"


class UserProfile(models.Model):
    stat_choices = {
        ("online", "Online"),
        ("offline", "Offline")
    }
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    friends = models.ManyToManyField(User, related_name="UserFriends", blank=True)
    followers = models.ManyToManyField(User, related_name="UserFollowers", blank=True) 
    following = models.ManyToManyField(User, related_name="UserFollowing", blank=True)
    bio = models.TextField(blank=True, max_length=250)
    status = models.CharField(max_length=7, choices=stat_choices, blank=False)
    img = models.ImageField(default="default_profile.jpg", upload_to="static/images/profile")

    def __str__(self):
        return self.status


