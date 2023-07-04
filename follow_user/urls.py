from django.urls import path
from follow_user import views

app_name = "follow_user"

urlpatterns = [
    path('', views.home, name="home"),
    path('user/', views.AllUser.as_view(), name='user'),
    path('update_status/', views.update_status, name='update_status'),
    path('notification/', views.Notification.as_view(), name='notification'),
    path('following/', views.start_following, name='following'),
    path('delete_request/<int:pk>/',views.Requestdelete.as_view(), name='delete_request'),

    path('profile-update/<int:pk>/', views.ProfileUpdateView.as_view(), name='profile-update'),
    path('profile/', views.profile,name='profile'),
]

