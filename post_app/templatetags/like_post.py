from django import template

register = template.Library()
from post_app. models import LikePost
from django.db.models import Sum

@register.filter
def number_of_likes(post_id):
    likes_sum = LikePost.objects.filter(post=post_id).aggregate(Sum("number_of_likes"))['number_of_likes__sum']
    return likes_sum if likes_sum  else 0
        
