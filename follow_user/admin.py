from django.contrib import admin
from .models import SendRequest

# Register your models here.


class SendRequestAdmin(admin.ModelAdmin):
    list_display = ['id', 'status', 'user',
                    'current_time', 'sender', 'receive']
admin.site.register(SendRequest, SendRequestAdmin)




