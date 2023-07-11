from django.contrib import admin
from .models import Post , LikePost , CommentPost


# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'image', 'title', 'created_at']
admin.site.register(Post, PostAdmin)


class LikePostAdmin(admin.ModelAdmin):
    list_display = ['id','post', 'number_of_likes', 'like_by']
admin.site.register(LikePost, LikePostAdmin)


class CommentPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'post','message']
admin.site.register(CommentPost, CommentPostAdmin)
