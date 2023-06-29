from django.urls import path
from user_app import views

app_name = "user_app"

urlpatterns = [
    path('', views.home, name="home"),
    path('signup/', views.SignupView.as_view(), name='signup'),
    path('login/', views.LoginView.as_view(), name='login')
]
