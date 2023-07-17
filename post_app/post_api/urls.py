from django.urls import path
from .import views

app_name = "post_app.post_api"

urlpatterns = [
    path('', views.CheckPostAPI.as_view(), name="post_check"),
    path('list_post/', views.ListPostView.as_view(), name="list_post"),
    path('create_post/', views.CreatePostview.as_view(), name="create_post"),
    path('like_post/', views.LikePostView.as_view(), name="like_post"),

]
