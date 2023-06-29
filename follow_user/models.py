from django.db import models
from user_app.models import User

# Create your models here.


class SendRequest(models.Model):

    STATUS_TYPE_CHOICES = (
        ('Follow', 'follow'),
        ('Following', 'following'),
        ('Requested', 'requested'),
        ('Confirm', 'confirm'),
        ('Delete', 'delete'),
        ('Accept', 'accept')
    )
    status = models.CharField(
        max_length=20, choices=STATUS_TYPE_CHOICES, null=True, default='Follow')
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='send', null=True)
    current_time = models.DateTimeField(auto_now_add=True)
    sender = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='request_user', null=True)
    receive = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='receive', null=True)

    def save(self, *args, **kwargs):
        if self.sender:
            self.status = SendRequest.STATUS_TYPE_CHOICES[2][0]
        elif self.receive:
            self.status = SendRequest.STATUS_TYPE_CHOICES[3][0]
        super().save(*args, **kwargs)


class Post(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post', null=True)
    image = models.ImageField(upload_to='post/image', blank=True)
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
