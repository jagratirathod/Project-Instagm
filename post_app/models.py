from django.db import models
from user_app.models import User
from django.utils import timezone
from django.conf import settings
from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save

# Create your models here.

class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post', null=True)
    image = models.ImageField(upload_to='post/image', blank=True)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

@receiver(post_save, sender=Post)
def send_notification(sender,instance,created,**kwargs):
    if created:
        subject = "Thought of the day"
        email_from = settings.EMAIL_HOST_USER
        recipient_list = ['jagratirathod02@gmail.com']
        message = f'Hii {instance.user.first_name} {instance.user.last_name} , A New Post Title  "{instance.title}" has been Posted'
        send_mail(subject,message,email_from,recipient_list)
    

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