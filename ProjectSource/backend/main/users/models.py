from django.db import models

class User(models.Model):

    first_name = models.CharField(max_length=50, default='')
    last_name = models.CharField(max_length=50, default='')
    email = models.EmailField(max_length=100, default='example@gmail.com')
    username = models.CharField(max_length=100, default='')
    password = models.CharField(max_length=50, default='')

    def __str__(self):
        return self.first_name
    