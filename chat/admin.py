from django.contrib import admin

from .models import ChatModel,Personal

########### personalchat
admin.site.register(ChatModel)

######### personal details
admin.site.register(Personal)

########### groupchat




