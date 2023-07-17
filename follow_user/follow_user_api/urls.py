from django.urls import path
from .import views

app_name = "follow_user.follow_user_api"

urlpatterns = [
    path('', views.CheckAPI.as_view(), name="check"),
    path('user/', views.AllUserView.as_view(), name="user"),
    path('notification/', views.NotificationView.as_view(), name="notification"),
    path('update_status/', views.UpdateStatusView.as_view(), name="update_status"),
    path('start_following/', views.StartFollowing.as_view(), name="start_following"),
    path('requestdelete/<int:pk>/', views.Requestdelete.as_view(), name="requestdelete"),
    path('profile_update/<int:pk>/', views.ProfileUpdateView.as_view(), name="profile_update"),
    path('profile/<int:pk>/', views.ProfileView.as_view(), name="profile"),
]


