from django.urls import path
from .views import chatbot_view, home_view

urlpatterns = [
    path("", home_view, name="home"),            # Homepage view for /
    path("chatbot/", chatbot_view, name="chatbot_view"),  # AJAX endpoint
]
