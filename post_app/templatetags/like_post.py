from django import template

register = template.Library()
from post_app. models import LikePost,Post
from django.db.models import Sum

@register.filter
def number_of_likes(post_id):
    likes_sum = Post.objects.filter(id=post_id).values_list('user')
    likes_sum = LikePost.objects.filter(like_by__in = likes_sum,post = post_id).values_list("number_of_likes",flat=True).last()  
    return likes_sum if likes_sum  else 0
        
# @register.filter
# def number_of_likes(post_id):
#     likes_sum = LikePost.objects.filter(post=post_id).aggregate(Sum("number_of_likes"))['number_of_likes__sum']
#     return likes_sum if likes_sum  else 0
        
