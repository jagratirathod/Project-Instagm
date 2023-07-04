from django.urls import path
from chat_app import views

app_name = "chat_app"

urlpatterns = [
    path('home/', views.home, name='home'),
    path('chat_room/', views.chat_room, name='chat_room'),
    path('send_message/', views.send_message, name='send_message'),
]
