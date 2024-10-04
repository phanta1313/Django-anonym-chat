from django.urls import path
from .views import Chat, Game

urlpatterns = [
    path('', Chat.as_view(), name='chat'),
    path('game/', Game.as_view(), name='game'),
]