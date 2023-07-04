from django import template

register = template.Library()


@register.filter
def is_request_sent(user, sender):
    return user.send.filter(sender=sender).exists()


