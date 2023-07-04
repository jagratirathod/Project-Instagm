from django.db import models
from user_app.models import User
from django.utils import timezone


# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post', null=True)
    image = models.ImageField(upload_to='post/image', blank=True)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class LikePost(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='users', null=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='like', null=True)
    number_of_likes = models.IntegerField(default=0)
    
   

class CommentPost(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='comment', null=True)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name='comment_post', null=True)
    message = models.CharField(max_length=90)
    created_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.message 