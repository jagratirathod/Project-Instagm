from django.contrib import admin
from .models import SendRequest, Post

# Register your models here.


class SendRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'user',
                    'current_time', 'sender', 'receive']


admin.site.register(SendRequest, SendRequestAdmin)


class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'image', 'title', 'created_at']


admin.site.register(Post, PostAdmin)
