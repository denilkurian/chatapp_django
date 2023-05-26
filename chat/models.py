from django.db import models
from django.contrib.auth.models import User


########## personal chat model
class ChatModel(models.Model):
    sender = models.CharField(max_length=100,default=None)
    messages = models.TextField(null=True,blank=True)
    thread_name = models.CharField(null=True,blank=True,max_length=500)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.messages
    

############  dp ststus setting
class Personal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    image = models.ImageField(upload_to='image/',max_length=400,blank=True)
    status = models.CharField(null=True,blank=True,max_length=500)

    def __str__(self):
        return self.status








