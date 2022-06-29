from operator import mod
from pyexpat import model
from django.contrib.auth.models import User
from django.db import models
# Create your models here.

class Topic(models.Model):
    name=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Room(models.Model):
    host=models.ForeignKey(User,on_delete=models.SET_NULL,null=True)
    topic=models.ForeignKey(Topic, on_delete=models.SET_NULL,null=True)
    name=models.CharField(max_length=100)
    desc=models.TextField(null=True, blank=True)
    #participants=models.CharField(max_length=)
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    class Meta():
        ordering=['-updated','-created']
     
    def __str__(self):
        return self.name

# class Topic(models.Model):
#     name=models.CharField(max_length=200,null=True)
#     def __str__(self):
#         return self.name

class Message(models.Model):
    #user=models.CharField(max_length=100)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    room=models.ForeignKey(Room,on_delete=models.CASCADE)
    body=models.TextField()
    updated=models.DateTimeField(auto_now=True)
    created=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:50]