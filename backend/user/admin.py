from django.contrib import admin
from .models import User, UserProfile

admin.register(User)
admin.register(UserProfile)