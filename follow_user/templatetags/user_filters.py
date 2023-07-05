from django import template
from follow_user.models import SendRequest

register = template.Library()


@register.filter
def is_request_sent(user, sender):
    return user.send.filter(sender=sender).exists()


@register.filter
def get_no_of_following(request):
    return SendRequest.objects.filter(user__email=request.user,status="Following").count()


@register.filter
def get_no_of_follower(request):
    return SendRequest.objects.filter(user__email=request.user,status="Accept").count()
