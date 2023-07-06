from django import template
from follow_user.models import SendRequest
from post_app.models import Post


register = template.Library()


@register.filter
def is_request_sent(user, sender):
    return user.send.filter(sender=sender).exists()


@register.filter
def get_no_of_following(user_id):
    return SendRequest.objects.filter(user=user_id,status="Following").count()


@register.filter
def get_no_of_follower(user_id):
    return SendRequest.objects.filter(user=user_id,status="Accept").count()


@register.filter
def get_no_post(user_id):
    return Post.objects.filter(user=user_id).count()
