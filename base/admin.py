from django.contrib import admin

# Register your models here.
from .models import Room, Topic, Message

#models uptil now
admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
