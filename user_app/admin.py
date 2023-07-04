from django.contrib import admin
from .models import User

# Register your models here.


class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'email', 'first_name','last_name', 'password','images']
admin.site.register(User, UserAdmin)
