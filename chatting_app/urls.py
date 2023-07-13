from django.urls import path
from . import views

app_name = "chatting_app"

urlpatterns = [
    path('', views.home9, name='home'),
]
