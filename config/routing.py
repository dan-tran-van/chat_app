from django.urls import path

from chat_app.chats.consumers import ChatConsumer

websocket_urlpatterns = [
    path("<conversation_name>/", ChatConsumer.as_asgi()),
]
