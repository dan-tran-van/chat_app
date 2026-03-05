from django.contrib import admin

from chat_app.chats.models import Conversation
from chat_app.chats.models import Message

# Register your models here.

admin.site.register(Conversation)
admin.site.register(Message)
