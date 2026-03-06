from django.urls import path

from chat_app.chats.consumers import ChatConsumer
from chat_app.chats.consumers import NotificationConsumer

websocket_urlpatterns = [
    path("chats/<conversation_name>/", ChatConsumer.as_asgi()),
    path("notifications/", NotificationConsumer.as_asgi()),
]
