from django.urls import path
from . import views

app_name = "post_app"

urlpatterns = [
    path('', views.home, name="home"),
    path('list_post/', views.ListPostView.as_view(), name='list_post'),
    path('create_post/', views.CreatePostView, name='create_post'),
    path('comment_post/', views.CreateCommentView.as_view(), name='comment_post'),
    path('delete_post/<int:pk>/', views.Postdelete.as_view(), name='delete_post'),
    path('like_post/', views.LikePostView, name='like_post'),
]
