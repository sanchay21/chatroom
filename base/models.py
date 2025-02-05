from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Topic(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name
    
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)
    name = models.CharField(max_length=200)
    desc = models.TextField(null=True, blank=True)     
    # participants = 
    updated = models.DateTimeField(auto_now=True)      # Takes time stamp every time
    created = models.DateTimeField(auto_now_add=True)  # First Time stamp only

    def __str__(self):
        return self.name

class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True) 

    def __str__(self):
        return self.body[0:50]

class Userprofile(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    bio = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
    