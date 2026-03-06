from django.conf import settings
from rest_framework.routers import DefaultRouter
from rest_framework.routers import SimpleRouter

from chat_app.chats.api.views import ConversationViewSet
from chat_app.chats.api.views import MessageViewSet
from chat_app.users.api.views import UserViewSet

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("users", UserViewSet)
router.register("conversations", ConversationViewSet)
router.register("messages", MessageViewSet)


app_name = "api"
urlpatterns = router.urls
